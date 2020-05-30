from rest_framework import serializers
from .models import users

class usersserializers(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=['USER_NAME','PASSWORD','USERTYPE']#or to get all fields do:fields='__all__'
                                                

#serializers.ModelSerializer: this creates the serializer for a model class