import enum
from uuid import UUID


class ResourceType(str, enum.Enum):
    Corpus = "corpus"
    Lexicon = "lexicon"

    @classmethod
    def from_str(cls, value: str) -> "ResourceType":
        for v in ResourceType:
            if v.value == value:
                return v
        raise ValueError(f"Unknown ResourceType (got '{value}')")


class Resource:
    def __init__(
        self,
        *,
        id: UUID,
        name: str,
        type: ResourceType,
    ) -> None:
        self._id = id
        self._name = name
        self._type = type

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> ResourceType:
        return self._type

    def set_name(self, name: str) -> None:
        # TODO validate name
        self._name = name
