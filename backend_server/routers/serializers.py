from rest_framework import serializers

class Attendance(serializers.Serializer):
    email = serializers.EmailField()