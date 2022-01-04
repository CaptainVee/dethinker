from django.urls import path
# from questions.api.views import ViewQuestions
from question.views import QuestionCreateView, QuestionListView, QuestionDetailView

urlpatterns = [
    path('question/new/', QuestionCreateView, name="new_question"),
    path('', QuestionListView.as_view(), name='question-home'),
    path('question/<int:pk>/', QuestionDetailView, name='question-detail'),

]

