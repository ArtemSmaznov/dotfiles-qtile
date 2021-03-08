from libqtile import bar, widget
import widgets as my_widget
import theme.default as theme


def init_panel_widgets():
    panel_widgets = [
        my_widget.separator(),
        my_widget.start_widget,
        my_widget.clock,
        my_widget.group_box,
        my_widget.prompt_widget,
        my_widget.separator(40),
        my_widget.window_name,

        my_widget.power_arrow(theme.widget_bg_1, theme.background),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            fontsize=11
        ),
        widget.ThermalSensor(
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            threshold=90,
            padding=5
        ),
        my_widget.power_arrow(theme.widget_bg_2, theme.widget_bg_1),
        widget.TextBox(
            text=" 🖬",
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=5
        ),
        my_widget.power_arrow(theme.widget_bg_1, theme.widget_bg_2),
        widget.Net(
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            padding=5
        ),
        my_widget.power_arrow(theme.widget_bg_2, theme.widget_bg_1),
        widget.TextBox(
            text=" Vol:",
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=0
        ),
        widget.Volume(
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=5
        ),
        my_widget.power_arrow(theme.widget_bg_1, theme.widget_bg_2),
        widget.CurrentLayout(
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            padding=5
        ),
        my_widget.power_arrow(theme.widget_bg_2, theme.widget_bg_1),
        my_widget.date,
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=theme.background,
            background=theme.widget_bg_2
        ),
        my_widget.power_arrow(theme.widget_bg_1, theme.widget_bg_2),
        widget.QuickExit(
            foreground=theme.foreground,
            background=theme.widget_bg_1
        ),
        my_widget.sys_tray,
    ]
    return panel_widgets


def init_bar():
    return bar.Bar(init_panel_widgets(), 24, background=theme.background)
