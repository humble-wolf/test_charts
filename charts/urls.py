from django.urls import path
from .views import chart_view, ChartDataAPI

urlpatterns = [
    path('', chart_view, name='chart-view'),
    path('api/chart-data/', ChartDataAPI.as_view(), name='chart-data-api'),
]
