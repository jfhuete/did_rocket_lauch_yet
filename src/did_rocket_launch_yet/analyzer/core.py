from bernard.conf import settings
from did_rocket_launch_yet.analyzer.api import FrameXApi


class FrameXAnalyzer:
    """
    Provide a Frame from rocket launching to be delivered to user

    This class consume The FrameX API and handle the user request to find the
    exact moment when the rocket is launched
    """

    def __init__(self):
        self.api = FrameXApi(video_name=settings.FRAMEX_VIDEO_NAME)
        self.video_properties = self.api.video_properties
        self.__actual_frame = None
        self.image = None
        self.last_frame = self.video_properties['frames'] - 1
        self.firts_frame = 0
        self.actual_frame = self.__calculate_middle_frame()

    @property
    def actual_frame(self):
        """
        Return the private actual_frame attribute
        """

        return self.__actual_frame

    @actual_frame.setter
    def actual_frame(self, frame):
        """
        Set private attribute actual_frame number and download this frame

        :param frame: Number of the actual frame
        :type frame: int
        """

        self.__actual_frame = frame

        return self.__actual_frame

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

        return self.image if not self.frame_found else None

    @property
    def frame_found(self):
        """
        Indicate if the searched frame is found

        The condition for frame found is that actual frame equal of first frame
        or last frame
        """

        return self.actual_frame in [self.last_frame, self.firts_frame]

    def __calculate_middle_frame(self):
        """
        This method return the middle frame between first_frame and last_frame

        :return: Frame in the middle of first_frame and last_frame rounded
        :rtype: int
        """

        return round((self.firts_frame + self.last_frame) / 2)