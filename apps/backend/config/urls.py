from django.contrib import admin
from django.urls import path
from api.entrypoint import api  # Импортируем наш инстанс API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Все запросы на /api/... уходят в Ninja
]