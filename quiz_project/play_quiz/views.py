from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Play
from .serializer import PlaySerializer

from quiz_questions.models import QuestionAnswers

import json

# Create your views here.
@api_view(['GET','POST'])
def get_or_add_play(request):
    try:
        if request.method == 'GET':
            obj = Play.objects.all()
            serializer = PlaySerializer(obj, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            data = {
                'user_name': request.POST.get('user_name'),
                'quiz': request.POST.get('quiz')
            }
            serializer = PlaySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Quiz.DoesNotExist as e:
        return Response({"message":"Data doesn't exists."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_play_details(request,pid):
    try:
        if request.method == 'GET':
            obj = Play.objects.get(id=pid)
            serializer = PlaySerializer(obj)
            return Response(serializer.data)
        
    except Play.DoesNotExist as e:
        return Response({"message":"Data doesn't exists."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def submit_quiz(request,pid):
    try:
        if request.method == 'POST': 
            score = 0
            for item in request.data['quiz_questions']:
                qid = item['que_id']
                ans = item['answer']

                que_obj = QuestionAnswers.objects.get(id=qid)
                if ans.lower() == que_obj.right_answer.lower():
                    score += que_obj.marks
            
            if score > 0:
                obj = Play.objects.get(id=pid)
                print(obj)
                data = {'user_name':obj.user_name, 'score': score, 'quiz': obj.quiz.id}
                serializer = PlaySerializer(obj, data=data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Play.DoesNotExist as e:
        return Response({"message":"Data doesn't exists."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


