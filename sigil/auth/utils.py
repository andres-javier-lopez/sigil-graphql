import logging
from typing import Union
from uuid import UUID

from starlette.requests import Request

from sigil.settings import ANON_USER_ENABLED, ANON_UUID, USER_ID_HEADER

logger = logging.getLogger(__name__)


def get_user_id(request: Request) -> Union[UUID, None]:
    user_id = request.headers.get(USER_ID_HEADER)
    if user_id:
        try:
            return UUID(user_id)
        except ValueError:
            logger.warning(f"Invalid uuid {user_id} in user id")
            return None

    if ANON_USER_ENABLED:
        logger.info("Using anon user")
        return UUID(ANON_UUID)

    logger.info("No user provided")
    return None
