import urllib

from api.services.ArtistService import ArtistService
from api.connectors.BaseConnector import BaseConnector

"""
@class      ArtistsConnector
@author     Nils Berlijn
@version    1.0
@since      1.0
"""
class ArtistsConnector(BaseConnector, ArtistService):
    def __init__(self):
        BaseConnector.__init__(self)
        ArtistService.__init__(self)

    def connected_get_artists(self, api_key, characters, page_size, page_number):
        return self.connect(api_key, self.http.request('GET',
                                                       self.api_url() + 'artists' + '?api_key=' + self.api_key() + '&characters=' + characters + '&page_size=' + page_size + '&page_number=' + page_number).data)

    def connected_get_artist(self, api_key, name):
        return self.connect(api_key, self.http.request('GET',
                                                       self.api_url() + 'artists/' + urllib.quote(name) + '?api_key=' + self.api_key()).data)
