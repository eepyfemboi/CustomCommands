# CustomCommands.message_components.File.py
"""
Represents a file that can be uploaded to a message
"""
from __future__ import annotations

import io
from typing import Union

import discord

from .Component import MessageComponent


class UnknownFileTypeError(Exception):
    def __init__(self, message: str):
        self.message = message

class File(MessageComponent):
    """
    Represents a file that can be uploaded to a message
    """
    def __init__(
                self, 
                content: Union[io.BytesIO, bytes, str, io.BufferedIOBase], 
                filename: str, 
                filetype: str = None, 
                description: str = None, 
                spoiler: bool = False
            ) -> None:
        if isinstance(content, str):
            content = bytes(str, 'utf-8')
        if isinstance(content, bytes):
            content = io.BytesIO(content)

        self.content = content

        if filetype is not None:
            if filetype.startswith('.'):
                parts = filetype.split('.')
                parts.remove('')
                filetype = '.'.join(parts)
        elif '.' in filename:
            filetype = filename.split('.')[-1]
        else:
            raise UnknownFileTypeError(f'The filetype for `{filename}` is unknown!')

        if not filename.endswith(filetype):
            filename += '.' + filetype

        self.filename = filename
        self.filetype = filetype

        self.description = description
        self.spoiler = spoiler

    def to_file(self):
        return discord.File(
            fp = self.content,
            filename = self.filename,
            description = self.description,
            spoiler = self.spoiler
        )

    @classmethod
    def from_file(cls, file: discord.File):
        return cls(
            content = file.fp,
            filename = file.filename,
            filetype = file.filename.split('.')[-1] if '.' in file.filename else None,
            description = file.description,
            spoiler = file.spoiler
        )
