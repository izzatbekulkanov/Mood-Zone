from django.shortcuts import render

# Create your views here.

def exam_dashboard(request):
    return render(request, 'app/exam/dashboard.html')