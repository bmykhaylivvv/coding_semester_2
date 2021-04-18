'''
Module webpage retrieving and saving cache.
'''

from urllib.request import urlopen
import time


class WebPage:
    '''
    Class for retrieving and saving website cache.
    '''

    def __init__(self, url, reload_time=3):
        self.url = url
        self._content = None
        self.reload_time = reload_time
        self.latest_reload = None

    @property
    def content(self):
        '''
        Retrieve and save website cache.
        '''
        now = time.time()
        if not self._content or now - self.latest_reload > self.reload_time:
            print('Retrieving New Page...')
            self._content = urlopen(self.url).read()
            self.latest_reload = time.time()

        return self._content
