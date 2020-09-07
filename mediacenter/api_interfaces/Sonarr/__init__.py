from .Shows import Shows
from .episodes import Episodes
from .models import Show


class Sonarr(Shows, Episodes):
    """Sonarr API Methods"""
