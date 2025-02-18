from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from authentication.permissions import IsAuthenticatedCustom
from .serializers import WeblinkSerializer
from .services.weblink import WebLinkService

@api_view(['POST'])
@permission_classes([IsAuthenticatedCustom])
def create_weblink(request):
    serializer = WeblinkSerializer(data=request.data)
    if not serializer.is_valid():
        raise ValidationError('유효성 검사에 실패했습니다. 입력값을 확인해주세요.')

    try:
        WebLinkService.create_weblink(serializer.validated_data, request.user)
        return Response({'message': '웹링크가 성공적으로 추가되었습니다.'}, status.HTTP_201_CREATED)
    except Exception as e: 
        raise e

@api_view(['POST'])
@permission_classes([IsAuthenticatedCustom])
def update_weblink(request):
    serializer = WeblinkSerializer(data=request.data)
    if not serializer.is_valid():
        raise ValidationError('유효성 검사에 실패했습니다. 입력값을 확인해주세요.')

    try:
        WebLinkService.create_weblink(serializer.validated_data, request.user)
        return Response({'message': '웹링크가 성공적으로 추가되었습니다.'}, status.HTTP_201_CREATED)
    except Exception as e: 
        raise e
