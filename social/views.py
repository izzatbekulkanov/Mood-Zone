from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'social-app/dashboard/main.html')
def accountSetting(request):
    return render(request, 'social-app/account-setting.html')
def birthday(request):
    return render(request, 'social-app/birthday.html')
def eventDetail(request):
    return render(request, 'social-app/event-detail.html')
def eventList(request):
    return render(request, 'social-app/event-list.html')
def friendRequest(request):
    return render(request, 'social-app/friend-request.html')
def friendList(request):
    return render(request, 'social-app/friend-list.html')
def friendProfile(request):
    return render(request, 'social-app/friend-profile.html')
def group(request):
    return render(request, 'social-app/group.html')
def groupDetail(request):
    return render(request, 'social-app/group-detail.html')
def newsFeed(request):
    return render(request, 'social-app/newsfeed.html')
def notification(request):
    return render(request, 'social-app/notification.html')
def profileBadges(request):
    return render(request, 'social-app/profile-badges.html')
def profileImages(request):
    return render(request, 'social-app/profile-images.html')
def profileVideo(request):
    return render(request, 'social-app/profile-video.html')
def socialProfile(request):
    return render(request, 'social-app/social-profile.html')
