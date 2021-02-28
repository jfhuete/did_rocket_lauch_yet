from bernard.conf import settings
import requests


class FrameXApi:
    """
    This class provide a handler to interact with Frame X API

    This class have the neccesaries methods to interact with Frame X API and
    get the images requested

    :param video_name: Name of the video to obtain information
    """

    def __init__(self, video_name):
        self.api_url = settings.FRAMEX_API_URL
        self.video_name = video_name
        self.__video = None

    @property
    def video(self):
        """
        Property that is FrameXVideo instance

        This property request to Frame X Api the metadata of the video called as
        video_name attribute. This property will be cached
        """

        if self.__video is None:
            response = requests.get(self.api_url)
            body = response.json()

            self.__video = FrameXVideo(
                **next(filter(lambda x: x['name'] == self.video_name, body))
            )

        return self.__video

    def get_frame_url(self, n_frame):
        """
        This method return the url of the frame passed by arg

        :param n_frame: Number of the frame to generate Frame X Api url
        :type n_frame: int
        """

        return f"{self.video.url}frame/{n_frame}"

    def get_frame(self, n_frame):
        """
        This method request to Frame X Api the frame number n_frame

        Request to Frame X Api the frame number n_frame and return an Image of
        this frame

        :param n_frame: Number of the frame that will be requested
        :type n_frame: int
        :return: Reply from api with the raw data of the image
        :rtype: class:`BytesIO`
        """

        return requests.get(self.get_frame_url, stream=True).raw


class FrameXVideo:
    """
    Representate the video metadata returned by API

    :param kwargs: All metadata returned from api for any video
    """

    def __init__(self, **kwargs):

        self.name = None
        self.width = None
        self.height = None
        self.frames = None
        self.frame_rate = None
        self.url = None
        self.first_frame = None
        self.last_frame = None

        for prop in kwargs:
            setattr(self, prop, kwargs[prop])
