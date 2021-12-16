from django.db.models import fields
from rest_framework.serializers import Serializer,ModelSerializer
from .models import client

class ClientSerializer(ModelSerializer):
    class Meta:
        model=client
        fields=('name','email','courseinterest')
        
