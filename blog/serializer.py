# coding: utf-8
# シリアライザ：データのにゅしゅつりょくを扱い、モデルへの橋渡しを行うクラス

from rest_framework import serializers

from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):

    # authorのserializerを上書き
    author = UserSerializer()
    
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')
