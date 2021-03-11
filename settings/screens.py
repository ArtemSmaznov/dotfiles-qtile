from libqtile.config import Screen

import lib.bars as bar

screens = [
    Screen(
        top=bar.init_bar(),
    ),
    Screen(
        top=bar.init_bar('side'),
    ),
]
