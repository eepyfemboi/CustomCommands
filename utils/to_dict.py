# CustomCommands.utils.to_dict.py
"""
Converts an item to a dict
"""
from __future__ import annotations

class NoDictConverterError(AttributeError):
    """
    Raised when the requested item cannot be converted to a dict
    """
    def __init__(self, message: str) -> None:
        self.message: str = message

def to_dict(obj) -> dict:
    """
    Converts an object to a dict.
    If the provided object is already a dict it just returns the same object
    If the provided object doesn't have a `to_dict` function it raises NoDictConverterError
    """
    if isinstance(obj, dict):
        return obj
    else:
        try:
            return obj.to_dict()
        except:
            raise NoDictConverterError(f'The object of type `{type(obj)}` has no attribute `to_dict`.')
