from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'mail/main.html.html')
def emailCompose(request):
    return render(request, 'mail/email-compose.html')
