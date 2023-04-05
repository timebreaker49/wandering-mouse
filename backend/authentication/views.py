from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class HomeView(APIView):
    
    # permission_classes = (IsAuthenticated, ) -- can use to block requests
    def get(self, request):
        content = {
            'message': 'Welcome to the JWT Authentication page with Django + React!'
        }
        
        return Response(content)        

class LogoutView(APIView):
    
    # permission_classes = (IsAuthenticated, )
    
    def post(self, request):
        print(request.data)
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)