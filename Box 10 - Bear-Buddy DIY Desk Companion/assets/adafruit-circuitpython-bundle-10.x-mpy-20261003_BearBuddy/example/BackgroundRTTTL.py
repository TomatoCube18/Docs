import time
import board
import pwmio

# --- tiny RTTTL parser: returns a list of (frequency_hz, seconds); 0 Hz = rest ---
_SEMI = {"c":0,"c#":1,"d":2,"d#":3,"e":4,"f":5,"f#":6,"g":7,"g#":8,"a":9,"a#":10,"b":11}

def _note_freq(letter, octave):
    if letter == "p":
        return 0                                   # 'p' = pause / rest
    midi = 12 * (octave + 1) + _SEMI[letter]
    return int(round(440 * 2 ** ((midi - 69) / 12)))

def parse_rtttl(tune):
    _, defaults, notes = tune.lower().split(":")
    d = o = b = None
    for item in defaults.split(","):
        k, v = item.split("=")
        if k == "d": d = int(v)
        elif k == "o": o = int(v)
        elif k == "b": b = int(v)
    d = d or 4; o = o or 6; b = b or 63
    out = []
    for tok in notes.split(","):
        tok = tok.strip()
        if not tok:
            continue
        i = 0
        while i < len(tok) and tok[i].isdigit():    # leading duration digits
            i += 1
        dur = int(tok[:i]) if i else d
        letter = tok[i]; j = i + 1
        if j < len(tok) and tok[j] == "#":          # sharp
            letter += "#"; j += 1
        rest = tok[j:]
        dotted = "." in rest
        octv = o
        for ch in rest:                             # trailing octave digit
            if ch.isdigit():
                octv = int(ch)
        secs = (4 / dur) * (60 / b)
        if dotted:
            secs *= 1.5
        out.append((_note_freq(letter, octv), secs))
    return out


class MelodyPlayer:
    """Plays an RTTTL tune one note at a time - never blocks the main loop."""
    def __init__(self, pin):
        self.buzzer = pwmio.PWMOut(pin, variable_frequency=True)
        self.notes = []
        self.index = 0
        self.playing = False
        self._next_time = 0

    def start(self, tune):
        self.notes = parse_rtttl(tune)
        self.index = 0
        self.playing = True
        self._next_time = time.monotonic()          # first note is due now

    def stop(self):
        self.playing = False
        self.buzzer.duty_cycle = 0

    def update(self):
        """Call this every time around your loop."""
        if not self.playing:
            return
        if time.monotonic() < self._next_time:
            return                                  # current note still ringing
        if self.index >= len(self.notes):
            self.stop()                             # reached the end
            return
        freq, secs = self.notes[self.index]
        if freq > 0:
            self.buzzer.frequency = freq
            self.buzzer.duty_cycle = 32768          # 50% -> sound on
        else:
            self.buzzer.duty_cycle = 0              # a rest
        self._next_time = time.monotonic() + secs
        self.index += 1
        
import neopixel
import digitalio

btnA = digitalio.DigitalInOut(board.IO9)
btnA.direction = digitalio.Direction.INPUT
btnA.pull = digitalio.Pull.UP

btnB = digitalio.DigitalInOut(board.IO4)
btnB.direction = digitalio.Direction.INPUT
btnB.pull = digitalio.Pull.UP


song = "Tetris:d=4,o=5,b=200:e6,8b,8c6,8d6,16e6,16d6,8c6,8b,a,8a,8c6,e6,8d6,8c6,b,8b,8c6,d6,e6,c6,a,2a,8p,d6,8f6,a6,8g6,8f6,e6,8e6,8c6,e6,8d6,8c6,b,8b,8c6,d6,e6,c6,a,a"
song2 = "MissionImpossible:o=5,d=16,b=100,b=100:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p,a#,g,2d,32p,a#,g,2c#,32p,a#,g,2c,p,a#4,c"

player = MelodyPlayer(board.IO10)
# player.start(song)

pixels = neopixel.NeoPixel(board.IO7, 25, brightness=0.3, auto_write=True)
level = 0
step = 8

while True:
    player.update()                    # keep the tune going (returns instantly)
    
    if not btnA.value:                       # A pressed (active-low)
        player.stop()
        player.start(song)
    elif not btnB.value:                       # B pressed (active-low)
        player.stop()
        player.start(song2)
        
    # meanwhile, pulse the matrix - proof the device isn't frozen
    pixels.fill((level, 0, 255 - level))
    level += step
    if level >= 255 or level <= 0:
        step = -step
        level = max(0, min(255, level))

    time.sleep(0.02)                   # ~50 fps loop; notes still land on time