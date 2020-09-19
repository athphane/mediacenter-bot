from .Shows import Shows
from .episodes import Episodes
from .models import Show
from .system_stats import SystemStats


class Sonarr(Shows, Episodes, SystemStats):
    """Sonarr API Methods"""
