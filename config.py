import os
import subprocess

from libqtile import hook, layout, bar
from libqtile.config import Key, Match, DropDown, Group, ScratchPad, Screen, Click, Drag, KeyChord
from libqtile.lazy import lazy
from typing import List
from Xlib import display as xdisplay

from widgets import *
from preferences import dmscripts

from themes import float_layout, global_layout
import themes
import utils
import widgets
import apps

# You can import 'colorized' for alternating fonts or 'powerline' for
# powerline-like styling of widgets
from utils.widget_container import colorized as widget_container

@hook.subscribe.startup_once
def autostart():
    autostart_script = os.path.expanduser("~/.local/bin/auto-start.sh")
    subprocess.call([autostart_script])

auto_fullscreen            = True
bring_front_click          = "floating_only"
cursor_warp                = False
dgroups_app_rules          = []  # type: List
focus_on_window_activation = "smart"
follow_mouse_focus         = False
reconfigure_screens        = True
auto_minimize              = True

floating_layout = layout.Floating(
    float_rules=[
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        #  Defaults
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        #  Steam
        Match(wm_class="Steam", title="Friends List"),
        Match(wm_class="Steam", title="News"),
        Match(wm_class="Steam", title="Guard"),
        Match(wm_class="Steam", title="Screenshot Uploader"),
        # Match(wm_class='Steam', title='Self Updater'),
        #  Other
        Match(wm_class="Nitrogen"),
    ],
    **float_layout
)

groups = [

    Group(
        "internet",
        label="globe",
        matches=[
            Match(
                wm_class=[
                    "firefox",
                    "Tor Browser",
                    "Chromium",
                    "Google-chrome",
                    "Brave-browser",
                    "vivaldi-stable",
                    "qutebrowser",
                    "nyxt",
                ]
            )
        ],
    ),

    Group(
        "gaming",
        label="gamepad",
        layout="max",
        matches=[
            Match(
                wm_class=[
                    "Wine",
                    "dolphin-emu",
                    "Lutris",
                    "Citra",
                    "SuperTuxKart",
                    "Steam",
                    "battle.net.exe",
                ]
            ),
            Match(
                title=[
                    "Steam",
                    "Battle.net",
                ]
            ),
        ],
    ),

    Group(
        "coding",
        label="keyboard",
        # spawn=apps.myTerminal,
        matches=[
            Match(
                wm_class=[
                    # 'Alacritty',
                    # 'Terminator',
                    # 'URxvt',
                    # 'UXTerm',
                    # 'kitty',
                    # 'K3rmit',
                    # 'XTerm',
                    "Geany",
                    "Atom",
                    "Subl3",
                    "code-oss",
                    "Emacs",
                    "Oomox",
                    "Unity",
                    "UnityHub",
                    "jetbrains-studio",
                ]
            ),
        ],
    ),

    Group(
        "computer",
        label="folder",
        matches=[
            Match(
                wm_class=[
                    "dolphin",
                    "ark",
                    "Nemo",
                    "pcmanfm",
                    "File-roller",
                    "googledocs",
                    "keep",
                    "calendar",
                ]
            ),
        ],
    ),

    Group(
        "music",
        label="headphones",
        spawn=apps.myCliMusic,
        matches=[
            Match(
                wm_class=[
                    "Spotify",
                    "youtubemusic-nativefier-040164",
                ]
            ),
        ],
    ),

    Group(
        "graphics",
        label="camera",
        matches=[
            Match(
                wm_class=[
                    "Gimp-2.10",
                    "Gimp",
                    "Inkscape",
                    "Flowblade",
                    "digikam",
                ]
            ),
        ],
    ),

    Group(
        "chat",
        label="sms",
        matches=[
            Match(
                wm_class=[
                    "whatsapp-for-linux",
                    "Slack",
                    "discord",
                    "signal",
                ]
            ),
        ],
    ),

    Group(
        "sandbox",
        label="layer-group",
        matches=[
            Match(
                title=[
                    "Celluloid",
                ],
            ),
            Match(
                wm_class=[
                    "vlc",
                    "obs",
                    "kdenlive",
                ],
            ),
        ],
    ),

    Group(
        "monitor",
        label="chart-bar",
        layout="max",
        matches=[
            Match(
                wm_class=[
                    "virt-manager",
                    "VirtualBox Manager",
                    "VirtualBox Machine",
                    "Cypress",
                ]
            ),
        ],
    )]

