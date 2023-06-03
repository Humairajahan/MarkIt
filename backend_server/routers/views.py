from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Attendance

class CheckIn(APIView):
    def post(self, request):
        serializer = Attendance(data=request.data)
        if serializer.is_valid():
            try:
                content = {
                    "user": serializer.validated_data["email"],
                    "status": "check-in with MarkIt successful!",
                    "time": datetime.now(),
                }
                return Response(content, status=200)
            except Exception:
                return Response("check-in with MarkIt failed", status=500)
        else:
            return Response(serializer.errors, status=400)
