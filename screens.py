from libqtile.config import Screen
from bar import init_bar

screens = [
    Screen(
        top=init_bar()
    ),
    Screen(
        top=init_bar()
    ),
]
