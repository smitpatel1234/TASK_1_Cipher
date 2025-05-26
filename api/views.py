from rest_framework.decorators import api_view 
from rest_framework.response import Response  
from rest_framework import status 
import cryptographytool 
from .models import CyptographyTool
from .serializer import CyptographyToolSerializer 
@api_view(['GET'])
def get_user(request):
    return Response(CyptographyToolSerializer({"type":"cizer cypire" , "Plaintext":"helloworld","Ciphertext":"cizer cypire"}).data)
@api_view(['POST'])
def post_type_plain(reqest):
    if reqest.method == 'POST':
        serializer = CyptographyToolSerializer(data=reqest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message":"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    