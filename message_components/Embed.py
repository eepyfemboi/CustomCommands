# CustomCommands.message_components.Embed.py
"""
Represents a custom embed
"""
from __future__ import annotations

import json
from typing import *

import discord
from discord import Colour
from discord.ext import commands

from .Component import MessageComponent


class EmbedComponent:
    def to_dict(self) -> Dict[str, str]:...

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> EmbedComponent:...

    def to_json(self) -> str:
        data = self.to_dict()
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_data: str) -> EmbedComponent:
        data = json.loads(json_data)
        return cls.from_dict(data)

    def __str__(self) -> str:
        return self.to_json()

    def __repr__(self) -> str:
        return repr(self.to_dict())

class EmbedFooter(EmbedComponent):
    def __init__(self, icon_url: str = None, text: str = None) -> None:
        self.icon_url: str = icon_url
        self.text: str = text

    def to_dict(self) -> Dict[str, str]:
        return {
            'icon_url': self.icon_url,
            'text': self.text
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> EmbedFooter:
        return cls(
            icon_url = data.get('icon_url', None),
            text = data.get('text', None)
        )

class EmbedAuthor(EmbedComponent):
    def __init__(self, icon_url: str = None, text: str = None, url: str = None) -> None:
        self.icon_url: str = icon_url
        self.text: str = text
        self.url: str = url

    def to_dict(self) -> Dict[str, str]:
        return {
            'icon_url': self.icon_url,
            'text': self.text,
            'url': self.url
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> EmbedAuthor:
        return cls(
            icon_url = data.get('icon_url', None),
            text = data.get('text', None),
            url = data.get('url', None)
        )

class Embed(MessageComponent):
    def __init__(
                self, 
                title: str = '', 
                description: str = '', 
                color: str = 'rgb(0, 0, 0)', 
                image_url: str = None, 
                thumbnail_url: str = None, 
                footer: Union[EmbedFooter, Dict[str, str]] = EmbedFooter(), 
                author: Union[EmbedAuthor, Dict[str, str]] = EmbedAuthor()
            ) -> None:
        self.title: str = title
        self.description: str = description
        self.color: Colour = Colour.from_str(color)
        self.image_url: str = image_url
        self.thumbnail_url: str = thumbnail_url
        self.footer: EmbedFooter = footer
        self.author: EmbedAuthor = author

    def to_dict(self) -> Dict[str, str]:
        return {
            'title': self.title,
            'description': self.description,
            'color': 'rgb' + str(self.color.to_rgb()),
            'image': self.image_url,
            'thumbnail': self.thumbnail_url,
            'footer': self.footer.to_dict(),
            'author': self.author.to_dict()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> Embed:
        return cls(
            title = data.get('title', ''),
            description = data.get('description', ''),
            color = Colour.from_str(data.get('color', 'rgb(0, 0, 0)')),
            footer = EmbedFooter.from_dict(data.get('footer', EmbedFooter().to_dict())),
            image_url = data.get('image', None),
            thumbnail_url = data.get('thumbnail', None),
            author = EmbedAuthor.from_dict(data.get('author', EmbedAuthor().to_dict()))
        )

    def to_json(self) -> str:
        data = self.to_dict()
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_data: str) -> Embed:
        data = json.loads(json_data)
        return cls.from_dict(data)

    def __str__(self) -> str:
        return self.to_json()

    def __repr__(self) -> str:
        return repr(self.to_dict())
