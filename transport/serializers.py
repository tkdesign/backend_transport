from rest_framework import serializers
from .models import Order, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ["id", "location", "type"]


class OrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "order_number", "customer_name", "date", "waypoints"]

    def create(self, validated_data):
        waypoints_data = validated_data.pop("waypoints")
        order = Order.objects.create(**validated_data)
        for wp in waypoints_data:
            Waypoint.objects.create(order=order, **wp)
        return order
