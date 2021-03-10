# https://terminal.sexy/ - Termite export format is very easy to convert
import theme.colors.material as material
import theme.colors.sweetlove as scheme

#  Sizes
bar_size = 24
app_gap = 6

#  Fonts
font_regular = 'SF Pro Text Regular'
font_bold = 'SF Pro Text Bold'

#  Colors
#  foreground = material.amber_100
foreground = scheme.foreground
background = scheme.background
inactive = material.grey_800
#  inactive = scheme.color8

selection_accent = scheme.color1
selection_bg = scheme.color9

other_selection_accent = scheme.color2
other_selection_bg = scheme.color10

widget_bg_0 = background
widget_bg_1 = scheme.color14
widget_bg_2 = scheme.color13
widget_bg_3 = scheme.color12
widget_bg_4 = scheme.color11

power_line_colors = [
    background,
    scheme.color9,
    scheme.color10,
    scheme.color11,
    scheme.color12,
    scheme.color13,
    scheme.color14,
]
