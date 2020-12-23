from enum import Enum, IntEnum, Flag, IntFlag
from dataclasses import dataclass
from typing import Union, List

from mashumaro import DataClassDictMixin
from mashumaro.types import SerializableType


class MyEnum(Enum):
    a = 'letter a'
    b = 'letter b'


class MyIntEnum(IntEnum):
    a = 1
    b = 2


class MyFlag(Flag):
    a = 1
    b = 2


class MyIntFlag(IntFlag):
    a = 1
    b = 2


@dataclass
class ShapeWithDefaults(DataClassDictMixin):
    name: str = 'SomeShape'
    num_corners: int = 4

@dataclass 
class CustomShape(DataClassDictMixin):
    name: str
    num_corners: int

@dataclass
class ShapeCollection(DataClassDictMixin):
    shapes: List[Union[str, CustomShape]]

@dataclass
class ShapeContainer(DataClassDictMixin):
    shapes: Union[ShapeWithDefaults, None]

@dataclass
class MyDataClass(DataClassDictMixin):
    a: int
    b: Union[int, str]

class MutableString(SerializableType):
    def __init__(self, value: str):
        self.characters = [c for c in value]

    def _serialize(self) -> str:
        return str(self)

    @classmethod
    def _deserialize(cls, value: str) -> 'MutableString':
        return MutableString(value)

    def __str__(self):
        return ''.join(self.characters)

    def __eq__(self, other):
        return self.characters == other.characters
