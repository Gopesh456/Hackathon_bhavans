from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage),
    path('question/<str:pk>/',views.questions, name='question'),
    path('getquestions/',views.getques,name = "getquestions"),
    path('questions/',views.overview,name = "questions"),
]