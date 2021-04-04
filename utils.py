from datetime import datetime as time

from libqtile import widget

import lib.widgets as my_widget
import settings.preferences as user
import theme.default as theme

kbr_index = 0


def switch_keyboard_layout(qtile):
    global kbr_index

    if kbr_index+1 < len(user.languages):
        kbr_index = kbr_index + 1
    else:
        kbr_index = 0
    qtile.cmd_spawn('setxkbmap ' + user.languages[kbr_index])


# ░█░█░█▀█░█░░░█░█░█▄█░█▀▀
# ░▀▄▀░█░█░█░░░█░█░█░█░█▀▀
# ░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀

def volume_increase(qtile):
    qtile.cmd_spawn('amixer -q sset Master on ' + str(user.volume_step) + '%+')


def volume_decrease(qtile):
    qtile.cmd_spawn('amixer -q sset Master on ' + str(user.volume_step) + '%-')


def volume_mute(qtile):
    qtile.cmd_spawn('amixer -q sset Master toggle')
