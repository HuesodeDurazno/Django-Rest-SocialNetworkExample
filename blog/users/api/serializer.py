from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','password']
    
    def create(self, validate_data):
        password = validate_data.pop('password',None)
        instance = self.Meta.model(**validate_data)
        
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']