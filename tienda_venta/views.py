from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import LoginSerializer, JoinFalso2, JoinFalso,JoinFalso3
from .models import Cliente2, PseudoJoin, Join2
from tienda_almacen.models import Producto
from tienda_almacen.serializer import GuardaProducto
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.shortcuts import get_list_or_404, get_object_or_404

'''
@api_view(['GET'])
def snippet_list(self,request):
    """
Listar o Crear   """
    if request.method == 'GET':
        variable = request.data.get('contra','false')
        variable1 = request.data.get('cedula','false')
        send = {"text":"No"}
        snippets = Cliente2.objects.filter(contra="123", cedula="123")
        if not snippets:
            return Response(send, status=status.HTTP_204_NO_CONTENT)
        else:
            serializer_context = {
            'request': request,
                 }       
            serializer = LoginSerializer(instance=snippets,many=True)
            return Response(request.query_params.get("cedula"), status=status.HTTP_200_OK)
    

    else:
        return Response("error")'''
   

class ClienteLogin(APIView):

    def get(self,request,contra,cedula):

        contraseña = str(contra)
        ids = str(cedula)
        parser_classes = [JSONParser]
        v = request.data
        v1 = request.data
        snippets = Cliente2.objects.filter(contra=contra, cedula=cedula)
        
        if not snippets:
            return Response("No")
        else:
            serializer = LoginSerializer(snippets, many=True)
            return Response(serializer.data)
       

class GetTodo(APIView):

    def get(self,request,categoria, ):

        parser_classes = [JSONParser]
       
        snippets = PseudoJoin.objects.filter(productos__categoria_id__id_categoria=categoria)

        
        if not snippets:
            return Response("No")
        else:
            serializer = JoinFalso2(snippets, many=True, context={'request': request})
            return Response(serializer.data)


class GetProducto(APIView):
    def get(self, request, clave):

        parser_classes = [JSONParser]

        products = PseudoJoin.objects.filter(productos__nombre_producto__iexact=clave)

        if not products:
            return Response("No")
        else:
            serializer = JoinFalso2(products, many=True, context={'request':request})
            return Response(serializer.data)


class GetRopa(APIView):

    def get(self,request):

        parser_classes = [JSONParser]
       
        snippets = PseudoJoin.objects.filter(productos__categoria_id__nombre_categoria="Ropa")

        
        if not snippets:
            return Response("No")
        else:
            serializer = JoinFalso2(snippets, many=True, context={'request': request})
            return Response(serializer.data)

class GetVideoJuegos(APIView):

    def get(self,request):

        parser_classes = [JSONParser]
       
        snippets = PseudoJoin.objects.filter(productos__categoria_id__nombre_categoria="VideoJuegos")

        
        if not snippets:
            return Response("No")
        else:
            serializer = JoinFalso2(snippets, many=True, context={'request': request})
            return Response(serializer.data)

class GetPhone(APIView):

    def get(self,request):

        parser_classes = [JSONParser]
       
        snippets = PseudoJoin.objects.filter(productos__categoria_id__nombre_categoria="Celulares")

        
        if not snippets:
            return Response("No")
        else:
            serializer = JoinFalso2(snippets, many=True, context={'request': request})
            return Response(serializer.data)

class GetTeles(APIView):

    def get(self,request):

        parser_classes = [JSONParser]
       
        snippets = PseudoJoin.objects.filter(productos__categoria_id__nombre_categoria="Televisores")

        
        if not snippets:
            return Response("No")
        else:
            serializer = JoinFalso2(snippets, many=True, context={'request': request})
            return Response(serializer.data)

class MandaProductosComprados(APIView):

    def get(self,request,cedula):

        snippets = Join2.objects.filter(pedido1__cliente__cedula=cedula)

        if not snippets:
            return Response("No")
        else:
            serializer = JoinFalso3(snippets, many=True, context={'request':request})
            return Response(serializer.data)

'''Retorna productos que estan en venta de determinado cliente'''
class MandaProductosenVenta(APIView):

    def get(self,request,cedula):

        snippets = PseudoJoin.objects.filter(vendedor__cedula=cedula)

        if not snippets:
            return Response("no")
        else:
            serializer = JoinFalso2(snippets, many=True, context={'request':request})
            return Response(serializer.data)

class MandaProductosenVendidos(APIView):

    def get(self,request,cedula):

        snippets = Join2.objects.filter(vendedor1__cedula=cedula)

        if not snippets:
            return Response("no")
        else:
            serializer = JoinFalso3(snippets, many=True, context={'request':request})
            return Response(serializer.data)



class GetStock(APIView):
    
    def get(self,request,id_producto):
        stock = Producto.objects.get(pk=id_producto)
        serializer = GuardaProducto(stock, context={'request':request})
        return Response(serializer.data)

'''Edita cantidad de ṕroductos'''
class UpdateProductos(APIView):

    def patch(self, request,pk,cantidad_producto):

        model = get_object_or_404(Producto,pk=pk)
        data = {'cantidad_producto':model.cantidad_producto-int(cantidad_producto)}

        serializer = GuardaProducto(model, data=data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response("error")


class RestauraProductos(APIView):
    def patch(self,request,pk,cantidad_producto):
        model = get_object_or_404(Producto,pk=pk)
        data = {'cantidad_producto':model.cantidad_producto+int(cantidad_producto)}

        serializer = GuardaProducto(model, data=data, partial=True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")

class AlteraPseudoJoi(APIView):
    def patch(self,request,productos_id,pedidos):
        model = get_object_or_404(PseudoJoin, productos_id=productos_id)
        data = {'pedidos':model.pedidos}

        serializer = JoinFalso(model, data=data, partial= True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")



class Descuentos(APIView):
    def patch(self,request,id_producto,precio_unidad):
        model = get_object_or_404(Producto,id_producto=id_producto)
        data = {'precio_unidad':model.precio_unidad-(int(precio_unidad))}

        serializer = GuardaProducto(model, data=data, partial=True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")