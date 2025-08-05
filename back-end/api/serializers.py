from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models import Servico
modelo_usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = modelo_usuario
        fields= ("id",'username', 'password', 'password2', 'email', 'address', 'contact', 'company_name')
        


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"passwordError":"As senhas não conferem!"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')

        user = modelo_usuario.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get('password'),
            email=validated_data.get('email', ''),
            address=validated_data.get('address', ''),
            contact=validated_data.get('contact', ''),
            company_name=validated_data.get('company_name', '')
        )
        return user
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = "__all__"