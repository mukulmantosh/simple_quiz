from django.urls import path
from . import views

urlpatterns = [
    path('listing', views.QuizListingAPI.as_view()),
    path('questions', views.QuestionListingAPI.as_view()),
    path('initiate', views.InitiateTestAPI.as_view())

]
