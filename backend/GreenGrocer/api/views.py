from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import SigninSerializer, SignupSerializer
from .auth import signups, signins


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        return signups(serializer)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        return signins(serializer)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


