from django.urls import path
from questions.api.views import ViewQuestions

urlpatterns = [
    path('', ViewQuestions.as_view()),
]

