def clear_default_groups(qtile):
    for i in range(10):
        qtile.cmd_delgroup(str(i + 1))
