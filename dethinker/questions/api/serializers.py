from rest_framework import serializers
from questions.models import *

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'username', 'school'
        )

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = (
            'course_code', 'course_title', 'session'
        )

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = (
            'answer'
        )

class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'school_name', 'department', 'faculty'
        )