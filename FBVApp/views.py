from django.shortcuts import render
from .models import Course,CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET','POST'])
def courseListView(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        courseSerializers = CourseSerializer(courses,many= True)
        return Response(courseSerializers.data)
    elif request.method == "POST":
       courseSerializers = CourseSerializer(data= request.data)
       if courseSerializers.is_valid():
            courseSerializers.save()
            return Response(courseSerializers.data)
       return Response(courseSerializers.errors)     
            
@api_view(['GET','PUT','DELETE'])
def courseDetailsView(request,pk):
    try:
        course = Course.objects.get(pk=pk)

    except Course.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)    

    if request.method == 'GET':
         courseSerializer = CourseSerializer(course)
         return Response(courseSerializer.data)

    elif request.method == 'PUT':
            courseSerializer = CourseSerializer(course,data = request.data)
            if courseSerializer.is_valid():
                courseSerializer.save()
                return Response(courseSerializer.data,status=status.HTTP_201_CREATED)

            return Response(courseSerializer.errors)    

    elif request.method == 'DELETE':   
            
            course.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)

