from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'appointment/main.html')
def bookAppointmentView(request):
    return render(request, 'appointment/book-appointment.html')
def doctorVisitView(request):
    return render(request, 'appointment/doctor-visit.html')
