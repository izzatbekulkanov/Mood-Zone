from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'file-manager/dashboard.html')
def allFiles(request):
    return render(request, 'file-manager/all-files.html')
def documentFolder(request):
    return render(request, 'file-manager/document-folder.html')
def imageFolder(request):
    return render(request, 'file-manager/image-folder.html')
def trash(request):
    return render(request, 'file-manager/trash.html')
def videoFolder(request):
    return render(request, 'file-manager/video-folder.html')
