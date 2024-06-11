from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDoList
from .serializers import ToDoListSerializer
from django.shortcuts import get_object_or_404


class ViewToDoListAPI(APIView):
    def get(self, request):
        todos = ToDoList.objects.all()
        serializer = ToDoListSerializer(todos, many=True)
        return Response(serializer.data)


class ViewToDoListCreateAPI(APIView):
    def post(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewToDoListUpdateAPI(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(ToDoList, pk=pk)
        serializer = ToDoListSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewToDoListDeleteAPI(APIView):
    def delete(self, request, pk):
        todo = get_object_or_404(ToDoList, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewToDoListDetailAPI(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDoList, pk=pk)
        serializer = ToDoListSerializer(instance=todo)
        return Response(serializer.data)
