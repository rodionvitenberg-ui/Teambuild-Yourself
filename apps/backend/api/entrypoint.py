from ninja import NinjaAPI
from users.api import router as users_router

# Инициализируем API
# auth=... добавим чуть позже, пока сделаем публичный доступ для теста
api = NinjaAPI(
    title="Teambuild API",
    version="1.0.0",
    description="The Brain of Teambuild System"
)

# Простой тест на жизнь
@api.get("/health")
def health_check(request):
    return {"status": "ok", "system": "The Brain is working"}

api.add_router("/users", users_router)
# api.add_router("/groups", "groups.api.router")