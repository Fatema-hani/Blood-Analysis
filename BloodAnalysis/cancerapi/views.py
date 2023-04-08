from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserData
from .serializers import UserSerilaizers
import joblib

 

loaded_model=joblib.load(open(r"cancerapi\bloodmodel", 'rb'))

class userlist(APIView):
    def get(self,request):
        users=UserData.objects.all()
        serializer=UserSerilaizers(users,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        age=int(self.request.data['age'])
        bmi=float(self.request.data['bmi'])
        glucouse=float(self.request.data['glucouse'])
        insuline=float(self.request.data['insuline'])
        homa=float(self.request.data['homa'])
        leptin=float(self.request.data['leptin'])
        adiponcetin=float(self.request.data['adiponcetin'])
        resistiin=float(self.request.data['resistiin'])
        mcp=float(self.request.data['mcp'])
        clf=loaded_model.predict([[age,bmi,glucouse,insuline,homa,leptin,adiponcetin,resistiin,mcp]])
        for i in range(1):
            if(clf[i]==1):
                self.request.data['classification']="No Cancer" 
            elif(clf[i]==2):
                self.request.data['classification']="Cancer" 
        serializer=UserSerilaizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data,status=404)