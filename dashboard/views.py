from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
@login_required
def index(request):
    nameLocation  = 'namangan'
    parameters = {'key': 'gjlovpwc309k5co71et88v63xsxqft89pskcamuu',
                  'place_id': nameLocation}

    url = "https://www.meteosource.com/api/v1/free/point"

    # data = requests.get(url, parameters).json()

    return render(request, 'main/index.html')

# @login_required
# def weather(request):
#     nameLocation = 'namangan'
#     parameters = {'key': 'gjlovpwc309k5co71et88v63xsxqft89pskcamuu',
#                   'place_id': nameLocation}
#
#     url = "https://www.meteosource.com/api/v1/free/point"
#
#     data = requests.get(url, parameters).json()
#
#     temperature = data['current']['temperature']
#     response_data = {'temperature': temperature}
#
#     return JsonResponse(response_data)