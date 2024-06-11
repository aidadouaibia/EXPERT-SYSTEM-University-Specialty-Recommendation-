from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .aima_logic import get_recommendation, calculate_method,kb, memory, agenda

from .serializers import UserInputSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse

class UserInputView(APIView):
    def post(self, request):
        # Générer un jeton CSRF
        csrf_token = get_token(request)
        
        # Votre logique de traitement de la requête
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            Filiere = serializer.validated_data.get('Filiere')
            MatierePref = serializer.validated_data.get('MatierePref')

            # Obtenir la recommandation et la méthode
            recommendation = get_recommendation(kb, memory)
            method = calculate_method(kb, agenda, memory)

            # Ajouter la recommandation et la méthode à la réponse JSON
            data = {
                'recommendation': recommendation,
                'method': method
            }
            return JsonResponse(data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
