from django.urls import path
from social.views import (
    dashboard,
    accountSetting,
    birthday,
    eventList,
    eventDetail,
    friendList,
    friendProfile,
    friendRequest,
    groupDetail,
    group,
    newsFeed,
    notification,
    profileVideo,
    profileBadges,
    profileImages,
    socialProfile)

app_name = 'social'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('accountSetting/', accountSetting, name='accountSetting'),
    path('birthday/', birthday, name='birthday'),
    path('eventList/', eventList, name='eventList'),
    path('eventDetail/', eventDetail, name='eventDetail'),
    path('friendList/', friendList, name='friendList'),
    path('friendProfile/', friendProfile, name='friendProfile'),
    path('friendRequest/', friendRequest, name='friendRequest'),
    path('groupDetail/', groupDetail, name='groupDetail'),
    path('group/', group, name='group'),
    path('newsFeed/', newsFeed, name='newsFeed'),
    path('notification/', notification, name='notification'),
    path('profileVideo/', profileVideo, name='profileVideo'),
    path('profileBadges/', profileBadges, name='profileBadges'),
    path('profileImages/', profileImages, name='profileImages'),
    path('socialProfile/', socialProfile, name='socialProfile'),
]
