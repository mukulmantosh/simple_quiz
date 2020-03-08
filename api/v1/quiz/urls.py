from django.urls import path
from . import views

urlpatterns = [
    path('listing', views.QuizListingAPI.as_view()),
    path('questions', views.QuestionListingAPI.as_view()),

]
