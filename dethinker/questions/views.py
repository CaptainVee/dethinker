# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from questions.serializers import *
# from questions.models import *
# from rest_framework import status



# class ViewQuestions(APIView):
#     def get(self, request, *args, **kwargs):
#         questions = Questions.objects.all()
#         serializer = QuestionSerializers(questions, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = QuestionSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
