# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import hook

# from typing import list 
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
font = "nerd-fonts-complete"
color_barra1= "1d8348"
color_barra2= "8e44ad"
tamano_iconos = 19
color_fg = " #abebc6"
color_activo = "#abebc6"
color_inactivo = "#b7950b"
tamano_barra = 30
grupo_1 = "#5dade2"
grupo_2 = "#ca6f1e"
grupo_3 = "#f5cba7"
color_texto_1 = "#f7dc6f"

# definiciòn de funciones

def separador ():
    return widget.Sep(
        padding= 3,
        foreground = color_barra2,
        linewith= 2,
        )

def rectangulo(vColor,tipo):
    if tipo == 0:
        icono = "" #nf-ple-left_half_circle_thick
    else:
        icono = "" # nf-ple-right_half_circle_thick
    return widget.TextBox(
                    text = icono,
                    fontsize = tamano_barra,
                    foreground = vColor,
                    padding = -0.8,
                    
    )

def fc_iconos (icono,color_grupo):
    return widget.TextBox (
        text = icono,
        foreground = color_texto_1,
        background = color_grupo,
        fontsize = tamano_iconos,

    )


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # lanzar menu y firefox
    Key ([mod], "m", lazy.spawn("rofi -show drun"), desc="lanzar dmenu"),
    Key ([mod], "f", lazy.spawn("firefox"), desc="lanzar firefox"),    
    # lanzar vscodium
    Key ([mod], "c", lazy.spawn("vscodium"), desc="lanzar codium"),
    # lanzar thunar
    Key ([mod], "a", lazy.spawn("thunar"), desc="lanzar thunar"),
    # lanzar spotify
    Key ([mod], "s", lazy.spawn("ncspot >> alacritty"), desc="lanzar spotify"),

    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # teclas volumen
    Key([], "XF86AudioLowerVolume", lazy.spwan("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spwan("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spwan("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    #catura pantalla
    Key([mod],"p", lazy.spawn("scrot")),
    Key([mod, "shift"], "p", lazy.spawn("scrot -s")),
]

groups = [Group(i) for i in ["", "爵", "" , "","","",]]

for i, group  in enumerate(groups):
    numeroEscritorio =str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio, lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),

            
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=3),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
     layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize= 14,
    padding= 2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                active = color_activo,
                inactive = color_inactivo,
                highlight_method = 'block',
                margin_x = 0,
                margin_y = 0,
                padding_x = 9,
                borderwidth = 2,
                fontsize = 18,
                rounded = 'True',
                this_current_screen_border = "#3498db",
                urgent_alert_method = 'border',
                center_aligned = 'True',

                ),
                separador(),
                widget.Prompt(),
                widget.WindowName(
                    foreground = color_texto_1,
                ),
                separador(),
                widget.Systray(
                    icon_size = 15, padding = 3,
                ),
                #grupo uno
                separador(),
                rectangulo(grupo_1,0),
                fc_iconos("",grupo_1),
                widget.ThermalSensor(
                    background = grupo_1,
                    tag_sensor = "Core 0",
                    fmt = 'Core_1 :{}',
                ),
                widget.ThermalSensor(
                    background = grupo_1,
                    tag_sensor = "Core 1",
                    fmt = 'Core_2 :{}',
                ),
                fc_iconos("  ",grupo_1),
                widget.MemoryGraph(
                    background = grupo_1,
                    type='line',
                    samples = 3000,
                    frequency = 4,
                    border_width = 1,
                    line_width = 2,
                    graph_color = grupo_2,
                ),
                widget.Memory(
                    background = grupo_1,
                    format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                ),
                rectangulo(grupo_1,1),
                separador(),
                #finaliza el grupo 1
                #comienza el grupo 2
                rectangulo(grupo_2,0),
                widget.Clock(
                    format=" %d-%b-%y %a %H:%M ",
                    background = grupo_2,
                    foreground = color_texto_1,
                ),
                fc_iconos("   ",grupo_2),
                widget.CheckUpdates(
                    background = grupo_2,
                    colour_have_updates = "#ffffff",
                    colour_no_updates = color_texto_1,
                    no_update_string = "0",
                    display_format = '{updates}',
                    update_interval = 1800,
                    distro = "Arch_checkupdates",

                ),
                rectangulo(grupo_2,1),
                #aca termina el grupo 2
                #comienza el grupo 3
                separador(),
                rectangulo(grupo_3,0),
                widget.CurrentLayoutIcon(
                    background = grupo_3,
                    scale = 0.7,
                ),
                widget.CurrentLayout(
                    background = grupo_3,
                    fmt = '{}',
                    fontsize = 2,
                ),
                widget.QuickExit(
                    default_text='  ',
                    countdown_format='[{}]',
                    background = grupo_3,
                    foreground = "#c0392b",  ),
                rectangulo(grupo_3,1),
            ],
            tamano_barra,
            border_width=[0, 0, 3, 0],  # Draw top and bottom borders
            border_color=["2ecc71" , "d7bde2", "d7bde2", "5dade2"],  # Borders are magenta
            background=[color_barra1 , color_barra2],
            
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                #comienza el grupo 2
                rectangulo(grupo_2,0),
                widget.Clock(
                    format=" %d-%b-%y %a %H:%M ",
                    background = grupo_2,
                    foreground = color_texto_1,
                ),
                fc_iconos("   ",grupo_2),
                widget.CheckUpdates(
                    background = grupo_2,
                    colour_have_updates = "#ffffff",
                    colour_no_updates = color_texto_1,
                    no_update_string = "0",
                    display_format = '{updates}',
                    update_interval = 1800,
                    distro = "Arch_checkupdates",

                ),
                rectangulo(grupo_2,1),
                #aca termina el grupo 2
                #comienza el grupo 3
                separador(),
                rectangulo(grupo_3,0),
                widget.CurrentLayoutIcon(
                    background = grupo_3,
                    scale = 0.7,
                ),
                widget.CurrentLayout(
                    background = grupo_3,
                    fmt = '{}',
                    fontsize = 2,
                ),
                widget.QuickExit(
                    default_text='  ',
                    countdown_format='[{}]',
                    background = grupo_3,
                    foreground = "#c0392b",  ),
                rectangulo(grupo_3,1),
            ],
            20,
            border_width=[0, 0, 3, 0],  # Draw top and bottom borders
            border_color=["2ecc71" , "d7bde2", "d7bde2", "5dade2"],  # Borders are magenta
            background=[color_barra1 , color_barra2],
            
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
