from rest_framework.decorators import api_view 
from rest_framework.response import Response  
from rest_framework import status 
from .models import CyptographyTool
from .serializer import CyptographyToolSerializer 
@api_view(['GET'])
def get_user(request):
    all_attampts=CyptographyTool.objects.all()
    serializer = CyptographyToolSerializer(all_attampts, many=True)
    return Response(CyptographyToolSerializer(all_attampts, many=True).data, status=status.HTTP_200_OK)
@api_view(['POST'])
def post_type_plain(reqest):
    if reqest.method == 'POST':
        print(reqest.data)
        if(reqest.data['type'] == 'Caesar Cipher'):
            plain = reqest.data['Plaintext']
            key = reqest.data['key']
            ciphertext = ""
            for ch in plain:
                if ch.isalpha():
                    ciphertext += chr((ord(ch)+key)%91) if ch.isupper() else chr((ord(ch)+key)%123)
                else:
                    ciphertext += ch
        savwm = {
            'type' :  reqest.data['type'],
                 'Plaintext': plain,
               'key': key,
             'Ciphertext': ciphertext
        }
        
        serializer = CyptographyToolSerializer(data=savwm)
       
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message":"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    enu