from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from .serializers import DrinkSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def drink(request):
    if request.method == 'GET':
    # get all the drink
      drinks =Drink.objects.all()
    #serializer 
      serializer=DrinkSerializer(drinks,many=True)
    #return json 
      return JsonResponse({'drink': serializer.data})
    if request.method == 'POST':
       serializer = DrinkSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)





@api_view(['GET', 'PUT','DELETE'])
def drinklist(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize the drink
        serializer = DrinkSerializer(drink)
        # Return JSON
        return JsonResponse({'drink': serializer.data})

    elif request.method == 'PUT':
       
        serializer = DrinkSerializer(drink, data=request.data)
        
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    elif request.method == 'DELETE':
        drink.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)















# myapp/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileUpload
from .serializers import FileUploadSerializer

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_files(request):
    files = FileUpload.objects.all()
    serializer = FileUploadSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
