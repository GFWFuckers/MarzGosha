from datetime import datetime

from app import logger, scheduler, xray
from app.db import (GetDB, crud)
from app.models.user import UserStatus
from app.utils import report
from app.utils.concurrency import GetBG
from config import AUTO_DELETE_INACTIVE_USERS
    

def auto_delete():
    if AUTO_DELETE_INACTIVE_USERS:
        with GetDB() as db, GetBG() as bg:
            for user in crud.get_users(db):
                if user.online_at and user.status not in (UserStatus.active, UserStatus.on_hold):
                    user_online = datetime.strptime(user.online_at.rstrip('Z'), "%Y-%m-%dT%H:%M:%S.%f" if '.' in user.online_at else "%Y-%m-%dT%H:%M:%S")
                    if user_online.day > AUTO_DELETE_INACTIVE_USERS:
                        crud.remove_user(db, user)
                        xray.operations.remove_user(user)
                        report.user_deleted(username=user.username, by='auto_delete', user_admin=user.admin)
                        logger.info(f"Deleted inactive user \"{user.username}\" who was last online at {user.online_at}")

scheduler.add_job(auto_delete, 'interval', days=1, coalesce=True, max_instances=1)
