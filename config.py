from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import socket
import subprocess

from bindings import mouse

#  Key modifiers
mod = "mod4"
alt = "mod1"
ctrl = "control"
shift = "shift"

terminal = guess_terminal()
text_editor = 'xed'
web_browser = 'chromium'
tor_browser = 'torbrowser-launcher'
incognito_browser = 'chromium --incognito'
file_manager = 'nemo'
music_player = 'youtubemusic-nativefier'
video_player = 'celluloid'
game = '/usr/bin/steam-runtime %U'
ide = 'code'
graphics_editor = 'gimp'
vector_editor = 'inkscape'
video_editor = 'kdenlive'
photos_library = 'digikam'
torrent_client = 'transmission-qt'
vpn = '/opt/piavpn/bin/pia-client --quiet'
vm = 'virtualbox'

network_manager = 'nm-connection-editor'
bluetooth_manager = 'blueman-manager'
power_manager = 'xfce4-power-manager-settings'
audio_manager = 'cinnamon-settings sound'
package_manager = 'pamac-manager'
lock = 'cinnamon-screensaver-command -l'

keys = [
    # System Control
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    #  Switch focus between monitors
    Key([mod], "period", lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(),
        desc='Move focus to prev monitor'),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, shift], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, shift], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, shift], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, ctrl], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, ctrl], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, ctrl], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, shift], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle windows states
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle maximize'),
    Key([mod], "w",
        lazy.window.toggle_floating(),
        desc='toggle floating'),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'),

    # Main Applications launched with SUPER + KEY
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch file manager"),
    Key([mod], "b", lazy.spawn(web_browser), desc="Launch web browser"),
    Key([mod], "i", lazy.spawn(incognito_browser),
        desc="Launch incognito browser"),
    #  desc="Launch web browser in incognito mode"),
    Key([mod], "t", lazy.spawn(tor_browser), desc="Launch tor browser"),
    Key([mod], "c", lazy.spawn(ide), desc="Launch IDE"),


    # Secondary Applications launched with CTRL + ALT + KEY
    Key([ctrl, alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([ctrl, alt], "m", lazy.spawn(music_player), desc="Launch music player"),
    Key([ctrl, alt], "p", lazy.spawn(photos_library),
        desc="Launch photos library"),
    Key([ctrl, alt], "v", lazy.spawn(video_player), desc="Launch video player"),
    Key([ctrl, alt], "g", lazy.spawn(graphics_editor),
        desc="Launch graphics editor"),
    Key([ctrl, alt], "s", lazy.spawn(game), desc="Launch Steam"),


]

group_names = [("Web", {'layout': 'columns'}),
               ("Game", {'layout': 'columns'}),
               ("Dev", {'layout': 'columns'}),
               ("PC", {'layout': 'columns'}),
               ("Mus", {'layout': 'columns'}),
               ("Vid", {'layout': 'columns'}),
               ("Misc", {'layout': 'columns'}),
               ("Gfx", {'layout': 'columns'}),
               ("Vbox", {'layout': 'columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group with SUPER + #
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group SUPER + SHIFT + #
    keys.append(Key([mod, "shift"], str(
        i), lazy.window.togroup(name, switch_group=False)))

layout_theme = {"border_width": 3,
                "margin": 4,
                "border_focus_stack": '#d75f5f'
                }

layouts = [
    layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(),
    #  layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #  layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#282c34", "#282c34"],  # panel background
          ["#434758", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"],  # color for the even widgets
          ["#e1acff", "#e1acff"]]  # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# Default widget settings
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def arch_logo():
    return widget.Image(
        filename="/usr/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg",
        use_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('chromium')}
    )


def init_panel_widgets():
    panel_widgets = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        arch_logo(),
        widget.Clock(
            foreground=colors[2],
            background=colors[0],
            format='%l:%M %p'
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=11,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[2],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[3],
            this_screen_border=colors[3],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors[3],
            background=colors[1]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),



        widget.TextBox(
            text='',
            background=colors[0],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=colors[2],
            background=colors[4],
            fontsize=11
        ),
        widget.ThermalSensor(
            foreground=colors[2],
            background=colors[4],
            threshold=90,
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" 🖬",
            foreground=colors[2],
            background=colors[5],
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.Net(
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors[2],
            background=colors[5],
            padding=0
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.Clock(
            foreground=colors[2],
            background=colors[5],
            format='%a %d %b %Y'
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[5]
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.QuickExit(
            foreground=colors[2],
            background=colors[4]
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
    ]
    return panel_widgets


screens = [
    Screen(
        top=bar.Bar(init_panel_widgets(), 24, background=colors[0]),
    ),
    Screen(top=bar.Bar(init_panel_widgets(), 24, background=colors[0])),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

# Run the utility of `xprop` to see the wm class and name of an X client.
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notofication'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"


@ hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
