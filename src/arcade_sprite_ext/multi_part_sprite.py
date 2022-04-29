"""Classes for handling multi-part sprites, derived from arcade.Sprite"""
from typing import Optional
import arcade

from . import coords


class MultiPartSprite(arcade.Sprite):
    """A subclass of Sprite that allows for the sprite to have sub-sprite elements
    Sub sprites are automatically added and removed from the relevant sprite lists.
    However, their position needs to be manually updated."""

    def __init__(  # pylint: disable=too-many-locals, too-many-arguments
        self,
        filename: Optional[str] = None,
        scale: float = 1,
        image_x: float = 0,
        image_y: float = 0,
        image_width: float = 0,
        image_height: float = 0,
        center_x: float = 0,
        center_y: float = 0,
        flipped_horizontally: bool = False,
        flipped_vertically: bool = False,
        flipped_diagonally: bool = False,
        hit_box_algorithm: str = "Simple",
        hit_box_detail: float = 4.5,
        texture: Optional[arcade.Texture] = None,
        angle: float = 0,
    ):
        super().__init__(
            filename=filename,  # type: ignore
            scale=scale,
            image_x=image_x,
            image_y=image_y,
            image_width=image_width,
            image_height=image_height,
            center_x=center_x,
            center_y=center_y,
            flipped_horizontally=flipped_horizontally,
            flipped_vertically=flipped_vertically,
            flipped_diagonally=flipped_diagonally,
            hit_box_algorithm=hit_box_algorithm,
            hit_box_detail=hit_box_detail,
            texture=texture,  # type: ignore
            angle=angle,
        )

        self._sub_sprites: dict[str, arcade.Sprite] = {}

    def remove_from_sprite_lists(self) -> None:
        super().remove_from_sprite_lists()

        for _, sprite in self._sub_sprites.items():
            sprite.remove_from_sprite_lists()

    def add_sub_sprite(
        self, name: str, sub_sprite: arcade.Sprite, offset: coords.Coords
    ) -> None:
        """
        Add a sub sprite to the sprite, with a specified offset.

        Args:
            name (str): Name to assign the sub sprite.
            sub_sprite (arcade.Sprite): The sprite to add.
            offset (coords.Coords): The offset from the original sprite.
        Raises:
            KeyError: If the sub-sprite already exists.
        """
        if name in self._sub_sprites:
            raise KeyError(f"{name} already exists as a sub sprite of {self}.")
        self._sub_sprites[name] = sub_sprite
        sub_sprite.set_position(
            self.center_x + offset.x_coord, self.center_y + offset.y_coord
        )

    def remove_sub_sprite(self, name: str) -> None:
        """
        Remove a sub sprite from the sprite by name.

        Args:
            name (str): Name of the sub sprite to remove.

        Raises:
            KeyError: If the name does not match a sub sprite.
        """
        if name not in self._sub_sprites:
            raise KeyError(f"{name} not a sub sprite of {self}.")
        self._sub_sprites.pop(name).remove_from_sprite_lists()

    def get_sub_sprite(self, name: str) -> arcade.Sprite:
        """
        Get a sub sprite by name.

        Args:
            name (str): Name of the sub sprite

        Raises:
            KeyError: If the sub-sprite does not exist

        Returns:
            arcade.Sprite: The sub-sprite associated with the given name.
        """
        if not name in self._sub_sprites:
            raise KeyError(f"{name} not a sub sprite of {self}.")
        return self._sub_sprites[name]

    def get_all_sprites(self) -> list[arcade.Sprite]:
        """
        Get the sprite and all its sub-sprites (including recursively).

        Returns:
            list[arcade.Sprite]: List of all the sub-sprites.
        """
        all_sprites: list[arcade.Sprite] = [self]

        for _, sprite in self._sub_sprites.items():
            if isinstance(sprite, MultiPartSprite):
                all_sprites += sprite.get_all_sprites()
            else:
                all_sprites.append(sprite)

        return all_sprites

    def sub_sprite_exists(self, name: str) -> bool:
        """
        Check if a sub sprite with the given name exists.

        Args:
            name (str): Name of the sub sprite.

        Returns:
            bool: Whether the sub sprite exists.
        """
        return name in self._sub_sprites
