# coding: utf-8

from bernard.engine import Tr, triggers as trg
from bernard.i18n import intents as its

from did_rocket_launch_yet.states import (
    Welcome, FirstFrame, RocketLaunched, RocketNotLaunched, LauchFound
)


transitions = [
    Tr(
        dest=Welcome,
        factory=trg.Text.builder(its.HELLO),
    ),
    Tr(
        dest=FirstFrame,
        origin=Welcome,
        factory=trg.Text.builder(its.START),
    ),
    Tr(
        dest=RocketNotLaunched,
        origin=FirstFrame,
        factory=trg.Text.builder(its.NO),
    ),
    Tr(
        dest=RocketNotLaunched,
        origin=RocketNotLaunched,
        factory=trg.Text.builder(its.NO),
    ),
    Tr(
        dest=RocketNotLaunched,
        origin=RocketLaunched,
        factory=trg.Text.builder(its.NO),
    ),
    Tr(
        dest=RocketLaunched,
        origin=FirstFrame,
        factory=trg.Text.builder(its.YES),
    ),
    Tr(
        dest=RocketLaunched,
        origin=RocketNotLaunched,
        factory=trg.Text.builder(its.YES),
    ),
    Tr(
        dest=RocketLaunched,
        origin=RocketLaunched,
        factory=trg.Text.builder(its.YES),
    ),
    Tr(
        dest=Welcome,
        origin=LauchFound,
        factory=trg.Text.builder(its.RESTART),
    ),
]
