from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Building
from .serializaers import BuildingSerializer, BricksSerializer, StatSerializer


class BuildingCreateView(APIView):
    """Создание записи о здании
        Формат ввода данных:
        {
            "address": "string",
            "year": "string"
        }
    """

    def post(self, request):
        if 'address' in request.data and 'year' in request.data:
            building = BuildingSerializer(data=request.data)
            if building.is_valid():
                building.save()
        else:
            return Response({"error": "bad request"}, status=400)
        return Response(status=201)


class BricksCreateView(APIView):
    """Создание записи о кирпичах
        Формат ввода данных:
        {
            "count": "integer"
        }
    """

    def post(self, request, id):
        building = Building.objects.get(id=id)
        if not building:
            return Response({"error": "building not found"}, status=404)
        if 'count' not in request.data:
            return Response({"error": "bad request"}, status=400)
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
