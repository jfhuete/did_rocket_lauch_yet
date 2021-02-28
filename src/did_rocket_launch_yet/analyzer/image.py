from PIL import Image
from bernard.conf import settings
from did_rocket_launch_yet.analyzer.api import FrameXApi


class FrameXImage:
    """
    This class is an abstraction for Image of the video

    You can to create an FrameXImage only with the number of the video
    frame. This class request from FrameXApi this frame, and create and process
    an image
    """

    DISPLAY_SIZE = (675, 405)

    def __init__(self):
        self.api = FrameXApi(video_name=settings.FRAMEX_VIDEO_NAME)

    def get_image(self, n_frame):
        """
        This method return the number of frame n_frame from the video

        Request from Frame X Api the frame correspond with n_frame and parse
        the raw data obtained for return an Image that can be send to user

        :param n_frame: Number of the frame requested
        :type n_frame: int
        :return: Image processed and ready to send to user
        :rtype: :py:class:`~PIL.Image.Image`
        """

        image = Image.open(self.api.get_frame(n_frame))
        image.thumbnail(FrameXImage.DISPLAY_SIZE)

        return image
