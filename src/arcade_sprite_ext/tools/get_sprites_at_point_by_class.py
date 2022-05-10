"""get_sprites_at_point_by_class function."""
import arcade
from ..coords import Coords


def get_sprites_at_point_by_class(
    position: Coords, cls: type, sprite_list: arcade.SpriteList
) -> list[arcade.Sprite]:
    """Get a list of sprites of a given class at a particular point.

    This function finds any sprite which overlaps the specified point and
    matches the given class (including children of that class).

    If a sprite has a different center_x/center_y but touches the point,
    this will return that sprite.

    Parameters
    ----------
    position : Coords
        Position to check.
    cls : type
        Class of sprite to find.
    sprite_list : arcade.SpriteList
        The sprite list to check in.

    Returns
    -------
    list[Sprite]
        List of matching sprites.
    """
    return [
        sprite
        for sprite in arcade.get_sprites_at_point(
            (position.x_coord, position.y_coord), sprite_list
        )
        if isinstance(sprite, cls)
    ]
