# coding: utf-8

from bernard.engine import Tr, triggers as trg
from bernard.i18n import intents as its

from did_rocket_launch_yet.states import Welcome, FirstFrame

transitions = [
    Tr(
        dest=Welcome,
        factory=trg.Text.builder(its.HELLO),
    ),
]