s_width = 0.8
s_height = 0.8
s_left_margin = (1.0 - s_height) / 2
s_top_margin = (1.0 - s_height) / 2

# Add a ScratchPad Group
groups.append(
    ScratchPad(
        "NSP",
        [
            DropDown(
                "terminal",
                apps.myTerminal,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "htop",
                apps.myCliTaskManager,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "files",
                apps.myCliFiles,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "music",
                apps.myCliMusic,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "virtmanager",
                apps.myVirtManager,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "torrent",
                apps.myTorrent,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "calc",
                apps.myCalculator,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "whatsapp",
                apps.myWhatsApp,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "discord",
                apps.myDiscord,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "anki",
                apps.myAnki,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
                on_focus_lost_hide=False,
            ),
        ],
    ),
)

layouts = [ layout.MonadTall(**global_layout)
          , layout.Columns(**global_layout)
          , layout.Tile(**global_layout)
          # , layout.MonadWide(**global_layout)
          # , layout.Stack(num_stacks=2)
          # , layout.Matrix()
          # , layout.RatioTile()
          # , layout.TreeTab()
          # , layout.VerticalTile(**global_layout)
          # , layout.Zoomy()
          , layout.Bsp(**global_layout)
          , layout.Max(**global_layout) ]

def primary_bar():
    return [ widgets.general.separator(4)
           , widgets.general.start_widget()
           , widgets.general.separator(2)
           , widgets.general.prompt_widget()
           , widgets.general.chord()
           , widgets.general.separator(4)
           , widgets.general.time()
           , widgets.general.layout_icon()
           , widgets.general.group_box()
           , widgets.general.separator(20)
           , widgets.general.task_list()
           , widgets.general.keyboard_layout()
           , widgets.general.sys_tray()
           , widgets.general.separator(5)
           ,*widget_container(
                widgets=[ widgets.general.updater
                        , widgets.sensor.thermals
                        , widgets.sensor.network_graph
                        , widgets.general.volume
                        , widgets.general.date ])
           , widgets.general.profile()
    ]

def secondary_bar():
    return [ widgets.general.separator()
           , widgets.general.time()
           , widgets.general.layout_icon()
           , widgets.general.group_box()
           , widgets.general.separator(40)
           , widgets.general.task_list()
           ,*widget_container(
                widgets=[ widgets.sensor.nvidia_sensors
                        , widgets.sensor.cpu_graph
                        , widgets.sensor.memory_graph
                        , widgets.sensor.network_graph
                        , widgets.general.volume
                        , widgets.general.date ])
    ]

def init_bar(s="secondary"):
    if s == "primary": my_bar = primary_bar()
    elif s == "secondary": my_bar = secondary_bar()
    else: my_bar = secondary_bar()

    return bar.Bar( my_bar
                  , themes.bar_size
                  , background=themes.background
                  , opacity=themes.bar_opacity
    )

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors


num_monitors = get_num_monitors()

screens = [
    Screen(
        top=init_bar("primary"),
    )
]

if num_monitors > 1:
    for m in range(num_monitors - 1):
        screens.append(
            Screen(
                top=init_bar("secondary"),
            )
        )

mod   = "mod4"
shift = "shift"
ctrl  = "control"
alt   = "mod1"

keys = []
dm = os.path.expanduser(dmscripts)

keys.append(
    Key( [ mod, ctrl ] , "d" , lazy.hide_show_bar("all") , desc="Debugging" )
)

