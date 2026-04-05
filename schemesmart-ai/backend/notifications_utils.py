from backend.models import Notification, User
from sqlalchemy.future import select

async def notify_all_users(db, scheme_name):

    result = await db.execute(select(User))
    users = result.scalars().all()

    for user in users:
        notification = Notification(
            user_id=user.id,
            message=f"New scheme added: {scheme_name}"
        )
        db.add(notification)

    await db.commit()