from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework import serializers

# Create your views here.
class ItemSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.CharField())



@api_view(['POST'])
def bfhl(request):
    if request.method == 'POST':
        items = ItemSerializer(data=request.data)
        if items.is_valid():
            data = items.data['data']
            numbers = []
            dataresp = {}
            dataresp['is_success'] = "true"
            dataresp['user_id'] = "john_doe_17091999"
            dataresp['email'] = "john@xyz.com"
            dataresp['roll_number'] = "ABCD123"
            dataresp['numbers'] = []
            dataresp['alphabets'] = []
            for i in data:
                try:
                    if int(i):
                        dataresp['numbers'].append(i)
                except ValueError:
                     dataresp['alphabets'].append(i)
            return Response(dataresp,status=200)