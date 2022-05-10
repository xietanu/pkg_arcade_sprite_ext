"""z-height mixin classes."""
import arcade


class ZHeightMixin:
    """A mixin intended to be used with Sprite that adds a z-height to the sprite."""

    def __init__(self, *args, z_height: float, **kwargs):
        """Initialize the sprite with a z-height.

        Parameters
        ----------
            *args
                Positional arguments to pass to the parent Sprite constructor.
            z_height : float, keyword only
                The relative z-height of the sprite.
                Determines the order drawn in (higher is on top).
            **kwargs
                Keyword arguments to pass to the parent Sprite constructor.

        """
        super().__init__(*args, **kwargs)
        self.z_height = z_height


class ZHeightSortMixin:  # pylint: disable=too-few-public-methods
    """A mixin intended to be used with SpriteList that sorts Sprites based on z-height.

    Sprites with no z-height will be treated as having a z-height of 0.
    """

    def append(self, sprite: arcade.Sprite) -> None:
        """Add a sprite to the list, then sort the sprites by their z-height.

        Parameters
        ----------
            sprite : Sprite
                Sprite to be added to the list.

        Raises
        ------
            TypeError
                If used with a non-SpriteList object.
        """
        if not isinstance(self, arcade.SpriteList):
            raise TypeError("ZHeightMixin only intended for use with SpriteList.")
        instance_super: arcade.SpriteList = super()  # type: ignore
        instance_super.append(sprite)
        instance_super.sort(
            key=lambda x: x.z_height if isinstance(x, ZHeightMixin) else 0
        )


class ZSortedSpriteList(ZHeightSortMixin, arcade.SpriteList):
    """A sprite list that sorts Sprites based on their z-height, if they have one.

    Sprites with no z-height will be treated as having a z-height of 0.
    """


class SpriteWithZHeight(ZHeightMixin, arcade.Sprite):
    """A sprite with a z-height.

    The z-height sets the order it's drawn relative to others in its SpriteList.
    """

    def __init__(
        self,
        *,
        z_height: float = 0,
        **sprite_kwargs,
    ):
        """Create a sprite with a z-height.

        The z-height sets the order it's drawn relative to others in its SpriteList.
        A higher z-height sprite will be drawn on top of a lower z-height sprite
        in the same sprite list.
        Must be added tp a sprite list with a z-height mixin for z-height functions to work.

        Parameters
        ----------
        z_height : float, optional
            The relative z-height of the sprite, by default 0
        """
        super().__init__(z_height=z_height, **sprite_kwargs)
