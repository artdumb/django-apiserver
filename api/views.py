from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Review, Post
from .serializer import ReviewSerializer, PostSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http.response import HttpResponse
from django.views.decorators    .csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class reviewAPI(APIView):
    # 댓글리스트
    def get(self, request, p_id):
        comments = get_list_or_404(Review, post_id=p_id)
        serializer = ReviewSerializer(comments, many=True)
        return Response(serializer.data)
    # 댓글쓰기

    def post(self, request, p_id):
        data = json.loads(request.body)
        post_id = p_id
        commentt = data.get('comment', None)

        # KEY_ERROR check
        if not (post_id and commentt):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        # valid post check
        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({'message': 'INVALID_POST'}, status=400)

        Review.objects.create(
            post=Post.objects.get(id=post_id),
            comment=commentt
        )

        return JsonResponse({'message': 'SUCCESS'}, status=200)


# 리스트 조회 (get) api
@api_view(['GET'])
def listpostAPI(request):
    modelDB = Post.objects.all()
    # 다수의 데이터를 받고자 할때(many=true)
    serializers = PostSerializer(modelDB, many=True)
    return Response(serializers.data)


# 개별 게시물 조회, 게시물 추가 api
@method_decorator(csrf_exempt, name='dispatch')
class postAPI(APIView):
    def get(self, request, id):
        obj = get_object_or_404(Post, pk=id)
        serializers = PostSerializer(obj)
        return Response(serializers.data)

    def post(self, request):
        data = json.loads(request.body)
        contentt = data.get('content', None)
        titlee = data.get('title', None)
        # KEY_ERROR check
        if not (contentt):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        Post.objects.create(
            content=contentt,
            title=titlee
        )

        return JsonResponse({'message': 'SUCCESS'}, status=200)

# 리뷰api
