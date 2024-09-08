from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=128)
    user_type = serializers.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')])

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
