from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.serializers import UserSerializer


@api_view(['GET'])
def getData(request):
    User = User.object.all()
    serializer = UserSerializer(User, many=True)
    return Response(serializer.data)

