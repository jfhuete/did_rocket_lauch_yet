# coding: utf-8

from bernard.engine import Tr, triggers as trg
from bernard.i18n import intents as its

from src.did_rocket_launch_yet.states import (
    Welcome, FirstFrame, RocketLaunched, RocketNotLaunched, LauchFound
)
from src.did_rocket_launch_yet.triggers import Afirmation


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
        factory=Afirmation.builder(its.NO, is_found=False),
    ),
    Tr(
        dest=RocketNotLaunched,
        origin=RocketNotLaunched,
        factory=Afirmation.builder(its.NO, is_found=False),
    ),
    Tr(
        dest=RocketNotLaunched,
        origin=RocketLaunched,
        factory=Afirmation.builder(its.NO, is_found=False),
    ),
    Tr(
        dest=RocketLaunched,
        origin=FirstFrame,
        factory=Afirmation.builder(its.YES, is_found=False),
    ),
    Tr(
        dest=RocketLaunched,
        origin=RocketNotLaunched,
        factory=Afirmation.builder(its.YES, is_found=False),
    ),
    Tr(
        dest=RocketLaunched,
        origin=RocketLaunched,
        factory=Afirmation.builder(its.YES, is_found=False),
    ),
    Tr(
        dest=LauchFound,
        origin=RocketLaunched,
        factory=Afirmation.builder(its.YES, is_found=True),
    ),
    Tr(
        dest=LauchFound,
        origin=RocketNotLaunched,
        factory=Afirmation.builder(its.YES, is_found=True),
    ),
    Tr(
        dest=LauchFound,
        origin=RocketLaunched,
        factory=Afirmation.builder(its.NO, is_found=True),
    ),
    Tr(
        dest=LauchFound,
        origin=RocketNotLaunched,
        factory=Afirmation.builder(its.NO, is_found=True),
    ),
    Tr(
        dest=FirstFrame,
        origin=LauchFound,
        factory=trg.Text.builder(its.RESTART),
    ),
]
