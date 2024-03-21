from django.shortcuts import render

# Create your views here.

def post_dashboard(request):
    return render(request, 'app/post/layout/index.html')