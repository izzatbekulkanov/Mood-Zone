# middleware.py

from django.utils import timezone
from django.contrib.auth import logout


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Foydalanuvchi kirish vaqtini olish
        last_activity = request.session.get('last_activity')

        if last_activity is not None:
            # Foydalanuvchi faol emasligini tekshirish
            if timezone.now() - last_activity > timezone.timedelta(seconds=30):
                logout(request)  # Avtomatik ravishda logout qilish

        # So'nggi faollik vaqtni yangilash
        request.session['last_activity'] = timezone.now()

        return response
