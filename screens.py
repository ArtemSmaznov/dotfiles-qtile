from libqtile.config import Screen

import bars

screens = [
    Screen(
        top=bars.init_bar(),
    ),
    Screen(
        top=bars.init_bar('side'),
    ),
]
