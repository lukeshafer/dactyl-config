print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.layers import Layers
from kmk.modules.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
keyboard.row_pins = (board.GP13, board.GP12, board.GP11, board.GP8, board.GP7, board.GP5, board.GP4, )
keyboard.col_pins = (board.GP27,board.GP26,board.GP22,board.GP21,board.GP3,board.GP2,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----- MODULES -----

layers = Layers()
media_keys = MediaKeys()
split = Split(
    split_side=SplitSide.LEFT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
)
keyboard.modules = [layers, media_keys, split]


# ----- USER KEYS -----

_____ = KC.TRNS
XXXXX = KC.NO
FN = KC.TT(1)


# ----- KEYMAP -----

keyboard.keymap = [
    [ # DEFAULT QWERTY
        KC.GRV,  KC.N1, KC.N2,   KC.N3,   KC.N4,   KC.N5,                    KC.N6, KC.N7, KC.N8,   KC.N9,   KC.N9,    KC.N5,
        KC.TAB,  KC.Q,  KC.W,    KC.E,    KC.R,    KC.T,                     KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,     KC.BSLS,
        KC.UP,  KC.A,  KC.S,    KC.D,    KC.F,    KC.G,                     KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN,  KC.QUOT,
        KC.DOWN, KC.Z,  KC.X,    KC.C,    KC.V,    KC.B,                     KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH,  KC.MINS,
        _____,   _____, KC.LBRC, KC.RBRC, KC.LCTL, KC.SPC,                   _____, FN,    KC.LEFT, KC.RIGHT, ____,     ____,
        _____,   _____, _____,   _____,   KC.LALT, KC.LGUI,                  _____, KC.BSPC, _____, _____,   ____,     ____,
        _____,   _____, _____,   _____,   KC.LSFT, XXXXX                     KC.RCTL, KC.ESC, _____,   _____,   ____,     ____,
    ],
    [ # FUNCTION LAYER
        KC.F1,  KC.F2,  KC.F3,   KC.F4,   KC.F5,   KC.F6,                    KC.F7, KC.F8, KC.F9,   KC.F10,  KC.F11,   KC.F12,
        XXXXX,  XXXXX,  XXXXX,   XXXXX,   XXXXX,   XXXXX,                    XXXXX, XXXXX, XXXXX,   XXXXX,   XXXXX,    XXXXX,
        XXXXX,  XXXXX,  XXXXX,   XXXXX,   XXXXX,   XXXXX,                    XXXXX, XXXXX, XXXXX,   XXXXX,   XXXXX,    XXXXX,
        XXXXX,  XXXXX,  XXXXX,   XXXXX,   XXXXX,   XXXXX,                    XXXXX, XXXXX, XXXXX,   XXXXX,   XXXXX,    XXXXX,
        _____,   _____, XXXXX,   XXXXX,   XXXXX,   XXXXX,                    _____, FN,    XXXXX,   XXXXX,   ____,     ____,
        _____,   _____, _____,   _____,   XXXXX,   XXXXX,                    _____, XXXXX, _____,   _____,   ____,     ____,
        _____,   _____, _____,   _____,   XXXXX,   XXXXX,                    XXXXX, XXXXX, _____,   _____,   ____,     ____,
    ],
]



if __name__ == '__main__':
    keyboard.go()
