import board
import neopixel
import time

WIDTH = HEIGHT = 5
pixels = neopixel.NeoPixel(board.IO7, WIDTH * HEIGHT, brightness=0.3, auto_write=False)

def xy(x, y):
    """Convert (x, y) grid coordinates to a serpentine chain index.
       This panel starts top-right: even rows run right->left, odd rows left->right."""
    if y % 2 == 0:
        return y * WIDTH + (WIDTH - 1 - x)   # even rows: right -> left
    else:
        return y * WIDTH + x                 # odd rows:  left  -> right


def draw(pattern, color=(255, 0, 40), bg=(0, 0, 0)):
    """pattern: a SYMBOLS name, a list of 5 row-strings, or a multiline string.
       Any of '1 # x *' counts as ON; everything else is OFF."""
    if isinstance(pattern, str):
        pattern = SYMBOLS[pattern] if pattern in SYMBOLS \
                  else [ln.strip() for ln in pattern.strip("\n").splitlines()]
    for y, row in enumerate(pattern):
        for x, cell in enumerate(row):
            pixels[xy(x, y)] = color if cell in "1#xX*" else bg
    pixels.show()

# A little picture library. '1' = lit, '0' = off.
SYMBOLS = {
    "HEART": ["01010",
              "11111",
              "11111",
              "01110",
              "00100"],
    "heart": ["00000",
              "01010",
              "01110",
              "00100",
              "00000"],
    "SMILE": ["00000",
              "01010",
              "00000",
              "10001",
              "01110"],
    "CHECK": ["00000",
              "00001",
              "00010",
              "10100",
              "01000"],
    "CROSS": ["10001",
              "01010",
              "00100",
              "01010",
              "10001"],
}

draw("SMILE", (0, 180, 255)); time.sleep(1.0)
while True:   
    draw("HEART",   (255, 0, 40)); time.sleep(0.4)
    draw("heart", (120, 0, 20)); time.sleep(0.4)