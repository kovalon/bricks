from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Building, Bricks
from .serializaers import BuildingSerializer, BricksSerializer, StatSerializer


class BuildingCreateView(APIView):
    """Создание записи о здании"""

    def post(self, request):
        building = BuildingSerializer(data=request.data)
        if building.is_valid():
            building.save()
        return Response(status=201)


class BricksCreateView(APIView):
    """Создание записи о кирпичах"""

    def post(self, request, id):
        building = Building.objects.get(id=id)
        bricks = BricksSerializer(data={'building': id, 'count': request.data['count']})
        if bricks.is_valid():
            bricks.save()
        return Response(status=201)


class StatListView(APIView):
    """Вывод информации по домам и кирпичам"""

    def get(self, request):
        buildings = Building.objects.all()
        stats = StatSerializer(buildings, many=True)
        return Response(stats.data)
