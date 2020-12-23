from typing import Mapping

from mashumaro.serializer.base.metaprogramming import CodeBuilder


class DataClassDictMixin:
    def __init_subclass__(cls, **kwargs):
        builder = CodeBuilder(cls)
        exc = None
        try:
            builder.add_from_dict()
        except Exception as e:
            exc = e
        try:
            builder.add_to_dict()
        except Exception as e:
            exc = e
        if exc:
            raise exc

    def _to_dict(
            self,
            use_bytes: bool = False,
            use_enum: bool = False,
            use_datetime: bool = False,
            omit_none:bool = False) -> dict:
        pass

    def after_to_dict(self, dct, omit_none: bool = False):
        return dct

    @classmethod
    def _from_dict(
            cls,
            d: Mapping,
            use_bytes: bool = False,
            use_enum: bool = False,
            use_datetime: bool = False) -> 'DataClassDictMixin':
        pass

    @classmethod
    def before_from_dict(cls, d: Mapping):
        return d


__all__ = [
    'DataClassDictMixin'
]
