# coding: utf-8
from bernard import layers as lyr
from bernard.platforms.telegram.layers import ReplyKeyboard, KeyboardButton
from bernard.analytics import page_view
from bernard.engine import BaseState
from bernard.i18n import translate as t

from did_rocket_launch_yet.store import cs
from did_rocket_launch_yet.analyzer import FrameXAnalyzer


class DidRocketLaunchYetState(BaseState):
    """
    Root class for Did Rocket Launch Yet.

    Here you must implement "error" and "confused" to suit your needs. They
    are the default functions called when something goes wrong. The ERROR and
    CONFUSED texts are defined in `i18n/en/responses.csv`.
    """

    @page_view('/bot/error')
    async def error(self) -> None:
        """
        This happens when something goes wrong (it's the equivalent of the
        HTTP error 500).
        """

        self.send(lyr.Text(t.ERROR))

    @page_view('/bot/confused')
    async def confused(self) -> None:
        """
        This is called when the user sends a message that triggers no
        transitions.
        """

        self.send(lyr.Text(t.CONFUSED))

    async def handle(self) -> None:
        raise NotImplementedError


class Welcome(DidRocketLaunchYetState):
    """
    Welcome state say hello and invite to play
    """

    @page_view('/bot/welcome')
    async def handle(self):

        name = await self.request.user.get_friendly_name()

        self.send(
            lyr.Text(t('WELCOME', name=name)),
            ReplyKeyboard(
                keyboard=[
                    [KeyboardButton(t.START)],
                ]
            )
        )


class FirstFrame(DidRocketLaunchYetState):
    """
    In this state the firts frame will be showed
    """

    @page_view('/bot/firtsframe')
    @cs.inject()
    async def handle(self, context):
        analyzer = FrameXAnalyzer()
        self.send(
            lyr.Text(t('QUESTION', frame=analyzer.actual_frame)),
            ReplyKeyboard(
                keyboard=[
                    [KeyboardButton(t.YES), KeyboardButton(t.NO)],
                ]
            )
        )
        context['frame_analyzer'] = analyzer.instance_data


class RocketNotLaunched(DidRocketLaunchYetState):
    """
    This state search a new frame from actual_frame to last_frame
    """

    @page_view('/bot/rocketnotlaunched')
    @cs.inject()
    async def handle(self, context):
        analyzer = FrameXAnalyzer(**context['frame_analyzer'])

        analyzer.get_next_frame(is_launched=False)

        self.send(
            lyr.Text(t('QUESTION', frame=analyzer.actual_frame)),
            ReplyKeyboard(
                keyboard=[
                    [KeyboardButton(t.YES), KeyboardButton(t.NO)],
                ]
            )
        )

        context['frame_analyzer'] = analyzer.instance_data


class RocketLaunched(DidRocketLaunchYetState):
    """
    This state search a new frame from first_frame to actual_frame
    """

    @page_view('/bot/rocketlaunched')
    @cs.inject()
    async def handle(self, context):
        analyzer = FrameXAnalyzer(**context['frame_analyzer'])

        analyzer.get_next_frame(is_launched=True)

        self.send(
            lyr.Text(t('QUESTION', frame=analyzer.actual_frame)),
            ReplyKeyboard(
                keyboard=[
                    [KeyboardButton(t.YES), KeyboardButton(t.NO)],
                ]
            )
        )

        context['frame_analyzer'] = analyzer.instance_data


class LauchFound(DidRocketLaunchYetState):
    """
    In this state the exact time when the rocket is launched is found
    """

    @page_view('/bot/launchfound')
    @cs.inject()
    async def handle(self, context):
        analyzer = FrameXAnalyzer(**context['frame_analyzer'])

        self.send(
            lyr.Text(t('FOUND', frame=analyzer.actual_frame)),
            ReplyKeyboard(
                keyboard=[
                    [KeyboardButton(t.RESTART)],
                ]
            )
        )