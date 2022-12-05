from uuid import UUID
from typing import Protocol, Dict
from entities.videos import Video
from external_systems.data_access.rds.abstract.common_protocols import (
    Searchable,
    Updatable
)
from external_systems.data_access.rds.abstract.videos import VideosDatabase


class SearchableUpdatable(Searchable, Updatable, Protocol):
    pass


class DescribeDbVideosFn(Protocol):
    def __call__(
        self,
        database: VideosDatabase,
        hash_id: UUID,
        authenticated_user_id: UUID
    ) -> SearchableUpdatable:
        ...


class PrepareNewListingBeforePublishFn(Protocol):
    def __call__(self, video: Video) -> Video:
        ...


class ParseVideoIntoStateDictFn(Protocol):
    def __call__(self, video: Video) -> Dict:
        ...
