import os
import subprocess

from libqtile import bar, hook, layout
from libqtile.config import (DropDown, EzClick, EzDrag, EzKey, Group, KeyChord,
                             Match, ScratchPad, Screen)
from libqtile.lazy import lazy
from Xlib import display as xdisplay

import apps
import themes
import utils
import widgets
from themes import float_layout, global_layout

# You can import 'colorized' for alternating fonts or 'powerline' for
# powerline-like styling of widgets
from utils.widget_container import colorized as widget_container

auto_fullscreen            = True
bring_front_click          = "floating_only"
cursor_warp                = False
dgroups_app_rules          = []  # type: List
focus_on_window_activation = "smart"
follow_mouse_focus         = False
reconfigure_screens        = True
auto_minimize              = True

myScript   = os.path.expanduser("~/.local/bin/")
myDMScript = os.path.expanduser("~/.local/bin/dm-scripts/")

@hook.subscribe.startup_once
def autostart():
    autostart_script = os.path.expanduser("~/.local/bin/auto-start.sh")
    subprocess.call([autostart_script])

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
        spawn=apps.myCliSysMonitor,
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
                apps.myCliSysTasks,
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
           , widgets.general.group_box()
           , widgets.general.separator(4)
           , widgets.general.layout_icon()
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
           , widgets.general.start_widget()
           , widgets.general.time()
           , widgets.general.group_box()
           , widgets.general.separator(4)
           , widgets.general.layout_icon()
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

keys.append(
    EzKey( "M-C-d" , lazy.hide_show_bar("all") , desc="Debugging" )
)

keys.extend([
    EzKey( "M-C-S-r" , lazy.restart()       , desc="Restart qTile"       ),
    EzKey( "M-C-r"   , lazy.reload_config() , desc="Reload qTile Config" ),
    EzKey( "M-C-q"   , lazy.shutdown()      , desc="Quit qTile"          ),

    # Swith Keyboard Layouts
    EzKey( "S-<Alt_L>" , lazy.spawn(myDMScript + "dm-lang") , desc="Language Switching" ),

    # Changing UI
    KeyChord( [ mod ] , "t" , [
        EzKey( "z" , lazy.hide_show_bar("all")                 , desc="Toggle Zen Mobde"   ),
        EzKey( "s" , lazy.hide_show_bar("all")                 , desc="Toggle Statusbar"   ),
        EzKey( "k" , lazy.spawn(myDMScript + "dm-keys toggle") , desc="Toggle Key Grabber" ),
    ], name="Toggle"),
])

keys.extend([
    EzKey( "M-q"     , lazy.window.kill()              , desc="Close focused Window" ),
    EzKey( "M-<F11>" , lazy.window.toggle_fullscreen() , desc="Toggle Fullscreen"    ),
    EzKey( "M-S-f"   , lazy.window.toggle_fullscreen() , desc="Toggle Fullscreen"    ),
    EzKey( "M-m"     , lazy.window.toggle_maximize()   , desc="Toggle Maximize"      ),
    EzKey( "M-f"     , lazy.window.toggle_floating()   , desc="Toggle Floating"      ),

    EzKey( "M-A-m" ,
        lazy.window.toggle_minimize(),
        lazy.layout.down(),
        desc="Toggle Minimize"),
])

keys.extend([
    EzKey( "M-<Slash>" , lazy.PLACEHOLDER         , desc="Switch navigation layer (Tiled vs Floating screens)" ),
    EzKey( "A-<Tab>"   , lazy.group.next_window() , desc="Move focus to next Window"                           ),
    EzKey( "A-S-<Tab>" , lazy.group.prev_window() , desc="Move focus to prev Window"                           ),
    EzKey( "M-h"       , lazy.layout.left()       , desc="Move focus to left Window"                           ),
    EzKey( "M-l"       , lazy.layout.right()      , desc="Move focus to right Window"                          ),
    EzKey( "M-j"       , lazy.layout.down()       , desc="Move focus to below Window"                          ),
    EzKey( "M-k"       , lazy.layout.up()         , desc="Move focus to above Window"                          ),
])

