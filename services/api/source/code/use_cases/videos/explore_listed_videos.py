from common.constants import LISTED_VIDEOS_QUERY_PAGE_LIMIT
from typing import List, Union, Callable, Optional
from uuid import UUID
from entities.videos import Video
from use_cases.validation_utils import is_anonymous_user
from external_systems.data_access.rds.abstract.videos import VideosDB


def make_explore_listed_videos(database: VideosDB) -> Callable[[Union[UUID, str], Optional[bool]], List[Video]]:
    """Creates Explore Listed Videos use case"""

    async def explore_listed_videos(
        authenticated_user_id: Union[UUID, str],
        pagination_index_is_smaller_than: int,
        include_my: Optional[bool] = False
    ) -> List[Video]:
        """Gets Listed Videos"""

        # if user wants to excldue its own videos while exploring, then mark it as excluded
        excluded_user_id = None if include_my else authenticated_user_id
        # allow authenticated user to view it's own private videos
        allow_privates_of_user_id = None if is_anonymous_user(user_id=authenticated_user_id) else authenticated_user_id

        return await (
            database.videos()
            .allow_privates_of(user_id=allow_privates_of_user_id)
            .hide_unlisted(flag=True)
            .exclude_user(user_id=excluded_user_id)
            .paginate(pagination_index_is_smaller_than=pagination_index_is_smaller_than)
            .limit(limit=LISTED_VIDEOS_QUERY_PAGE_LIMIT)
            .search()
        )

    return explore_listed_videos
