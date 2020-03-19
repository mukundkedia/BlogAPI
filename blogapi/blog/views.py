# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here
class BlogAPIView(APIView):
    def get(self,request):
        blogdata = Blog.objects.all()
        serializer = BlogSerializer(blogdata, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = request.data
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)        

class BlogDetail(APIView):
    def get_object(self,id):
        try:
            return Blog.objects.get(id=id)

        except:
            return HttpResponse(status=status.HTTP_404_BAD_REQUEST)

    def get(self,request,id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)    

    def put(self,request,id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

    def delete(self,request,id):
        blog = self.get_object(id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
