from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class MetroListView(APIView):
    """Вывод информации московском метрополитене
        Формат ввода данных: ["станция1", "станция2", ..., "станцияN"]
    """

    def post(self, request):
        result = requests.get('https://api.hh.ru/metro/1').json()
        data = [lines['stations'] for lines in result['lines']]
        stations = []
        for element in data:
            stations.extend(el['name'] for el in element)
        if not isinstance(request.data, list):
            return Response({"error": "bad request"}, status=400)
        unchanged = [el for el in request.data if el in stations]
        updated = [el for el in request.data if el not in stations]
        deleted = [el for el in stations if el not in request.data]

        result = {
            'unchanged': unchanged,
            'updated': updated,
            'deleted': deleted,
        }

        return Response(result)
