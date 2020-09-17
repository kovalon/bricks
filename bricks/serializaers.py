from django.db.models import Sum
from rest_framework import serializers

from .models import Building, Bricks


class BuildingSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления зданий"""

    class Meta:
        model = Building
        fields = "__all__"


class BricksSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления кирпичей"""

    class Meta:
        model = Bricks
        fields = "__all__"


class BrickSerializer(serializers.ModelSerializer):
    """Сериализатор для информации о кирпичах"""

    class Meta:
        model = Bricks
        fields = ('count', 'date')


class StatSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода статистики по домам и кирпичам"""
    bricks = BrickSerializer(Bricks.objects.all().annotate(Sum('date')), many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('address', 'year', 'bricks')
