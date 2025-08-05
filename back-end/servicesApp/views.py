from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from api.serializers import ServiceSerializer
from api.models import Servico
from django.shortcuts import render
from django.db.models import Q
modelo_usuario = get_user_model()
 
@api_view(['GET'])
def getAllServices(request):
    services = Servico.objects.all()

    servicesJson = ServiceSerializer(services, many=True)

    if services:
        return Response({"Usuarios":servicesJson.data}, status=status.HTTP_200_OK)
    else:
        return Response({"Usuarios":"Nenhum serviço cadastrado"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getServiceByQuery(request):
    query = request.query_params.get('q')

    services = Servico.objects.all()

    if query:
        services = services.filter(
            Q(titulo__icontains=query) | Q(descricao__icontains=query)
        )

    servicesJson = ServiceSerializer(services, many=True)

    return Response(servicesJson.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def addService(request):
    if request.method == 'POST':        
        service = ServiceSerializer(data=request.data)

        if service.is_valid():
            service.save(usuario=request.user)


            #caso a página de cadastro de serviços e a de listar serviços fosse uma só
            # html_card = render(request, 'partials/cardForMyServicesPage.html', {'service':new_service}).content.decode('utf-8')

            return Response({'message':'Serviço cadastrado com sucesso!', 'success':True}, status=status.HTTP_201_CREATED)
        else:
            print(service.errors)
            return Response({'message':'Erro no cadastro!', 'errors':service.errors, 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': "Método não permitido! Só POST é possível.", 'success':False}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 