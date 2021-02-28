from bernard.conf import settings
from did_rocket_launch_yet.analyzer.api import FrameXApi


class FrameXAnalyzer:
    """
    Provide a Frame from rocket launching to be delivered to user

    This class consume The FrameX API and handle the user request to find the
    exact moment when the rocket is launched

    :param first_frame: First frame pointer, default None
    :type first_frame: int, optional
    :param last_frame: Last frame pointer, default None
    :type last_frame: int, optional
    :param actual_frame: Actual frame pointer, default None
    :type actual_frame: int, optional
    """

    def __init__(self, first_frame=None, last_frame=None, actual_frame=None):

        self.api = FrameXApi(video_name=settings.FRAMEX_VIDEO_NAME)

        if last_frame is None:
            self.last_frame = api.video.frames - 1
        else:
            self.last_frame = last_frame
        self.first_frame = 0 if first_frame is None else first_frame
        self.actual_frame = self.__calculate_middle_frame()

    def get_next_frame(self, is_launched):
        """
        Return the next frame to deliver to user

        According of the user answer this method return the next frame. If the
        answer of is_launched is yes, next frame will be

        :param is_launched: Indicate if th rocket is launched to calculate the
                            new limits. True indicate launched, False indicate
                            not launched
        :param is_launched: bool
        :return: Next frame to display to user or None if don't have more
                 frames between last_frame and first_frame (Found rocket
                 launching)
        :rtype: None if frame found else :py:class:`~PIL.Image.Image` object.
        """

        self.last_frame = self.actual_frame if is_launched else self.last_frame
        self.first_frame = self.actual_frame \
            if not is_launched else self.first_frame
        self.actual_frame = self.__calculate_middle_frame()

        return self.api.get_frame_url(self.actual_frame) \
             if not self.frame_found else None

    @property
    def frame_found(self):
        """
        Indicate if the searched frame is found

        The condition for frame found is that actual frame equal of first frame
        or last frame
        """

        return self.actual_frame in [self.last_frame, self.first_frame] or \
            abs(self.last_frame - self.first_frame) == 2

    @property
    def instance_data(self):
        """
        Return a dict with necessary data to recover the state of this class
        """

        return {
            "actual_frame": self.actual_frame,
            "last_frame": self.last_frame,
            "first_frame": self.first_frame
        }

    def __calculate_middle_frame(self):
        """
        This method return the middle frame between first_frame and last_frame

        :return: Frame in the middle of first_frame and last_frame rounded
        :rtype: int
        """

        return round((self.first_frame + self.last_frame) / 2)