keys.extend([
    EzKey( "M-S-h" , lazy.layout.shuffle_left()  , desc="Swap focused Window with the one to the left"  ),
    EzKey( "M-S-l" , lazy.layout.shuffle_right() , desc="Swap focused Window with the one to the right" ),
    EzKey( "M-S-j" , lazy.layout.shuffle_down()  , desc="Swap focused Window with the one below"        ),
    EzKey( "M-S-k" , lazy.layout.shuffle_up()    , desc="Swap focused Window with the one above"        ),
])

keys.extend([
    EzKey( "M-C-h" , lazy.layout.grow_left()  , desc="Grow focused Window left"  ),
    EzKey( "M-C-l" , lazy.layout.grow_right() , desc="Grow focused Window right" ),
    EzKey( "M-C-j" , lazy.layout.grow_down()  , desc="Grow focused Window down"  ),
    EzKey( "M-C-k" , lazy.layout.grow_up()    , desc="Grow focused Window up"    ),
])





keys.extend([
    EzKey( "M-<Comma>"  , lazy.prev_screen() , desc="Move focus to prev Screen" ),
    EzKey( "M-<Period>" , lazy.next_screen() , desc="Move focus to next Screen" ),
    EzKey( "M-<F1>"     , lazy.to_screen(0)  , desc="Move focus to 1st Screen"  ),
    EzKey( "M-<F2>"     , lazy.to_screen(1)  , desc="Move focus to 2nd Screen"  ),
])

keys.extend([
    EzKey( "M-S-<Comma>"  , lazy.function(lambda qtile: qtile.current_window.cmd_toscreen(0)) , desc="Move window to Screen" ),
    EzKey( "M-S-<Period>" , lazy.function(lambda qtile: qtile.current_window.cmd_toscreen(1)) , desc="Move window to Screen" ),
])



