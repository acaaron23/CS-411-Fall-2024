from typing import Optional

from wildlife_tracker.migration_path.migration import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationPath:
    def __init__(self) -> None:
        paths: dict[int, MigrationPath] = {}

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass

    def get_migration_paths() -> list[MigrationPath]:
        pass

    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass

    