keys.extend([
    Key( [ mod, ctrl ] , "r" , lazy.restart()  , desc="Restart qTile" ),
    Key( [ mod, ctrl ] , "q" , lazy.shutdown() , desc="Quit qTile"    ),

    # Swith Keyboard Layouts
    Key( [ shift ] , "Alt_L" , lazy.spawn(dm + "dm-lang") , desc="Language Switching" ),

    # Changing UI
    KeyChord( [ mod ] , "t" , [
        Key([] , "z" , lazy.hide_show_bar("all")         , desc="Toggle Zen Mobde"   ),
        Key([] , "s" , lazy.hide_show_bar("all")         , desc="Toggle Statusbar"   ),
        Key([] , "k" , lazy.spawn(dm + "dm-keys toggle") , desc="Toggle Key Grabber" ),
    ], mode="Toggle"),
])

keys.extend([
    Key( [ mod        ] , "q"   , lazy.window.kill()              , desc="Close focused Window" ),
    Key( [ mod        ] , "F11" , lazy.window.toggle_fullscreen() , desc="Toggle Fullscreen"    ),
    Key( [ mod, shift ] , "f"   , lazy.window.toggle_fullscreen() , desc="Toggle Fullscreen"    ),
    Key( [ mod        ] , "m"   , lazy.window.toggle_maximize()   , desc="Toggle Maximize"      ),
    Key( [ mod        ] , "f"   , lazy.window.toggle_floating()   , desc="Toggle Floating"      ),

    Key( [ mod, alt ] , "m" ,
        lazy.window.toggle_minimize(),
        lazy.layout.down(),
        desc="Toggle Minimize"),
])

keys.extend([
    Key( [ mod        ] , "slash" , lazy.PLACEHOLDER         , desc="Switch navigation layer (Tiled vs Floating screens)" ),
    Key( [ alt        ] , "Tab"   , lazy.group.next_window() , desc="Move focus to next Window"                           ),
    Key( [ alt, shift ] , "Tab"   , lazy.group.prev_window() , desc="Move focus to prev Window"                           ),
    Key( [ mod        ] , "h"     , lazy.layout.left()       , desc="Move focus to left Window"                           ),
    Key( [ mod        ] , "l"     , lazy.layout.right()      , desc="Move focus to right Window"                          ),
    Key( [ mod        ] , "j"     , lazy.layout.down()       , desc="Move focus to below Window"                          ),
    Key( [ mod        ] , "k"     , lazy.layout.up()         , desc="Move focus to above Window"                          ),
])

keys.extend([
    Key( [ mod, shift ] , "h" , lazy.layout.shuffle_left()  , desc="Swap focused Window with the one to the left"  ),
    Key( [ mod, shift ] , "l" , lazy.layout.shuffle_right() , desc="Swap focused Window with the one to the right" ),
    Key( [ mod, shift ] , "j" , lazy.layout.shuffle_down()  , desc="Swap focused Window with the one below"        ),
    Key( [ mod, shift ] , "k" , lazy.layout.shuffle_up()    , desc="Swap focused Window with the one above"        ),
])

keys.extend([
    Key( [ mod, ctrl ] , "h" , lazy.layout.grow_left()  , desc="Grow focused Window left"  ),
    Key( [ mod, ctrl ] , "l" , lazy.layout.grow_right() , desc="Grow focused Window right" ),
    Key( [ mod, ctrl ] , "j" , lazy.layout.grow_down()  , desc="Grow focused Window down"  ),
    Key( [ mod, ctrl ] , "k" , lazy.layout.grow_up()    , desc="Grow focused Window up"    ),
])





keys.extend([
    Key( [ mod ] , "comma"  , lazy.prev_screen() , desc="Move focus to prev Screen" ),
    Key( [ mod ] , "period" , lazy.next_screen() , desc="Move focus to next Screen" ),
    Key( [ mod ] , "F1"     , lazy.to_screen(0)  , desc="Move focus to 1st Screen"  ),
    Key( [ mod ] , "F2"     , lazy.to_screen(1)  , desc="Move focus to 2nd Screen"  ),
])

