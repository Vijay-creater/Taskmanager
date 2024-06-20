from task.models import *
from django.contrib.auth.hashers import check_password
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField()
    password = serializers.CharField(
        label=("password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=125,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'user_name', 'password']


    def validate(self, data):
        user_name = data.get('user_name')
        Password = data.get('password')
        if user_name and Password:
            user = User.objects.filter(user_name = user_name).first()
            if user is None:
                raise serializers.ValidationError({'message':'Invaled User Name'})
            if not check_password(Password, user.password):
                raise serializers.ValidationError({'message':'Invaled Password'})
        else:
            raise serializers.ValidationError({'message':'Please Enter User Name and Password'})

        data['user'] = user
        return data
    
class registerSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField()
    class Meta:
        model = User
        fields = ['user_name','password','email','display_name']
    
    def validate_user_name(self, data):
        if User.objects.filter(user_name=data).exists():
            raise serializers.ValidationError('User Name is already exists')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user