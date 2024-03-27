from django.db.models import Count
from django.db.models.functions import Lower
from django.http import JsonResponse

from core import settings
from library.models import Author


def get_authors(request):

    authors = Author.objects.annotate(book_count=Count('books')).order_by(Lower('name'))
    data = list(authors.values('id', 'name', 'phone_number', 'image', 'email', 'author_code', 'is_active', 'book_count'))  # Ma'lumotlarni to'plash
    for item in data:
        if item['image']:
            item['image_url'] = settings.MEDIA_URL + item['image']  # Rasm URL sini qo'shish
    return JsonResponse(data, safe=False)