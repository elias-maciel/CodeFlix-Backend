from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        return Response(
            status=HTTP_200_OK,
            data=[
                {
                    "id": "c71d6b9f-a549-4e43-b8cd-da6d430a47da",
                    "name": "Movie",
                    "description": "Movie description",
                    "is_active": True,
                },
                {
                    "id": "c71d6b9f-a549-4e43-b8cd-da6d430a47db",
                    "name": "Documentary",
                    "description": "Documentary description",
                    "is_active": True,
                },
            ],
        )