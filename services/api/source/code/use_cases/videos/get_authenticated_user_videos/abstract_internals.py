from external_systems.data_access.rds.abstract.videos import VideosDatabase
from uuid import UUID
from typing import Protocol
from external_systems.data_access.rds.abstract.common_protocols import (
    Searchable
)


class DescribeDbUnprocessedVideosFn(Protocol):
    def __call__(
        self,
        database: VideosDatabase,
        authenticated_user_id: UUID
    ) -> Searchable:
        ...


class DescribeDbVideosFn(Protocol):
    def __call__(
        self,
        database: VideosDatabase,
        authenticated_user_id: UUID
    ) -> Searchable:
        ...
