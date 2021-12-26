import preferences as user

def clear_default_groups(qtile):
    for i in range(10):
        qtile.cmd_delgroup(str(i + 1))

def volume_increase(qtile):
    qtile.cmd_spawn("amixer -q sset Master on " + str(user.volume_step) + "%+")

def volume_decrease(qtile):
    qtile.cmd_spawn("amixer -q sset Master on " + str(user.volume_step) + "%-")

def volume_mute(qtile):
    qtile.cmd_spawn("amixer -q sset Master toggle")
