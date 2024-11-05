from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@login_required
def chart_view(request):
    return render(request, 'charts/chart.html')

class ChartDataAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"values": [10, 15, 20, 25, 30]}
        return Response(data)
