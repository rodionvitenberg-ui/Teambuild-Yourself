from ninja import Router
from django.shortcuts import get_object_or_404
from .models import User
from .schemas import UserOut

router = Router()

@router.get("/me", response=UserOut)
def get_me(request):
    # Пока хардкод: берем первого попавшегося юзера для теста
    # (позже здесь будет request.user из токена)
    user = User.objects.first()
    if not user:
        return 404, {"detail": "No users found. Create one via admin first."}
    return user