def validate_room_slug(value):
    from django.core.exceptions import ValidationError
    from slugify import slugify

    from .models import (
        Room,
    )

    rooms_slugs = [
        room.get('slug')
        for room in Room.objects.all().values('slug')
    ]
    if slugify(value) in rooms_slugs:
        raise ValidationError('Room with similar name already exists.')