keys.extend([
    Key( [ mod, shift ] , "comma"  , lazy.function(lambda qtile: qtile.current_window.cmd_toscreen(0)) , desc="Move window to Screen" ),
    Key( [ mod, shift ] , "period" , lazy.function(lambda qtile: qtile.current_window.cmd_toscreen(1)) , desc="Move window to Screen" ),
])



keys.extend([
    Key( [ mod ]        , "space" , lazy.next_layout()      , desc="Switch Laouts"            ),
    Key( [ mod, shift ] , "space" , lazy.prev_layout()      , desc="Switch Laouts"            ),
    Key( [ mod, alt ]   , "space" , lazy.to_layout_index(0) , desc="Switch to default Layout" ),
    Key( [ mod ]        , "equal" , lazy.layout.normalize() , desc="Reset all window sizes"   ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key( [ mod, shift ] , "Return" , lazy.layout.toggle_split() , desc="Toggle between split and unsplit sides of stack" ),
])

# Only map up to 10 Layouts to number keys
def getNumberOfKeysForLayouts():
    if len(layouts) > 10:
        return 10
    else:
        return len(layouts)

# Switch to another Layout with SUPER + ALT + #
for i in range(getNumberOfKeysForLayouts()):
    key = str(i + 1)
    if i + 1 == 10:
        key = "0"

    keys.append(Key([mod, alt], key, lazy.to_layout_index(i)))

# Switch to last Layout
keys.append(Key([mod, alt], "quoteleft", lazy.to_layout_index(len(layouts) - 1)))

keys.extend([
    Key( [ mod ] , "Tab" , lazy.screen.toggle_group()      , desc="Toggle Workspace" ),
    Key( [ mod ] , "F12" , lazy.group["coding"].toscreen(1), desc="meh"              ),

    KeyChord( [ mod ] , "g" , [
        Key( [] , "h" , lazy.screen.prev_group()                  , desc="Move to the group on the left"               ),
        Key( [] , "l" , lazy.screen.next_group()                  , desc="Move to the group on the right"              ),
        Key( [] , "d" , lazy.function(utils.clear_default_groups) , desc="Delete system 1-9 groups after a bad config" ),
    ], mode="Groups"),
])

# Only map up to 10 Groups to number keys
def getNumberOfKeysForGroups():
    if len(groups) > 10:
        return 10
    else:
        return len(groups)


# Switch to another Group with SUPER + #
# Send current window to another Group SUPER + SHIFT + #
for i in range(getNumberOfKeysForGroups()):
    name = groups[i].name

    key = str(i + 1)
    if i + 1 == 10:
        key = "0"

    keys.extend([
        Key( [ mod ]        , key , lazy.group[name].toscreen() ),
        Key( [ mod, shift ] , key , lazy.window.togroup(name)   )
    ])

keys.extend([
    Key( [ mod       ] , "quoteleft" , lazy.group["NSP"].dropdown_toggle("terminal") , desc="Terminal Scratchpad"     ) ,
    Key( [ mod       ] , "e"         , lazy.group["NSP"].dropdown_toggle("files"   ) , desc="File Manager Scratchpad" ) ,
    Key( [ ctrl, alt ] , "Delete"    , lazy.group["NSP"].dropdown_toggle("htop"    ) , desc="Htop Scratchpad"         ) ,

    KeyChord( [ mod ] , "s" , [
        Key( [] , "h" , lazy.group["NSP"].dropdown_toggle("htop"       ) , desc="Htop Scratchpad"        ) ,
        Key( [] , "m" , lazy.group["NSP"].dropdown_toggle("music"      ) , desc="Music Scratchpad"       ) ,
        Key( [] , "c" , lazy.group["NSP"].dropdown_toggle("calc"       ) , desc="Calculator Scratchpad"  ) ,
        Key( [] , "w" , lazy.group["NSP"].dropdown_toggle("whatsapp"   ) , desc="WhatsApp Scratchpad"    ) ,
        Key( [] , "d" , lazy.group["NSP"].dropdown_toggle("discord"    ) , desc="Discord Scratchpad"     ) ,
        Key( [] , "v" , lazy.group["NSP"].dropdown_toggle("virtmanager") , desc="VirtManager Scratchpad" ) ,
        Key( [] , "t" , lazy.group["NSP"].dropdown_toggle("torrent"    ) , desc="Torrent Scratchpad"     ) ,
        Key( [] , "a" , lazy.group["NSP"].dropdown_toggle("anki"       ) , desc="Anki Scratchpad"        ) ,
    ], mode="Scratchpads"),
])

keys.extend([
    Key( [      ] , "XF86AudioRaiseVolume" , lazy.spawn("amixer set Master 2%+ unmute") , desc="Increase System Volume" ),
    Key( [      ] , "XF86AudioLowerVolume" , lazy.spawn("amixer set Master 2%- unmute") , desc="Decrease System Volume" ),
    Key( [      ] , "XF86AudioMute"        , lazy.spawn("amixer set Master toggle"    ) , desc="Mute"                   ),
    Key( [ ctrl ] , "XF86AudioRaiseVolume" , lazy.spawn("mpc volume +2"               ) , desc="Increase Player Volume" ),
    Key( [ ctrl ] , "XF86AudioLowerVolume" , lazy.spawn("mpc volume -2"               ) , desc="Decrease Player Volume" ),
    Key( [      ] , "XF86AudioPrev"        , lazy.spawn("mpc prev"                    ) , desc="Prev Song"              ),
    Key( [      ] , "XF86AudioNext"        , lazy.spawn("mpc next"                    ) , desc="Next Song"              ),
    Key( [      ] , "XF86AudioPlay"        , lazy.spawn("mpc toggle"                  ) , desc="Play/Pause Music"       ),
    Key( [      ] , "XF86AudioStop"        , lazy.spawn("mpc stop"                    ) , desc="Stop Music"             ),
])

keys.extend([
    KeyChord( [ mod ] , "d" , [
        Key( [ mod ] , "d"         , lazy.spawn(dm + "dm-master"    ) , desc="DM Master"     ),
        Key( [     ] , "w"         , lazy.spawn(dm + "dm-wallpaper" ) , desc="DM Wallpaper"  ),
        Key( [     ] , "r"         , lazy.spawn(dm + "dm-record"    ) , desc="DM Record"     ),
        Key( [     ] , "p"         , lazy.spawn(dm + "dm-power"     ) , desc="DM Power"      ),
        Key( [     ] , "t"         , lazy.spawn(dm + "dm-theme"     ) , desc="DM Theme"      ),
        Key( [     ] , "s"         , lazy.spawn(dm + "dm-screenshot") , desc="DM Screenshot" ),
        Key( [     ] , "b"         , lazy.spawn(dm + "dm-bookman"   ) , desc="DM Bookman"    ),
        Key( [     ] , "n"         , lazy.spawn(dm + "dm-notify"    ) , desc="DM Notify"     ),
        Key( [     ] , "backslash" , lazy.spawn(dm + "dm-notify"    ) , desc="DM Notify"     ),
        Key( [     ] , "k"         , lazy.spawn(dm + "dm-keys"      ) , desc="DM Keys"       ),
    ], mode="dm-scripts"),
])

keys.extend([
    Key( [ alt ] , "F4" , lazy.spawn(dm + "dm-power") , desc="Logout Menu"),

    KeyChord( [ mod ] , "z" , [
        Key( [] , "z" , lazy.spawn(dm + "dm-power"         ) , desc="dm-power"          ),
        Key( [] , "l" , lazy.spawn(dm + "dm-power lock"    ) , desc="Lock Screen"       ),
        Key( [] , "s" , lazy.spawn(dm + "dm-power suspend" ) , desc="Suspend System"    ),
        Key( [] , "p" , lazy.spawn(dm + "dm-power poweroff") , desc="Shutdown System"   ),
        Key( [] , "r" , lazy.spawn(dm + "dm-power reboot"  ) , desc="Reboot System"     ),
        Key( [] , "w" , lazy.spawn(dm + "dm-power windows" ) , desc="Reboot to Windows" ),
    ], mode="(l)ock, (s)uspend, (p)oweroff, (r)eboot, (w)indows"),
])

keys.extend([
    Key( [            ] , "Print" , lazy.spawn(dm + "dm-screenshot screen") , desc="Fullscreen Screenshot"     ),
    Key( [ mod, shift ] , "Print" , lazy.spawn(dm + "dm-screenshot area"  ) , desc="Selection Area Screenshot" ),
    Key( [ alt        ] , "Print" , lazy.spawn(dm + "dm-screenshot window") , desc="Active Window Screenshot"  ),
    Key( [ mod        ] , "Print" , lazy.spawn(dm + "dm-screenshot full"  ) , desc="Full Desktop Screenshot"   ),
])

keys.extend([
    KeyChord( [ mod ] , "backslash" , [
        Key( [       ] , "backslash" , lazy.spawn(dm + "dm-notify recent" ) , desc="Show most recent Notifications" ),
        Key( [ mod   ] , "backslash" , lazy.spawn(dm + "dm-notify recent" ) , desc="Show most recent Notifications" ),
        Key( [ shift ] , "backslash" , lazy.spawn(dm + "dm-notify recents") , desc="Show few recent Notifications"  ),
        Key( [       ] , "r"         , lazy.spawn(dm + "dm-notify recents") , desc="Show few recent Notifications"  ),
        Key( [ shift ] , "c"         , lazy.spawn(dm + "dm-notify clear"  ) , desc="Clear all Notifications"        ),
        Key( [       ] , "c"         , lazy.spawn(dm + "dm-notify close"  ) , desc="Clear last Notification"        ),
        Key( [       ] , "a"         , lazy.spawn(dm + "dm-notify context") , desc="Open last Notification"         ),
    ], mode="Notifications"),
])

keys.extend([
    Key( [ ctrl, alt  ] , "t"      , lazy.spawn(apps.myTerminal        ) , desc="Launch Terminal"                      ),
    Key( [ mod        ] , "Return" , lazy.spawn(apps.myTerminal        ) , desc="Launch Terminal"                      ),
    Key( [ mod        ] , "c"      , lazy.spawn(apps.myIde             ) , desc="Launch IDE"                           ),
    Key( [ mod        ] , "b"      , lazy.spawn(apps.myWebBrowser      ) , desc="Launch Web Browser"                   ),
    Key( [ mod        ] , "i"      , lazy.spawn(apps.myIncBrowser) , desc="Launch Web Browser in Incognito Mode" ),
    Key( [ mod        ] , "p"      , lazy.spawn(apps.myPassManager ) , desc="Autofill Passwords"                   ),
    Key( [ mod        ] , "r"      , lazy.spawn(apps.myLauncher        ) , desc="Launch Launcher"                      ),
    Key( [ mod, shift ] , "r"      , lazy.spawn("dmenu_run"            ) , desc="Launch dmenu"                         ),

    # Primary
    KeyChord( [ mod ] , "o" , [
        Key( [] , "t" , lazy.spawn(apps.myTorBrowser ) , desc="Launch Tor Browser"  ),
        Key( [] , "s" , lazy.spawn(apps.mySteam       ) , desc="Launch Steam"        ),
    ], mode="Open Primary"),

    # Secondary
    KeyChord( [ ctrl, alt ] , "o" , [
        Key( [] , "t" , lazy.spawn(apps.myCliText  ) , desc="Launch Text Editor"   ),
        Key( [] , "p" , lazy.spawn(apps.myPicLibrary) , desc="Launch Photo Library" ),
        Key( [] , "g" , lazy.spawn(apps.myImgEditor ) , desc="Launch Image Editor"  ),
        Key( [] , "r" , lazy.spawn(apps.myVctEditor) , desc="Launch Vector Editor" ),
        Key( [] , "v" , lazy.spawn(apps.myVidEditor ) , desc="Launch Video Editor"  ),
    ], mode="Open Secondary"),
])

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
