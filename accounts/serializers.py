from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from django.core import exceptions

class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, style={"input_type":"password"})
    password2 = serializers.CharField(write_only=True, style={"input_type":"password"})

    class Meta:
        model = User
        fields = ["email", "username", "password", "password2"]


    def validate(self,attrs):

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password":"Passwords do not matched"})
        
        try:
            validate_password(attrs["password"])

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password":list(e.messages)})

        return attrs

    def create(self,validate_data):
        validate_data.pop("password2")

        user = User.objects.create(**validate_data)
        user.set_password(validate_data["password"])

        user.save()

        return user



class UpdateUsernameSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username"]



class ChangePasswordSerializer(serializers.ModelSerializer):

    prev_password = serializers.CharField(write_only=True, style={"input_type":"password"})

    new_password1 = serializers.CharField(write_only=True, style={"input_type":"password"})
    new_password2 = serializers.CharField(write_only=True, style={"input_type":"password"})
    
    
    class Meta:
        model =User 
        fields = ["prev_password","new_password1","new_password2"]

    
    def validate(self,attrs):

        if not  self.context["request"].user.check_password(attrs["prev_password"]):
            raise serializers.ValidationError({"prev_password":"prev password not correct !"})

        if attrs["new_password1"] != attrs["new_password2"]:
            raise serializers.ValidationError({"password":"Passwords do not matched"})
        
        try:
            validate_password(attrs["new_password1"])

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password":list(e.messages)})
        
        
        return attrs


    def update(self, instance, validated_data):
        
        instance.set_password(validated_data["new_password1"])
        instance.save()
        
        return  instance



class UpdateUserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User 
        fields = ["first_name", "last_name"]














