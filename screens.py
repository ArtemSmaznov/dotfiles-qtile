from libqtile.config import Screen
import bar

screens = [
    Screen(
        top=bar.init_bar()
    ),
    Screen(
        top=bar.init_bar()
    ),
]
