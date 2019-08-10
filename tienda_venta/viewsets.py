from rest_framework import viewsets
from .serializer import Cliente2Serializer, LoginSerializer, OfertaSerializer, JoinFalso, JoinFalso2
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2,PseudoJoin

from .models import Oferta




class ClienteViewSets(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    queryset.delete()
    serializer_class = Cliente2Serializer

class ClienteLogin(viewsets.ModelViewSet):
    
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer
    



class OfertaViewSets(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()
    serializer_class = OfertaSerializer


'''Join entre Modelo cliente oferta y Productos'''
class viewjoin(viewsets.ModelViewSet):

    queryset = PseudoJoin.objects.all()
    serializer_class = JoinFalso

class VistaPrueba(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()
    serializer_class = JoinFalso2

class VistaPrueba2(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()[4:]
    serializer_class = JoinFalso2
