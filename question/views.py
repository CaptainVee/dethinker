from django.contrib.auth.decorators import login_required
from question.forms import QuestionCreateForm, AnswerForm
from django.shortcuts import render, redirect, get_object_or_404
from question.models import Question, Answer
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




@login_required
def QuestionCreateView(request, *args, **kwargs):
    if request.method == 'POST':
        form = QuestionCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Question.objects.create(
                author=request.user,
                body=form.cleaned_data['body'],
                title = form.cleaned_data['title']
                )
            messages.info(request, "Your Question has been successfully created, Thank you")
            return redirect('home')
    else:
        form = QuestionCreateForm()
    context = {
        'form': form,
        }
    return render(request, 'question/question_form.html', context)


class QuestionListView(ListView):
    model = Question
    template_name = 'question/homes.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 5


def QuestionDetailView(request, pk, *args, **kwargs):
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AnswerForm(request.POST)
            form.instance.author = request.user
            form.instance.question = question
            if form.is_valid():
                form.save()
                return redirect('question-detail', pk=pk)
        else:
            return redirect('login')
    else:
        form = AnswerForm()

    context = {
                'answer':answers,
                'form': form,
                'question': question,
                }
    return render(request, "question/question_detail.html", context)












