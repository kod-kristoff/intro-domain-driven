from pathlib import Path
from uuid import UUID

import pytest

from resources.infrastructure.repositories.json_file_resources import (
    JsonFileResourceRepository,
)
from resources.application.repositories.resources import ResourceRepository
from resources.application.use_cases.updating_name import UpdateName, UpdatingName


@pytest.fixture()
def repo():
    return JsonFileResourceRepository(Path("tests/assets/resources.json"))


@pytest.fixture()
def resource_id():
    return UUID("53dd4178-17fa-4725-a5ef-1a217e9946b9")


def test_updating_name_succeeds(repo: ResourceRepository, resource_id: UUID):
    uc = UpdatingName(repo=repo)

    input_dto = UpdateName(
        id=resource_id,
        name="Lexicon Royale",
    )
    uc.execute(input_dto)

    resource = repo.get(resource_id)

    assert resource.name == "Lexicon Royale"
