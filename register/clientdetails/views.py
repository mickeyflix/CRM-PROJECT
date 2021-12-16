from django.http import response
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view

# Create your views here.
from .serializers import ClientSerializer
from .models import client
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
class TestView(APIView):
    def post(self,request,*args,**kwargs):
        serial=ClientSerializer(data=request.data)
        
        
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        
    def get(self,request,*args,**kwargs):
        cl=client.objects.all()
        serial=ClientSerializer(cl,many=True)
        return Response(serial.data)
@api_view(('GET',))
def claim_here(request,client_id):
    client_obj=client.objects.get(id=client_id)
    client_obj.claimedby=request.user
    client_obj.save()
    return redirect('/admin/clientdetails/client')