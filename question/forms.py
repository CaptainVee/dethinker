from django import forms
from question.models import Question, Answer


# class AnnouncementUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Announcement
# 		fields = ['title', 'message', 'image']



class QuestionCreateForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [  
					'title',
					'body',
					]


class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['body',]