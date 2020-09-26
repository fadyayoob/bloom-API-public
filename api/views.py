import json
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,SessionSerializer,GroupSerializer,SearchSerializer ,ProductSerializer,Mouse_ClickSerializer , CartSerializer ,Add_To_CartSerializer ,Delete_From_The_CartSerializer ,CheckoutSerializer
from rest_framework import generics
from .models import Session,Search,Product,Mouse_Click,Cart ,Add_To_Cart,Delete_From_The_Cart,Checkout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
# Create your views here.


@api_view(['POST'])
def users(request):
    all_users = User.objects.all()
    data = UserSerializer(all_users, many=True).data
    return Response({'data': data})



@api_view(['POST'])
def user(request,id):
    all_users = User.objects.get(id=id)
    data = UserSerializer(all_users).data
    return Response({'data': data})



class add_user(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Search(generics.ListCreateAPIView):
     queryset = Search.objects.all()
     serializer_class = SearchSerializer
     
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SearchSerializer(queryset, many=True)
        return Response(serializer.data)
class Product(generics.ListCreateAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class Mouse_Click(generics.ListCreateAPIView):
     queryset = Mouse_Click.objects.all()
     serializer_class = Mouse_ClickSerializer
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = Mouse_ClickSerializer(queryset, many=True)
        return Response(serializer.data)

class  Cart(generics.ListCreateAPIView):
     queryset = Cart.objects.all()
     serializer_class =  CartSerializer
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

class Add_To_Cart(generics.ListCreateAPIView):
     queryset = Add_To_Cart.objects.all()
     serializer_class = Add_To_CartSerializer
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = Add_To_CartSerializer(queryset, many=True)
        return Response(serializer.data)

class Delete_From_The_Cart(generics.ListCreateAPIView):
     queryset = Delete_From_The_Cart.objects.all()
     serializer_class = Delete_From_The_CartSerializer
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = Delete_From_The_CartSerializer(queryset, many=True)
        return Response(serializer.data)

class Checkout(generics.ListCreateAPIView):
     queryset = Checkout.objects.all()
     serializer_class = CheckoutSerializer
     def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CheckoutSerializer(queryset, many=True)
        return Response(serializer.data)
"""
class  Carte(generics.ListCreateAPIView):
        # Note the use of `get_queryset()` instead of `self.queryset`
    def carte(self, request, format=None):
        x = {"Session": { "Mac": "aaa", "Auth0_Token": "aaa" },"Request":[{"Name": "aaa", "Price": "aaaa", "Url": "aaaa" }]}
        y = json.loads(x) 
        return print(x)
"""
@api_view(['POST'])
@parser_classes([JSONParser])
def carte(request, format=None):
    Name = request.POST.get("Name")
    Price =request.POST.get("Price")
    Url = request.POST.get("Url")
    return Response({'received data': request.data})

@api_view(['POST'])
@parser_classes([JSONParser])
def checkoute(request, format=None):
    Name = request.POST.get("Title")
    Price =request.POST.get("Price")
    Qty = request.POST.get("Qty")
    soldby = request.POST.get("Soldby")
    ShipSpeed = request.POST.get("ShipSpeed")
    Address = request.POST.get("Address")
    return Response({'received data': request.data})
  