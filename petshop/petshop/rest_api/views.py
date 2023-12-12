from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from reserva.models import reserva
from rest_api.serializers import agendamentomodelserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly




class agendamentoviewset(ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = agendamentomodelserializers
    permission_classes = [IsAuthenticatedOrReadOnly]



@api_view(['POST','GET'])
def hello_word(request):
    consulta = reserva.objects.all()
    serializer = agendamentomodelserializers(instance=consulta,many = True)
    return Response(serializer.data)



    