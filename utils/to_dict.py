# CustomCommands.utils.to_dict.py
from __future__ import annotations

class NoDictConverterError(AttributeError):
    def __init__(self, message: str) -> None:
        self.message: str = message

def to_dict(obj):
    if isinstance(obj, dict):
        return obj
    else:
        try:
            return obj.to_dict()
        except:
            raise NoDictConverterError(f'The object of type `{type(obj)}` has no attribute `to_dict`.')
