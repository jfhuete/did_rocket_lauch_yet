from bernard.conf import settings
import requests


class FrameXApi:
    """
    This class provide a handler to interact with Frame X API

    :param video_name: Name of the video to obtain information
    """

    def __init__(self, video_name):
        self.api_url = settings.FRAMEX_API_URL

        response = requests.get(self.api_url)
        body = response.json()

        self.video_properties = filter(lambda x: x['name'] == video_name, body)
