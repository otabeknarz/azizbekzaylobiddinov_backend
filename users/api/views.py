from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
from users.serializers import UserSerializer


@api_view(['GET'])
def get_user(request, id):
    user = User.objects.filter(id=id).first()
    if not user:
        return Response({"error": "User not found"}, status=404)

    return Response(UserSerializer(user).data, status=200)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_users_id(request):
    users = [user.id for user in User.objects.all()]
    return Response(users, status=200)


@api_view(['POST'])
def add_user(request):
    id = request.data.get('id')
    username = request.data.get('username')

    if not username:
        request.data['username'] = id

    user = User.objects.filter(id=id).first() if id else User.objects.filter(username=username.lower()).first()
    if user:
        return Response({"error": "User already exists", "data": UserSerializer(user).data}, status=400)

    request.data["username"] = request.data.get("username").lower()

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def update_or_add_user(request):
    id = request.data.get('id')
    username = request.data.get('username')

    if not id:
        return Response({"error": "Id is required"}, status=400)

    if not username:
        request.data['username'] = id
    else:
        request.data["username"] = request.data.get("username").lower()

    user = User.objects.filter(id=id).first() if id else User.objects.filter(username=username.lower()).first()
    if user:
        user.username = request.data.get("username")
        user.name = request.data.get('name', user.name)
        user.phone_number = request.data.get('phone_number', user.phone_number)
        user.save()
        return Response(UserSerializer(user).data, status=200)

    user = User.objects.create_user(**request.data)
    return Response(UserSerializer(user).data, status=201)
