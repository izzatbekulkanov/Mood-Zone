from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .client import oAuth2Client
from core.settings import (
    CLIENT_SECRET,
    CLIENT_ID,
    REDIRECT_URI,
    RESOURCE_OWNER_URL,
    TOKEN_URL,
    AUTHORIZE_URL,
)


class OAuthAuthorizationView(APIView):
    def get(self, request, *args, **kwargs):
        client = oAuth2Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            authorize_url=AUTHORIZE_URL,
            token_url=TOKEN_URL,
            resource_owner_url=RESOURCE_OWNER_URL
        )
        authorization_url = client.get_authorization_url()
        return Response(
            {
                'authorization_url': authorization_url
            },
            status=status.HTTP_200_OK)


class OAuthCallbackView(APIView):
    def get(self, request, *args, **kwargs):
        full_info = {}
        auth_code = request.query_params.get('code')
        if not auth_code:
            return Response(
                {
                    'status': False,
                    'error': 'Authorization code is missing'
                },
                status=status.HTTP_400_BAD_REQUEST)

        client = oAuth2Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            authorize_url=AUTHORIZE_URL,
            token_url=TOKEN_URL,
            resource_owner_url=RESOURCE_OWNER_URL
        )
        access_token_response = client.get_access_token(auth_code)

        if 'access_token' in access_token_response:
            access_token = access_token_response['access_token']
            user_details = client.get_user_details(access_token)
            full_info['details'] = user_details
            full_info['token'] = access_token

            # Foydalanuvchi modeliga foydalanuvchi ma'lumotlarini qo'shish
            CustomUser = get_user_model()

            # Foydalanuvchi ma'lumotlarini olish
            email = user_details.get('email', None)
            employee_id_number = user_details.get('employee_id_number', None)

            # E-mail manzilini tekshirish va saqlash
            if email:
                user, created = CustomUser.objects.get_or_create(
                    email=email,
                    defaults={
                        'full_name': user_details.get('name', ''),
                        'first_name': user_details.get('firstname', ''),
                        'second_name': user_details.get('surname', ''),
                        'third_name': user_details.get('patronymic', ''),
                        # Boshqa ma'lumotlar
                    }
                )
            elif employee_id_number:
                # E-mail manzili mavjud emas, employee_id_number dan email yaratish
                email = f"{employee_id_number}@namspi.uz"
                user, created = CustomUser.objects.get_or_create(
                    email=email,
                    defaults={
                        'full_name': user_details.get('name', ''),
                        'first_name': user_details.get('firstname', ''),
                        'second_name': user_details.get('surname', ''),
                        'username': user_details.get('login', ''),
                        'third_name': user_details.get('patronymic', ''),
                        'birth_date': user_details.get('birth_date', ''),
                        'phone_number': user_details.get('phone', ''),
                        'image': user_details.get('picture', ''),
                        # Boshqa ma'lumotlar
                    }
                )
            return Response(full_info, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'status': False,
                    'error': 'Failed to obtain access token'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login')  # Foydalanuvchi avtorizatsiyadan chiqqandan so'ng o'tkaziladigan URL
