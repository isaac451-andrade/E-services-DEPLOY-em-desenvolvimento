from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from api.serializers import UsuarioSerializer
modelo_usuario = get_user_model()

@api_view(['GET'])
def getAllUsers(request):
    users = modelo_usuario.objects.all()

    usersJson = UsuarioSerializer(users, many=True)


    if users:
        return Response({"Usuarios":usersJson.data}, status=status.HTTP_200_OK)
    else:
        return Response({"Usuarios":"Nenhum usuário cadastrado"}, status=status.HTTP_400_BAD_REQUEST)
        





@api_view(['POST'])
def addUser(request):
    if request.method == 'POST':
        user = UsuarioSerializer(data=request.data)

        if user.is_valid():
            user.save()
            return Response({'message':'Usuário cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)

        else:
            print(user.errors)
            return Response({'message':'Erro no cadastro!', 'errors':user.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': "Método não permitido! Só POST é possível.", 'status':'error'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def getUserById(request, id):
    if request.method == 'GET':
        try:
            user = modelo_usuario.objects.get(id=id)

            userData = UsuarioSerializer(user)

            return Response(userData.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Usuário com este ID não existe!'}, status= status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def getUserByName(request, name):
    if request.method == 'GET':
        try:

            user = modelo_usuario.objects.get(username=name)
            userData = UsuarioSerializer(user)

            return Response(userData.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Usuário com este NOME não existe!'}, status= status.HTTP_404_NOT_FOUND)
        
@api_view(['DELETE'])
def deleteUserById(request, id):

    try:
        userToBeDeleted = modelo_usuario.objects.get(id=id)

        if not request.user.is_superuser and request.user.id !=id:
            print(f"user={request.user} || superuser= {request.user.is_superuser}")
            return Response({'message':'Você não tem permissão para acessar este usuário!'}, status=status.HTTP_403_FORBIDDEN)
        
        userToBeDeleted.delete()
        return Response({'message': "Usuário deletado com sucesso!"}, status=status.HTTP_200_OK)
    except:
         return Response({'message': 'Usuário com este ID não existe!'}, status= status.HTTP_404_NOT_FOUND)

    

    
    
