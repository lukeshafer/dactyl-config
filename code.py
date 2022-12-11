print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
keyboard.row_pins = (board.GP13, board.GP12, board.GP11, board.GP14, board.GP10, board.GP27, board.GP28, )
keyboard.col_pins = (board.GP22,board.GP21,board.GP20,board.GP19,board.GP3,board.GP2,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----- MODULES -----

layers = Layers()mkk,kkkmm
media_keys = MediaKeys()
mouse_keys = MouseKeys()
split = Split(
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)
keyboard.modules = [layers, split, mouse_keys, media_keys]


# ----- USER KEYS -----

_____ = KC.TRNS
#_____ = KC.NO
FN = KC.MO(1)
CLMK = KC.TG(2)


# ----- KEYMAP -----

keyboard.keymap = [
    [ # DEFAULT QWERTY
        KC.GRV,  KC.N1, KC.N2,   KC.N3,   KC.N4,   KC.N5,                    KC.N6, KC.N7, KC.N8,   KC.N9,   KC.N0,    KC.EQL,
        KC.TAB,  KC.Q,  KC.W,    KC.E,    KC.R,    KC.T,                     KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,     KC.MINS,
        KC.ESC,  KC.A,  KC.S,    KC.D,    KC.F,    KC.G,                     KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN,  KC.QUOT,
        KC.BSPC, KC.Z,  KC.X,    KC.C,    KC.V,    KC.B,                     KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH,  KC.ENT,
        _____,   KC.RLD,KC.LBRC, KC.RBRC, KC.LCTL, KC.LGUI,                  CLMK,  KC.SPC, KC.BSLS, KC.SLSH,_____,   _____,
        _____,   _____, _____,   _____,   FN,      KC.LSHIFT,                _____, KC.RSHIFT, _____,  _____,_____,    _____,
        _____,   _____, _____,   _____,   KC.LALT, KC.ENT,                   KC.LGUI,KC.RCTL, _____,  _____, _____,    _____,
    ],
    [ # FUNCTION LAYER
        KC.F1,  KC.F2,  KC.F3,   KC.F4,   KC.F5,   KC.F6,                    KC.F7, KC.F8, KC.F9,   KC.F10,  KC.F11,   KC.F12,
        _____,_____,  _____,   KC.UP,   _____,   KC.VOLU,                    _____, _____, _____,   _____,   _____,    _____,
        _____,  _____,  KC.LEFT, KC.DOWN, KC.RIGHT,KC.VOLD,                  KC.MW_UP, KC.MB_LMB, KC.MB_MMB,   KC.MB_RMB,   _____,    _____,
        KC.DEL,  _____,  _____,   _____,   _____,   KC.MUTE,                 KC.MW_DN, _____, KC.MPLY,   _____,   _____,    KC.CAPS,
        _____,  _____,  _____,   _____,   _____,   _____,                    _____, _____,    KC.MNXT,   KC.MPRV,   _____,     _____,
        _____,  _____,  _____,   _____,   KC.TO(0), _____,                   _____, _____, _____,   _____,   _____,     _____,
        _____,  _____,  _____,   _____,   _____,   _____,                    _____,_____, _____,   _____,   _____,     _____,
    ],
    [ # COLEMAK LAYER
        _____,  _____,  _____,   _____,   _____,   _____,                    _____, _____, _____,   _____,   _____,    _____,
        _____,  KC.Q,  KC.W,    KC.F,    KC.P,    KC.G,                      KC.J,  KC.L,  KC.U,    KC.Y,    KC.SCLN,     KC.BSLS,
        _____,  KC.A,  KC.R,    KC.S,    KC.T,    KC.D,                      KC.H,  KC.N,  KC.E,    KC.I,    KC.O,  KC.QUOT,
        _____,  KC.Z,  KC.X,    KC.C,    KC.V,    KC.B,                      KC.K,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH,  KC.MINS,
        _____,   _____, _____,   _____,   _____,   _____,                    KC.TG(0), _____, _____,   _____,   _____,     _____,
        _____,   _____, _____,   _____,   _____,   _____,                    _____, _____, _____,   _____,   _____,     _____,
        _____,   _____, _____,   _____,   _____,   _____,                    _____, _____, _____,   _____,   _____,     _____,
    ],
]



if __name__ == '__main__':
    keyboard.go()
