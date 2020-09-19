import re
from typing import List, Union

from ..RawSonarr import RawSonarrAPI


class Show:
    """
    Show object for each show in Sonarr
    """
    def __init__(self, data):
        self.id = None
        self.title = None
        self.alternateTitles = None
        self.sortTitle = None
        self.seasonCount = None
        self.totalEpisodeCount = None
        self.episodeCount = None
        self.episodeFileCount = None
        self.sizeOnDisk = None
        self.overview = None
        self.nextAiring = None
        self.previousAiring = None
        self.network = None
        self.airTime = None
        self.images: Union[List[SonarrImage], None] = None
        self.seasons: Union[List[SonarrSeason], None] = None
        self.year = None
        self.path = None
        self.profileId = None
        self.seasonFolder = None
        self.monitored = None
        self.useSceneNumbering = None
        self.runtime = None
        self.tvdbId = None
        self.tvRageId = None
        self.tvMazeId = None
        self.firstAired = None
        self.lastInfoSync = None
        self.seriesType = None
        self.cleanTitle = None
        self.imdbId = None
        self.titleSlug = None
        self.certification = None
        self.genres = None
        self.tags = None
        self.added = None
        self.ratings = None
        self.qualityProfileId = None

        self.__load_json(data)

    def __str__(self):
        """
        String representation is the title.
        :return:
        """
        return self.title

    def __load_json(self, data):
        """
        Load the data into the class attributes
        :param data:
        :return:
        """
        exempt_keys = ['alternateTitles', 'images', 'seasons']
        for key in data:
            if key not in exempt_keys:
                setattr(self, key, data[key])
            elif isinstance(data[key], list):
                setattr(self, key, [])

                if key == 'alternateTitles':
                    for alt_titles in data[key]:
                        self.alternateTitles.append(alt_titles)

                if key == 'images':
                    for image in data[key]:
                        self.images.append(SonarrImage(image))

                if key == 'seasons':
                    for season in data[key]:
                        self.seasons.append(SonarrSeason(season))

    def get_image(self, coverType):
        for image in self.images:
            if image.coverType == coverType:
                return image

    @property
    def banner(self):
        return self.get_image('banner')

    @property
    def poster(self):
        return self.get_image('poster')

    @property
    def fan_art(self):
        return self.get_image('fanart')


class SonarrImage(RawSonarrAPI):
    """
    Sonarr image object
    """
    def __init__(self, data):
        super().__init__()
        self.coverType: str = data['coverType']
        self.__url: str = data['url']

    @property
    def full_url(self):
        """
        Full URL to image property.
        :return:
        """
        clean_url = re.compile(r'(.+)(?=\?)')
        matches = clean_url.match(self.__url.lstrip('/').lstrip('sonarr'))
        return self.url_with_key(matches.group(1))


class SonarrSeason:
    """
    Sonarr season object
    """
    def __init__(self, data):
        self.seasonNumber = data['seasonNumber']
        self.monitored = data['monitored']
        self.statistics = SonarrSeasonStatistics(data['statistics'])


class SonarrSeasonStatistics:
    """
    Sonarr season statistic object
    """
    def __init__(self, data):
        self.nextAiring = None
        self.previousAiring = None
        self.episodeFileCount = None
        self.totalEpisodeCount = None
        self.sizeOnDisk = None
        self.percentOfEpisodes = None

        for key in data:
            setattr(self, key, data[key])
