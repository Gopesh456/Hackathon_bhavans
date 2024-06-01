from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage),
    path('question/<str:pk>/',views.questions, name='question'),
    path('getquestions/',views.getques,name = "getquestions"),
    path('getmsg/',views.getmsg,name = "getmsg"),
    path('sendmsg/',views.sendmsg,name = "sendmsg"),
    path('questions/',views.overview,name = "questions"),
    path('getpoints/',views.getPoints,name = "getpoints"),
    path('getresults/',views.getResults,name = "getresults"),
    path('post_correct/',views.getCorrect,name = "post_correct"), # type: ignore
    path('leaderboard/',views.leaderboard,name = "learderboard"), # type: ignore
]