"""A package that provides additional functionality to Arcade sprites.

Includes:
- MultiPartSprite: A sprite that supports adding additional sub-sprites that
    are drawn and move with their parent sprite.
- ZHeightMixin: A mixin for Arcade Sprite classes that adds a z-height to them.
    When used with a sprite list with the ZHeightSortMixin, the sprites within
    the list will automatically be drawn in ascending z-height order.
- ZHeightSortMixin: A mixin for Arcade SpriteList classes that adds support for
    sorting by z-height. Sprites without a z-height will treated as having a
    z-height of 0.
- SpriteWithZHeight: A basic Arcade Sprite with the z-height mixin applied.
- ZSortedSpriteList: A basic Arcade SpriteList with the z-height mixin applied.
- Coords:  Class for storing 2D or 3D coordinates. Has methods to adding,
    subtracting and measuring the Euclidean distance between them.
- tools: This module provides useful functions to aid manipulating sprites.
    - get_sprites_at_point_by_class: Get a list of sprites of a given class
        at a particular point.
"""
from . import tools
from .multi_part_sprite import MultiPartSprite
from .coords import Coords
from .z_height_mixin import (
    ZHeightMixin,
    ZSortedSpriteList,
    SpriteWithZHeight,
    ZHeightSortMixin,
)
