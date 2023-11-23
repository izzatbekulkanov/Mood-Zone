from django.shortcuts import render

# Create your views here.

def landingPageView(request):
    return render(request, 'landing-pages/index.html')
