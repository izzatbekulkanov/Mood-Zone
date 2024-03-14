from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout, get_user_model, login
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.settings import (
    CLIENT_SECRET,
    CLIENT_ID,
    REDIRECT_URI,
    RESOURCE_OWNER_URL,
    TOKEN_URL,
    AUTHORIZE_URL,
)
from .client import oAuth2Client


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

        # return redirect(authorization_url)
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
            old_date_str = user_details.get('birth_date', '')
            if old_date_str:
                # Convert the old date string to datetime object
                old_date = datetime.strptime(old_date_str, '%d-%m-%Y')

                # Convert datetime object to new string format 'YYYY-MM-DD'
                new_date_str = old_date.strftime('%Y-%m-%d')
            else:
                new_date_str = None

            # E-mail manzilini tekshirish va saqlash
            if email:
                first_name = user_details.get('firstname', '')
                second_name = user_details.get('surname', '')
                id_number = user_details.get('id', '')  # id bilan
                if id_number:
                    username = (first_name + '_' + second_name + str(id_number)).lower()
                else:
                    # Agar id mavjud emas bo'lsa, boshqa identifikatsiya xususiyatidan foydalaning
                    username = (first_name + '_' + second_name).lower()
                user, created = CustomUser.objects.get_or_create(
                    email=email,
                    defaults={
                        'full_name': user_details.get('name', ''),
                        'first_name': user_details.get('firstname', ''),
                        'second_name': user_details.get('surname', ''),
                        'username': username,
                        'third_name': user_details.get('patronymic', ''),
                        'birth_date': new_date_str,
                        'phone_number': user_details.get('phone', ''),
                        'token': access_token,
                        'image': user_details.get('picture', ''),
                        # Boshqa ma'lumotlar
                    }
                )
                oauth_login(request, email, user)  # Faydalanuvchini login qiling
            elif employee_id_number:
                # Tekshirish: employee_id_number ga teng foydalanuvchi mavjudmi?
                existing_user = CustomUser.objects.filter(employee_id_number=employee_id_number).first()
                if existing_user:
                    first_name = user_details.get('firstname', '')
                    second_name = user_details.get('surname', '')
                    id_number = user_details.get('id', '')  # id bilan
                    if id_number:
                        username = (first_name + '_' + second_name + str(id_number)).lower()
                    else:
                        # Agar id mavjud emas bo'lsa, boshqa identifikatsiya xususiyatidan foydalaning
                        username = (first_name + '_' + second_name).lower()
                    # Foydalanuvchi malumotlarini yangilash
                    existing_user.full_name = user_details.get('name', '')
                    existing_user.first_name = user_details.get('firstname', '')
                    existing_user.second_name = user_details.get('surname', '')
                    existing_user.username = username
                    existing_user.third_name = user_details.get('patronymic', '')
                    existing_user.birth_date = new_date_str
                    existing_user.phone_number = user_details.get('phone', '')
                    existing_user.token = access_token
                    existing_user.image = user_details.get('picture', '')
                    existing_user.save()
                    oauth_login(request, existing_user.email, existing_user)  # Faydalanuvchini login qiling
                else:
                    # Yangi foydalanuvchi yaratish
                    email = f"{employee_id_number}@namspi.uz"
                    user_type = user_details.get('type', '')
                    first_name = user_details.get('firstname', '')
                    second_name = user_details.get('surname', '')
                    id_number = user_details.get('id', '')  # id bilan
                    if id_number:
                        username = (first_name + '_' + second_name + str(id_number)).lower()
                    else:
                        # Agar id mavjud emas bo'lsa, boshqa identifikatsiya xususiyatidan foydalaning
                        username = (first_name + '_' + second_name).lower()

                    if user_type == 'employee':
                        user_type = '2'  # Hodim

                    user, created = CustomUser.objects.get_or_create(
                        email=email,
                        defaults={
                            'employee_id_number': employee_id_number,
                            'full_name': user_details.get('name', ''),
                            'first_name': user_details.get('firstname', ''),
                            'second_name': user_details.get('surname', ''),
                            'username': username,
                            'third_name': user_details.get('patronymic', ''),
                            'birth_date': new_date_str,
                            'phone_number': user_details.get('phone', ''),
                            'token': access_token,
                            'image': user_details.get('picture', ''),
                            'user_type': user_type,  # Foydalanuvchi tipini kiritish
                            # Boshqa ma'lumotlar
                        }
                    )
                    oauth_login(request, email, user)  # Faydalanuvchini login qiling

            # return Response(full_info, status=status.HTTP_200_OK)
            return redirect('index')
        else:
            return Response(
                {
                    'status': False,
                    'error': 'Failed to obtain access token'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


def oauth_login(request, email, user):
    # Faydalanuvchi obyektini olish
    # user = get_object_or_404(CustomUser, email=email)

    # Faydalanuvchini avtorizatsiya qilish
    user.backend = 'django.contrib.auth.backends.ModelBackend'  # Faydalanuvchi uchun kerakli backendni aniqlash
    login(request, user)


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login')  # Foydalanuvchi avtorizatsiyadan chiqqandan so'ng o'tkaziladigan URL
