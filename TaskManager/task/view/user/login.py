from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from task.serializer.user.login import *
from knox.auth import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from datetime import datetime
from task.bulkcreation import checkbulkcreations

# to get user logic detail
def doAdminLogin(user, request):
    user_data = User.objects.get(user_name=user)
    token = AuthToken.objects.create(user=user_data)[1]
    data={  
        'user_id':user_data.id,
        'is_super_admin':user_data.is_super_admin,
        'user_name':user_data.user_name,
        "message": 'User Suceessfully loged',
        "Token": token,
    }
    return data




class LoginAPI(APIView):

    def post(self, request):   
        try:
            checkbulkcreations()
            serializer_class = LoginSerializer(data=request.data)
            if serializer_class.is_valid():
                checkbulkcreations()
                user = serializer_class.validated_data['user_name']
                data = doAdminLogin(user, request)
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
        
class RegisterAPI(APIView):

    def post(self, request):   
        try:
            serializer_class = registerSerializer(data=request.data)
            if serializer_class.is_valid():
                print('save')
                query = serializer_class.save()
                print('query')
                userid = query.id
                print(userid,'userid')
                userquery = User.objects.get(id=userid)
                
                print(userquery,'userquery')
                data = doAdminLogin(userquery, request)
                return Response(data,status=status.HTTP_200_OK)
            else:
                print(serializer_class.errors,'serializer_class.errors')
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)



        