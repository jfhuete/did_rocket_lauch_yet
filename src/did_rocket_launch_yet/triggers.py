from bernard import layers as lyr
from bernard.engine.triggers import Text

from did_rocket_launch_yet.store import cs
from did_rocket_launch_yet.analyzer import FrameXAnalyzer


class Afirmation(Text):
    """
    This trigger interpret the user reply as yes or no, but also detect if the
    frame is found in order to pass to final state

    :param request: Request provided by bernard
    :type request: class `bernard.engine.request.Request`
    :param user_reply: User reply if the roacket is launched or not
    :type user_reply: str
    :param is_found: If the frame when the rocket is launched is found this
                     param is true
    :type is_found: bool
    """

    def __init__(self, request, intent, is_found):
        super().__init__(request, intent)
        self.is_found = is_found

    # noinspection PyMethodOverriding
    @cs.inject()
    async def rank(self, context) -> float:

        if "frame_analyzer" not in context:
            return .0

        analyzer = FrameXAnalyzer(**context["frame_analyzer"])

        try:
            user_reply = self.request.get_layer(lyr.RawText).text
        except (KeyError, ValueError, TypeError):
            return .0

        is_launched = user_reply == "Yes"
        analyzer.get_next_frame(is_launched=is_launched)
        context["frame_analyzer"] = analyzer.instance_data

        found_condition = self.is_found == analyzer.frame_found
        intent_condition = await super().rank() == 1.

        return 1. if (found_condition and intent_condition) else .0
