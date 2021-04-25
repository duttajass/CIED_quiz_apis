from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Quiz, QuestionAnswers
from .serializer import QuizSerializer, QuestionAnswersSerializer

# Create your views here.

@api_view(['GET','POST'])
def get_or_add_quiz(request):
    try:
        if request.method == 'GET':
            obj = Quiz.objects.all()
            serializer = QuizSerializer(obj, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            data = {'quiz_name': request.POST.get('quiz_name')}

            serializer = QuizSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Quiz.DoesNotExist as e:
        return Response({"message":"Data doesn't exists."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET','POST'])
def get_or_add_questions_for_quiz(request,qid):
    try:
        if request.method == 'GET':
            obj = QuestionAnswers.objects.filter(for_quiz=qid)
            serializer = QuestionAnswersSerializer(obj, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            data = {
                'question': request.POST.get('question'),
                'choice_1': request.POST.get('choice_1'),
                'choice_2': request.POST.get('choice_2'),
                'choice_3': request.POST.get('choice_3'),
                'right_answer': request.POST.get('right_answer'),
                'marks': request.POST.get('marks'),
                'for_quiz': qid
            }

            serializer = QuestionAnswersSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except QuestionAnswers.DoesNotExist as e:
        return Response({"message":"Data doesn't exists."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
