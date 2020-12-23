import pytest
from dataclasses import dataclass

from .entities import (
    ShapeCollection,
    CustomShape,
    ShapeContainer,
)

from mashumaro.exceptions import UnserializableField, UnserializableDataError,\
    MissingField, InvalidFieldValue

def test_union():
    dumped = {'shapes': ['triange', {'name': 'square', 'num_corners' : 4}]}
    assert ShapeCollection._from_dict(dumped)._to_dict() == dumped

def test_invalid_union():
    dumped = {'shapes': ['triange', {'badfield': True}]}
    with pytest.raises(InvalidFieldValue):
        ShapeCollection._from_dict(dumped)

def test_dict_value():
    dumped = { 'shapes': {} }
    assert ShapeContainer._from_dict(dumped)._to_dict() == {'shapes': {'name': 'SomeShape', 'num_corners': 4}}

def test_invalid_union_no_match_from_dict():
    dumped = {'shapes': ['triange', {'name': 'square', 'num_corners': 'four'}]}
    with pytest.raises(ValueError):
        ShapeCollection._from_dict(dumped)

def test_invalid_union_no_match_to_dict():
    invalid = ShapeCollection(shapes=[
        'triange',
        CustomShape(name='square', num_corners='four'),
    ])

    with pytest.raises(ValueError):
        invalid._to_dict()
