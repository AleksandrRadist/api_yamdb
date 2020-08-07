import random
import string

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .models import User
from .serializers import UsersSerializer
from .permissions import IsStaff


class UsersViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    permission_classes = (
        permissions.IsAuthenticated,
        IsStaff,
    )
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET', 'PATCH'])
def get_current_user(request):
    user = request.user
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def random_code_generator(size=30,
                          chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_confrm_code_generator():
    confirmation_code = random_code_generator()
    token_unique = User.objects.filter(
        confirmation_code=confirmation_code).exists()
    if token_unique:
        return random_code_generator()
    return confirmation_code


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': unique_confrm_code_generator().make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse(
                'Please confirm your email'
                ' address to complete the registration'
            )
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. '
                            'Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
