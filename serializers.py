from rest_framework import serializers
from .models import UserInput


class UserInputSerializer(serializers.ModelSerializer):
    Filiere = serializers.CharField()
    MatierePref = serializers.CharField()

    class Meta:
        model = UserInput
        fields = ('Filiere', 'MatierePref')

    def create(self, validated_data):
        return UserInput.objects.create(**validated_data)