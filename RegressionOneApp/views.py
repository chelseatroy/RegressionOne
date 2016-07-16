from django.shortcuts import render
from RegressionOneApp.serializers import ThingamabobSerializer
from RegressionOneApp.models import Thingamabob
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
from django.http import HttpResponse


def foo(request):
    return HttpResponse("Hello World!")


def bar(request):
    return HttpResponse("Bar! Baz!")


class ThingamabobsView(APIView):
    def post(self, request):
        serializer = ThingamabobSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            t = Thingamabob(description=data['description'], done=False)
            t.save()
            request.data['id'] = t.pk  # return id
            return Response(request.data, status=status.HTTP_201_CREATED)
