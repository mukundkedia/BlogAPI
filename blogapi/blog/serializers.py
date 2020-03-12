from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','data','posted','updated',)
        model = models.Blog