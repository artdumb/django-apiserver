from .models import Post, Review
from rest_framework import serializers
# 모델의 필드에 맞게 시리얼라이저클래스 생성


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
