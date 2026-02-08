from ninja import Schema
from uuid import UUID

class UserProfileSchema(Schema):
    timezone: str
    subscription_tier: str
    global_streak: int
    avatar_url: str | None = None

class UserOut(Schema):
    id: UUID  # Отдаем public_id, а не внутренний int
    username: str
    email: str
    profile: UserProfileSchema  # Вложенная схема