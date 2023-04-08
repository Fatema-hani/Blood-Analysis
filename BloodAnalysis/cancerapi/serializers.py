from dataclasses import field
from rest_framework import serializers

from .models import UserData


class UserSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = UserData
        #fields = ('first_name','Last_name')
        fields = '__all__'
        