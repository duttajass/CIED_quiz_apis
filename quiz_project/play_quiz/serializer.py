from rest_framework import serializers
from .models import Play

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ['id','user_name','score','quiz']