keys.extend([
    EzKey( "M-<Space>" , lazy.next_layout()      , desc="Switch Laouts"            ),
    EzKey( "M-S-<Space>" , lazy.prev_layout()      , desc="Switch Laouts"            ),
    EzKey( "M-A-<Space>" , lazy.to_layout_index(0) , desc="Switch to default Layout" ),
    EzKey( "M-<Equal>" , lazy.layout.normalize() , desc="Reset all window sizes"   ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    EzKey( "M-S-<Return>" , lazy.layout.toggle_split() , desc="Toggle between split and unsplit sides of stack" ),
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

    keys.append(
        EzKey( f"M-A-{key}", lazy.to_layout_index(i))
    )

# Switch to last Layout
keys.append(
    EzKey( "M-A-<Quoteleft>", lazy.to_layout_index(len(layouts) - 1))
)

keys.extend([
    EzKey( "M-<Tab>" , lazy.screen.toggle_group()       , desc="Toggle Workspace" ),
    EzKey( "M-<F12>" , lazy.group["coding"].toscreen(1) , desc="meh"              ),

    KeyChord( [ mod ] , "g" , [
        EzKey( "h" , lazy.screen.prev_group()                  , desc="Move to the group on the left"               ),
        EzKey( "l" , lazy.screen.next_group()                  , desc="Move to the group on the right"              ),
        EzKey( "d" , lazy.function(utils.clear_default_groups) , desc="Delete system 1-9 groups after a bad config" ),
    ], name="Groups"),
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
        EzKey( f"M-{key}"   , lazy.group[name].toscreen() ),
        EzKey( f"M-S-{key}" , lazy.window.togroup(name)   )
    ])

keys.extend([
    EzKey( "M-<Quoteleft>" , lazy.group["NSP"].dropdown_toggle("terminal") , desc="Terminal Scratchpad"     ) ,
    EzKey( "M-e"           , lazy.group["NSP"].dropdown_toggle("files"   ) , desc="File Manager Scratchpad" ) ,
    EzKey( "C-A-<Delete>"  , lazy.group["NSP"].dropdown_toggle("htop"    ) , desc="Htop Scratchpad"         ) ,

    KeyChord( [ mod ] , "s" , [
        EzKey( "a" , lazy.group["NSP"].dropdown_toggle("anki"       ) , desc="Anki Scratchpad"        ) ,
        EzKey( "c" , lazy.group["NSP"].dropdown_toggle("calc"       ) , desc="Calculator Scratchpad"  ) ,
        EzKey( "d" , lazy.group["NSP"].dropdown_toggle("discord"    ) , desc="Discord Scratchpad"     ) ,
        EzKey( "h" , lazy.group["NSP"].dropdown_toggle("htop"       ) , desc="Htop Scratchpad"        ) ,
        EzKey( "m" , lazy.group["NSP"].dropdown_toggle("music"      ) , desc="Music Scratchpad"       ) ,
        EzKey( "t" , lazy.group["NSP"].dropdown_toggle("torrent"    ) , desc="Torrent Scratchpad"     ) ,
        EzKey( "v" , lazy.group["NSP"].dropdown_toggle("virtmanager") , desc="VirtManager Scratchpad" ) ,
        EzKey( "w" , lazy.group["NSP"].dropdown_toggle("whatsapp"   ) , desc="WhatsApp Scratchpad"    ) ,
    ], name="Scratchpads"),
])

keys.extend([
    EzKey( "<XF86AudioRaiseVolume>"   , lazy.spawn(myScript + "set-volume.sh + 2") , desc="Increase System Volume" ),
    EzKey( "<XF86AudioLowerVolume>"   , lazy.spawn(myScript + "set-volume.sh - 2") , desc="Decrease System Volume" ),
    EzKey( "<XF86AudioMute>"          , lazy.spawn(myScript + "toggle-mute.sh"   ) , desc="Mute"                   ),
    EzKey( "C-<XF86AudioRaiseVolume>" , lazy.spawn("mpc volume +2"               ) , desc="Increase Player Volume" ),
    EzKey( "C-<XF86AudioLowerVolume>" , lazy.spawn("mpc volume -2"               ) , desc="Decrease Player Volume" ),
    EzKey( "<XF86AudioPrev>"          , lazy.spawn("mpc prev"                    ) , desc="Prev Song"              ),
    EzKey( "<XF86AudioNext>"          , lazy.spawn("mpc next"                    ) , desc="Next Song"              ),
    EzKey( "<XF86AudioPlay>"          , lazy.spawn("mpc toggle"                  ) , desc="Play/Pause Music"       ),
    EzKey( "<XF86AudioStop>"          , lazy.spawn("mpc stop"                    ) , desc="Stop Music"             ),
])

keys.extend([
    KeyChord( [ mod ] , "d" , [
        EzKey( "M-d"         , lazy.spawn(myDMScript + "dm-master"    ) , desc="DM Master"     ),
        EzKey( "w"           , lazy.spawn(myDMScript + "dm-wallpaper" ) , desc="DM Wallpaper"  ),
        EzKey( "r"           , lazy.spawn(myDMScript + "dm-record"    ) , desc="DM Record"     ),
        EzKey( "p"           , lazy.spawn(myDMScript + "dm-power"     ) , desc="DM Power"      ),
        EzKey( "t"           , lazy.spawn(myDMScript + "dm-theme"     ) , desc="DM Theme"      ),
        EzKey( "s"           , lazy.spawn(myDMScript + "dm-screenshot") , desc="DM Screenshot" ),
        EzKey( "b"           , lazy.spawn(myDMScript + "dm-bookman"   ) , desc="DM Bookman"    ),
        EzKey( "n"           , lazy.spawn(myDMScript + "dm-notify"    ) , desc="DM Notify"     ),
        EzKey( "<Backslash>" , lazy.spawn(myDMScript + "dm-notify"    ) , desc="DM Notify"     ),
        EzKey( "k"           , lazy.spawn(myDMScript + "dm-keys"      ) , desc="DM Keys"       ),
    ], name="dm-scripts"),
])

keys.extend([
    EzKey( "A-<F4>" , lazy.spawn(myDMScript + "dm-power") , desc="Logout Menu"),

    KeyChord( [ mod ] , "z" , [
        EzKey( "z" , lazy.spawn(myDMScript + "dm-power"         ) , desc="dm-power"          ),
        EzKey( "l" , lazy.spawn(myDMScript + "dm-power lock"    ) , desc="Lock Screen"       ),
        EzKey( "s" , lazy.spawn(myDMScript + "dm-power suspend" ) , desc="Suspend System"    ),
        EzKey( "p" , lazy.spawn(myDMScript + "dm-power poweroff") , desc="Shutdown System"   ),
        EzKey( "r" , lazy.spawn(myDMScript + "dm-power reboot"  ) , desc="Reboot System"     ),
        EzKey( "w" , lazy.spawn(myDMScript + "dm-power windows" ) , desc="Reboot to Windows" ),
    ], name="(l)ock, (s)uspend, (p)oweroff, (r)eboot, (w)indows"),
])

keys.extend([
    EzKey( "<Print>" , lazy.spawn(myDMScript + "dm-screenshot screen") , desc="Fullscreen Screenshot"     ),
    EzKey( "M-S-<Print>" , lazy.spawn(myDMScript + "dm-screenshot area"  ) , desc="Selection Area Screenshot" ),
    EzKey( "A-<Print>" , lazy.spawn(myDMScript + "dm-screenshot window") , desc="Active Window Screenshot"  ),
    EzKey( "M-<Print>" , lazy.spawn(myDMScript + "dm-screenshot full"  ) , desc="Full Desktop Screenshot"   ),
])

keys.extend([
    KeyChord( [ mod ] , "backslash" , [
        EzKey( "<Backslash>"   , lazy.spawn(myDMScript + "dm-notify recent" ) , desc="Show most recent Notifications" ),
        EzKey( "M-<Backslash>" , lazy.spawn(myDMScript + "dm-notify recent" ) , desc="Show most recent Notifications" ),
        EzKey( "S-<Backslash>" , lazy.spawn(myDMScript + "dm-notify recents") , desc="Show few recent Notifications"  ),
        EzKey( "r"             , lazy.spawn(myDMScript + "dm-notify recents") , desc="Show few recent Notifications"  ),
        EzKey( "S-c"           , lazy.spawn(myDMScript + "dm-notify clear"  ) , desc="Clear all Notifications"        ),
        EzKey( "c"             , lazy.spawn(myDMScript + "dm-notify close"  ) , desc="Clear last Notification"        ),
        EzKey( "a"             , lazy.spawn(myDMScript + "dm-notify context") , desc="Open last Notification"         ),
    ], name="Notifications", mode=True),
])

keys.extend([
    EzKey( "C-A-t"      , lazy.spawn(apps.myTerminal    ) , desc="Launch Terminal"                      ),
    EzKey( "M-<Return>" , lazy.spawn(apps.myTerminal    ) , desc="Launch Terminal"                      ),
    EzKey( "M-c"        , lazy.spawn(apps.myIde         ) , desc="Launch IDE"                           ),
    EzKey( "M-b"        , lazy.spawn(apps.myWebBrowser  ) , desc="Launch Web Browser"                   ),
    EzKey( "M-i"        , lazy.spawn(apps.myIncBrowser  ) , desc="Launch Web Browser in Incognito Mode" ),
    EzKey( "M-p"        , lazy.spawn(apps.myPassManager ) , desc="Autofill Passwords"                   ),
    EzKey( "M-r"        , lazy.spawn(apps.myLauncher    ) , desc="Launch Launcher"                      ),
    EzKey( "M-S-r"      , lazy.spawn("dmenu_run"        ) , desc="Launch dmenu"                         ),

    # Primary
    KeyChord( [ mod ] , "o" , [
        EzKey( "t" , lazy.spawn(apps.myTorBrowser ) , desc="Launch Tor Browser"  ),
        EzKey( "s" , lazy.spawn(apps.mySteam      ) , desc="Launch Steam"        ),
    ], name="Launch"),

    # Secondary
    KeyChord( [ ctrl, alt ] , "o" , [
        EzKey( "t" , lazy.spawn(apps.myCliText      ) , desc="Launch Text Editor"   ),
        EzKey( "p" , lazy.spawn(apps.myPhotoLibrary ) , desc="Launch Photo Library" ),
        EzKey( "g" , lazy.spawn(apps.myImgEditor    ) , desc="Launch Image Editor"  ),
        EzKey( "r" , lazy.spawn(apps.myVctEditor    ) , desc="Launch Vector Editor" ),
        EzKey( "v" , lazy.spawn(apps.myVidEditor    ) , desc="Launch Video Editor"  ),
    ], name="Launch Secondary"),
])

# Drag floating layouts.
mouse = [
    EzDrag(
        "M-1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    EzDrag( "M-3" , lazy.window.set_size_floating(), start=lazy.window.get_size()),
    EzClick( "M-2", lazy.window.bring_to_front()),
]
