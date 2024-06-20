from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from task.serializer.task.task import *
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):   
        try:
            searchTerm = request.query_params.get('searchTerm')
            selectedDate = request.query_params.get('selectedDate')
            taskStatus = request.query_params.get('taskStatus')
            commonqueryset = Task.objects.select_related('status')
            if searchTerm and searchTerm !='':
                commonqueryset = commonqueryset.filter(title__icontains=searchTerm)
            if selectedDate and selectedDate !='':
                commonqueryset =  commonqueryset.filter(due_date=selectedDate)
            if taskStatus and taskStatus !='':
                commonqueryset =  commonqueryset.filter(status=taskStatus)
            serializer_class = GetTankSerializer(commonqueryset,many=True)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):   
        try:
            id = request.query_params.get('id')
            queryset = Task.objects.get(id=id)
            serializer_class = GetTankUnitSerializer(queryset)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):   
        try:
            serializer_class = PostTankSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):   
        try:
            id = request.data.get('id')
            queryset = Task.objects.get(id=id)
            serializer_class = PostTankSerializer(queryset,data=request.data,partial=True)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):   
        try:
            id = request.query_params.get('id')
            Task.objects.filter(id=id).delete()
            return Response({'message':'Task deleted Successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
class TaskStatusAPI(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):   
        try:
            queryset = TaskStatus.objects.all()
            serializer_class = GetStatusSerializer(queryset,many=True)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):   
        try:
            id = request.data.get('id')
            statusid = request.data.get('status')
            Task.objects.filter(id=id).update(status_id=statusid)
            return Response({'message':'Status Updated Successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)