from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import  Session,Search,Product,Mouse_Click,Cart,Add_To_Cart,Delete_From_The_Cart,Checkout
from drf_writable_nested.serializers import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SessionSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class SearchSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Search
        fields = ['Session','keywords']

class ProductSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Product
        fields = '__all__'

class Mouse_ClickSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Mouse_Click
        fields = '__all__'
              
class CartSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

class Add_To_CartSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Add_To_Cart
        fields = '__all__'
              
class Delete_From_The_CartSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Delete_From_The_Cart
        fields = '__all__'

class CheckoutSerializer(WritableNestedModelSerializer):
    Session = SessionSerializer()
    class Meta:
        model = Checkout
        fields = ['Session','Title','Price','Qty','Soldby','ShipSpeed','Address']

     
   
              