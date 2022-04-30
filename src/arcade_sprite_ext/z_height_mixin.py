"""ZHeightMixin"""
import arcade


class ZHeightMixin:
    """A mixin intended to be used with Sprite that adds a z-height to the sprite."""

    def __init__(self, *args, z_height: float, **kwargs):
        """
        Args:
            z_height (float, keyword only): The relative z-height of the sprite.
                Determines the order drawn in.
        """
        super().__init__(*args, **kwargs)
        self.z_height = z_height


class ZHeightSortMixin:  # pylint: disable=too-few-public-methods
    """A mixin intended to be used with SpriteList that sorts Sprites based on z-height."""

    def append(self, sprite: arcade.Sprite) -> None:
        """
        Add a sprite to the list.

        Args:
            sprite (Sprite): Sprite to be added to the list
        """
        if not isinstance(self, arcade.SpriteList):
            raise TypeError("ZHeightMixin only intended for use with SpriteList.")
        instance_super: arcade.SpriteList = super()  # type: ignore
        instance_super.append(sprite)
        instance_super.sort(
            key=lambda x: x.z_height if isinstance(x, ZHeightMixin) else 0
        )


class ZSortedSpriteList(ZHeightSortMixin, arcade.SpriteList):
    """A sprite list that sorts Sprites based on their Z-height, if they have one."""


class SpriteWithZHeight(ZHeightMixin, arcade.Sprite):
    """A sprite with Z-height that sets the order it's drawn
    relative to others in its SpriteList"""

    def __init__(
        self,
        *,
        z_height: float = 0,
        **sprite_kwargs,
    ):
        super().__init__(z_height=z_height, **sprite_kwargs)
