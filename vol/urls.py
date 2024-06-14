from django.urls import path
from . import views 

urlpatterns = [
    path('vol/',views.vol,name = "vol"),
    path('getAns/',views.getAnswer,name = 'getAns'),
    path('answer/<str:pk>',views.answerChecker,name= "answerChecker"),
]

