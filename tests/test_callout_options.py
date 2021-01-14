from dataclasses import dataclass
from typing import Optional

from mashumaro import DataClassDictMixin


def test_omit_none():
    class MyDataClassDictMixin(DataClassDictMixin):

        def __post_serialize__(self, dct, options=None):
            keep_none = False
            if options and 'keep_none' in options and options['keep_none']:
                keep_none = True
            if not keep_none:  # remove attributes that are None
                new_dict = {k: v for k, v in dct.items() if v is not None}
                dct = new_dict
            return dct

    @dataclass
    class DataClass(MyDataClassDictMixin):
        name: str
        variation: Optional[str] = None
        some_flag: Optional[bool] = None

    instance = DataClass(name='testing')
    dct = instance.to_dict(options={'keep_none': False})

    assert 'variation' not in dct
