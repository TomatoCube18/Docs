## 🐻 ESP32-C3 Bear-Buddy D.I.Y Desktop Companion -  CircuitPython Mini-Camp 



Last Updated: 2nd Nov 2026

### Chapter 1:

#### 1.1: Introduction to CircuitPython Programming

In this mini-camp, we will learn **CircuitPython** using the **Bear-Buddy**, a solder-it-yourself desk companion built around the **ESP32-C3 SuperMini** board! This is a hands-on heavy, easy to follow guided workshop for **Python** users who are curious about **physical computing** & how Python could be used in said field. If you've used Python before, you're already ahead! Now it's time to make your code interact with the real world: **Buttons**, **LEDs**, **Sound**, glowing **NeoPixel matrix**, an **Infrared remote**, and so much more.

By the end of this guide, you'll be able to program your **fully assembled Bear-Buddy** complete with lights, sound, a scrolling pixel face, controllable via a remote control, and even use it as a clock using an i2c character display.

#### 1.2: What is CircuitPython?

**CircuitPython** is a version of Python designed to run on resource constrained device/microcontrollers class devices, aka, small computers embedded inside everyday devices. Developed by Adafruit, CircuitPython brings Python's simplicity into various maker friendly hardware projects.

##### 🔑 Key Features:

- Live coding: Just edit and save `code.py` to run your changes.
- No compiler or special toolchain needed.
- Strong hardware library support (LEDs, buttons, NeoPixels, IR, sensors, displays...)

##### 🐍 CircuitPython vs Python

While the syntax is similar to standard Python 3, CircuitPython uses special modules to interact with various Hardware peripherals:

- `board` - pin mapping (e.g. `board.IO3`)
- `digitalio`, `analogio`, `pwmio` - for physical I/O
- `neopixel`, `pulseio`, `busio` - CircuitPython libraries for peripherals (hold on to your horses, We will be looking at all of them)

##### ⚠️ One Big Difference from the Raspberry Pi Pico

If you have used a Raspberry Pi Pico before, you may remember it shows up on your computer as a USB drive called `CIRCUITPY`, and you install libraries by **dragging and dropping** files onto it.

The **ESP32-C3 does *not* work this way.** It has no USB mass-storage drive. Instead, you edit `code.py` and install libraries **through Thonny** over the USB serial connection. Don't worry, it is only a few clicks different, and [2.4](# 2.4) walks you through it once so every later chapter just says *"install the library (see §2.4)"*.

#### 1.3: Meet Bear-Buddy & Its Peripherals

Everything on Bear-Buddy is already wired to a fixed predefined pin on the ESP32-C3, so there is no breadboard wiring to get wrong, you just address the right pin in code. Here is the full map we will use:

| Peripheral                        | ESP32-C3 Pin(s)                     |
| --------------------------------- | ----------------------------------- |
| **Simple LED**                    | `IO3`                               |
| **Button A** (also BOOT / strap)  | `IO9`                               |
| **Button B**                      | `IO4`                               |
| **Buzzer**                        | `IO10`                              |
| **NeoPixel 5×5 Matrix** (serpentine) | `IO7`                            |
| **IR Receiver**      | `IO21`                              |
| **I²C bus** | `SDA = IO5`, `SCL = IO6`           |

![1.3.1 - BearBuddy_Pinout](assets/1.3.1%20-%20BearBuddy_Pinout.png)

> 💡 Note:
> Keep this table handy. Whenever a chapter says `board.IO7`, it is talking about one of the pins above.

#### 1.4: Meet the ESP32-C3 Supermini board

Bear-Buddy's "brain" is a tiny off-the-shelf **ESP32-C3 SuperMini** development board, soldered onto the bear PCB through its pin headers. Smaller than a postage stamp, it still packs a surprising amount:

- A **32-bit RISC-V** processor running at up to **160 MHz**
- **Wi-Fi** and **Bluetooth LE** radios on board (your gateway to IoT later!)
- A **USB-C** connector for power, flashing, and the serial console
- 400 KB SRAM and 4 MB of flash storage

Every Bear-Buddy peripheral is wired to a fixed pin (see §1.3), but it is worth knowing the three things already on the SuperMini *itself*: two buttons and an LED. You'll use all three during this camp.

##### 🔘 The Two Onboard Buttons: BOOT and RESET

On the SuperMini you'll find two small tactile buttons, usually marked **BOOT** (or **B** / **IO9**) and **RST** (or **RESET** / **R**).

| Button    | Connected to          | What it does                                                 |
| --------- | --------------------- | ------------------------------------------------------------ |
| **RESET** | `EN` (chip enable)    | Restarts the board instantly and re-runs `code.py` from the top, like switching it off and on again. |
| **BOOT**  | `IO9` (strapping pin) | Held *during* reset / power-up, it drops the chip into **download mode** so new firmware can be flashed (that's how we installed CircuitPython in §2.2). While your program is already running, it is just an ordinary push-button. |

> 💡 Note:
> On Bear-Buddy, **Button A and the onboard BOOT button are the same pin (`IO9`)**, they are wired together. So "press Button A" and "press the SuperMini's BOOT button" do exactly the same thing. That is why §2.2 can say "hold Button A" to enter download mode.

Two handy habits for the whole camp:

- **Code acting weird? Tap RESET.** A clean restart without unplugging anything.
- **Need to re-flash or recover a stuck board?** Hold BOOT (Button A), tap RESET (or replug USB), then release BOOT.




### Chapter 2:

#### 2.1: CircuitPython Quick Start Guide with Thonny IDE

##### 2.1.1: 🧰 What You'll Need to get started:

- Your assembled **Bear-Buddy** (with an installed ESP32-C3 SuperMini develoment board)
- A **USB-C** cable (a *data* cable, not charge-only)
- Thonny IDE (Download: https://thonny.org)
- The **Bear-Buddy 5x5 font file** bundled with your kit [`font5x5.bin - https://www.tomatocube.com/file_dir/misc_files/font5x5.bin`](https://www.tomatocube.com/file_dir/misc_files/font5x5.bin), plus the official latest [CircuitPython Library Bundle](https://circuitpython.org/libraries) or the [Tested CircuitPython Library Version - 20261003](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20261003/adafruit-circuitpython-bundle-10.x-mpy-20261003.zip)
- (For flashing) the CircuitPython firmware for the **ESP32-C3** from https://circuitpython.org/downloads (search *ESP32-C3*), or use the **TomatoCube ESP32-C3 Firmware Flasher** at https://tomatocube.com/file_dir/misc_files/ESP32-C3_Flasher/

#### 2.2: 🚀 Install CircuitPython on the ESP32-C3

Unlike the Pico (which takes a drag-and-drop `.uf2` file), the ESP32-C3 is flashed with a `.bin` image over USB serial. Pick the easier Option A unless you enjoy the command line.

##### 🔘 Entering Download (Bootloader) Mode

Some computers need the board put into download mode before flashing:

1. Press and **hold Button A (`IO9` / BOOT)**.
2. While still holding it, plug the USB-C cable in (or tap the RESET button if your board has one).
3. Release **Button A**.

The board is now waiting to receive firmware.

###### [Option A]: Web-based Installer (Recommended)

1. Open **Google Chrome** or **Microsoft Edge** (they support WebSerial).
2. Go to the **TomatoCube ESP32-C3 Firmware Flasher** at https://tomatocube.com/file_dir/misc_files/ESP32-C3_Flasher/, *or* the board page on https://circuitpython.org for the ESP32-C3 and click **OPEN INSTALLER**.
3. Plug in Bear-Buddy (use download mode above if asked), click **Connect**, and pick the serial port.
4. Choose **Install CircuitPython** and follow the prompts.

✅ When it finishes, the board reboots and runs CircuitPython. It will appear as a **serial port** (there is *no* `CIRCUITPY` drive, that is expected).

###### [Option B]: Command Line with `esptool`

```bash
pip install esptool

# Put the board in download mode first (hold Button A while plugging in)
esptool.py --chip esp32c3 erase_flash
esptool.py --chip esp32c3 write_flash -z 0x0 adafruit-circuitpython-esp32c3-<version>.bin
```

Replace the filename with the firmware you downloaded. After flashing, unplug and replug normally.

> 💡 Note:
> Always use the CircuitPython build recommended for your Bear-Buddy kit. A mismatched build may name pins differently or leave out a peripheral we need (like `pulseio` for the IR remote).

#### 2.3: Connecting with Thonny

1. Plug Bear-Buddy into your computer with the USB-C cable.
2. Open **Thonny IDE**.
3. Go to **Tools > Options > Interpreter** and set:
   - **Interpreter**: `CircuitPython (generic)`
   - **Port**: select the serial port for your board (e.g. *USB JTAG/serial debug unit*)
4. Click **OK**. The REPL console (`>>>`) at the bottom of Thonny is now talking to Bear-Buddy.

To see every pin name your build exposes, type this into the REPL:

```python
import board
dir(board)
```

> 💡 Note:
> Because there is no `CIRCUITPY` drive, your program lives *on the board* as `/code.py`. Open **View > Files** in Thonny: the **top pane** is your computer, the **bottom pane** is Bear-Buddy. That bottom pane is how you create `code.py`, make a `/lib` folder, and upload libraries.

#### 2.4: ⭐ Installing Libraries Without a CIRCUITPY Drive
This is the single most important setup step, and the biggest difference from the Raspberry Pico board. On the Pico you drag `.mpy` files onto a drive. On the ESP32-C3 you **upload** them through Thonny's Files pane instead. Do this once and the rest of the camp is easy.

1. Download and unzip the latest from [CircuitPython Library Bundle](https://circuitpython.org/libraries) (the **Bundle for Version 10.x**) or the [Tested CircuitPython Library Version - 20261003](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20261003/adafruit-circuitpython-bundle-10.x-mpy-20261003.zip) on your computer. Keep the **Bear-Buddy library pack** from your kit unzipped too.
2. In Thonny, open **View > Files**.
3. In the **bottom (device)** pane, if there is no `lib` folder, right-click → **New directory…** → name it `lib`.
4. In the **top (computer)** pane, browse into the bundle's `lib/` folder and find the library a chapter asks for.
5. Select it (a `.mpy` file, or a whole folder), right-click → **Upload to /** or **Upload to /lib** (upload it **into the `lib` folder**).
6. Repeat whenever a new chapter needs a new library.

Your device `/` & `/lib/` folder will gradually fill up, for example:

```bash
/
├── font5x5.bin
/lib/
├── neopixel.mpy
├── adafruit_pixelbuf.mpy
├── adafruit_irremote.mpy
└── ...
```

> 💡 Note:
> `.mpy` files are pre-compiled libraries. A few libraries in this camp (like the character-LCD driver) are provided as plain `.py` files in your kit pack, upload them exactly the same way.

#### 2.5: 👋🏻 Digital Output / Hello-World - Blinking the LED (IO3)

Before we embark on the full journey, we will do a quick test to verify that both hardware and software are set up correctly. Let's start with the **Hello-World of the embedded world**: blinking the on-board LED on `IO3`.

![2.5.1 - LED_Location](assets/2.5.1%20-%20LED_Location.png)


##### 📍 LED Pin Mapping

| Bear-Buddy | ESP32-C3 Pin |
| ---------- | ------------ |
| User LED   | **IO3**      |

🔧 In the code entry section of the `Thonny` IDE, insert the following code:

```python
import board
import digitalio
import time

# Configure IO3 as an output pin
led = digitalio.DigitalInOut(board.IO3)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True    # Turn on LED
    time.sleep(0.5)
    led.value = False   # Turn off LED
    time.sleep(0.5)
```

##### 🧪 Key Functions:

- `digitalio.DigitalInOut()` - Access a digital pin of the MCU
- `Direction.OUTPUT` - Set the MCU pin as output
- `led.value = True/False` - Control the voltage on the pin, `True` is `HIGH` or 3.3V & `False` is `LOW` or 0V

Hit `F5` or the green Run button to write the script to Bear-Buddy. If everything works, the LED on **IO3** should blink every half-second!

> 💡 Note:
> If your LED turns on when you expect it off (and vice-versa), it is wired **active-low**. Just swap the `True`/`False` values.

##### ㊔ Naming Your Program File:

CircuitPython looks for a code file on the board to run. There are four options: `code.txt`, `code.py`, `main.txt` and `main.py`. CircuitPython looks for those files, in that order, and runs the first one it finds. While `code.py` is the recommended name, it is good to know the others exist.

#### 2.6: 👋🏻 Sending a Message to the User - Hello World (Serial Console)

One of the staples of programming is the **print statement**, a line that causes your code to output text:

`print("Hello, world!")`

These print statements need somewhere to display, that's the **serial console** (the REPL at the bottom of Thonny), which receives output from Bear-Buddy over USB.

🔧 Insert the updated code:

```python
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.IO3)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("Hello, CircuitPython!")
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

##### 🧪 Key Functions

- `print()` - Pass textual information back to you through the REPL console

The `print()` function is an indispensable debugging tool: it gives real-time feedback over USB with no extra hardware, letting you monitor sensor readings, input states, and program flow to diagnose issues and verify logic.

#### 2.7: Analog Output - LED Fading

Most GPIO pins are **digital**, either ON (3.3V) or OFF (0V). To create in-between brightness we use **Pulse Width Modulation (PWM)**, which rapidly switches the pin ON and OFF. Adjusting the ratio of ON-time to OFF-time (the **duty cycle**) changes the average voltage, and so the LED brightness.

###### 0% Duty Cycle (PWM on a 0 ~ 3v3 Scale)

<svg width="600" height="100" style="zoom: 75%;" >
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <polyline points="0,80 600,80" fill="none" stroke="blue" stroke-width="2" />
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 25% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <line x1="0" y1="60" x2="600" y2="60" stroke="green" stroke-width="1" stroke-dasharray="5,5" />
  <text x="80" y="55" font-size="10" fill="green">Average ~0.825V</text>
  <polyline points="0,80 0,20 50,20 50,80 200,80 200,20 250,20 250,80 400,80 400,20 450,20 450,80 600,80" fill="none" stroke="blue" stroke-width="2" />
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 50% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <line x1="0" y1="50" x2="600" y2="50" stroke="orange" stroke-width="1" stroke-dasharray="5,5" />
  <text x="10" y="45" font-size="10" fill="orange">Average ~1.65V</text>
  <polyline points="0,80 0,20 100,20 100,80 200,80 200,20 300,20 300,80 400,80 400,20 500,20 500,80 600,80" fill="none" stroke="blue" stroke-width="2" />
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 100% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <line x1="0" y1="20" x2="600" y2="20" stroke="black" stroke-width="1" />
  <polyline points="0,20 600,20" fill="none" stroke="blue" stroke-width="2" />
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

```python
import board
import pwmio
import time

# Configure IO3 as a PWM output pin
led = pwmio.PWMOut(board.IO3, frequency=5000, duty_cycle=0)

while True:
    for i in range(0, 65535, 512):   # fade up
        led.duty_cycle = i
        time.sleep(0.01)
    for i in range(65535, 0, -512):  # fade down
        led.duty_cycle = i
        time.sleep(0.01)
```

###### 🧪 Key Functions:

- `PWMOut()` - Configure a pin for PWM output
- `frequency` - How fast the pin switches (5 kHz is invisible to the eye)
- `duty_cycle` - Brightness as a 16-bit value (0 = off, 65535 = full brightness for an active-high LED)



#### 2.8: 💡 The ESP32-C3 Supermini Onboard LED - Your Free Second Debug LED

The SuperMini also carries its own small **LED on `IO8`**, which is *separate* from Bear-Buddy's Simple LED on `IO3`. That means you actually have **two** LEDs to play with: the big one on the bear's body (`IO3`) and this tiny one on the brain board (`IO8`). The onboard one makes an excellent **second debugging indicator**, e.g. blink `IO8` to signal "I reached this part of the code" while `IO3` shows something else.

One quirk: the onboard LED is wired **active-low**, so you turn it **on** by driving the pin **LOW** (`False`) and **off** by driving it **HIGH** (`True`), the opposite of what you might expect.

```python
import board
import digitalio
import time

# Onboard SuperMini LED on IO8 (active-low!)
onboard = digitalio.DigitalInOut(board.IO8)
onboard.direction = digitalio.Direction.OUTPUT

while True:
    onboard.value = False   # LOW  = LED ON  (active-low)
    time.sleep(0.5)
    onboard.value = True    # HIGH = LED OFF
    time.sleep(0.5)
```

> 💡 Note:
> `IO8` is also a **strapping pin**, so like `IO9` it has a job at boot time, but it is perfectly safe to use as an output LED once your program is running. If the onboard LED doesn't blink, your board revision may use a different pin: run `import board; dir(board)` in the REPL and look for a `LED` entry, or try a neighbouring pin.

There is usually a second, **always-on** LED (often red) near the USB-C port, that one is just the **power indicator** and isn't programmable.



### Chapter 3:

#### 3.1: Digital Input - Reading the Buttons

Bear-Buddy has two tactile push-buttons. In this activity, each button toggles the LED on and off, a simple, intuitive interaction:

- Press Button → MCU senses the change → LED toggles ON/OFF

![3.1.1 - Buttons_Location](assets/3.1.1%20-%20Buttons_Location.png)

##### 📍 Button Pin Mapping

| Button       | ESP32-C3 Pin | Notes                         |
| ------------ | ------------ | ----------------------------- |
| **Button A** | **IO9**      | Also the BOOT / strapping pin |
| **Button B** | **IO4**      |                               |

Both buttons are **active-low**: they read `True` (HIGH) when idle and `False` (LOW) when pressed, so we enable the internal **pull-up** resistors.

> 💡 Note:
> **Button A *is* the SuperMini's onboard BOOT button** (both are `IO9`, see §1.4 & §2.8). So whatever you wire up for Button A here, the little BOOT button on the brain board does the exact same thing.

🔧 Insert the following code:

```python
import time
import board
import digitalio

# LED on IO3
led = digitalio.DigitalInOut(board.IO3)
led.direction = digitalio.Direction.OUTPUT
led.value = False

# Button A (IO9) and Button B (IO4), both active-low
btnA = digitalio.DigitalInOut(board.IO9)
btnA.direction = digitalio.Direction.INPUT
btnA.pull = digitalio.Pull.UP

btnB = digitalio.DigitalInOut(board.IO4)
btnB.direction = digitalio.Direction.INPUT
btnB.pull = digitalio.Pull.UP

# Track last states for edge detection (pull-up idle = True)
last_A = True
last_B = True

print("Ready: Button A toggles the LED, Button B prints a message")

while True:
    # -------- BUTTON A (IO9 -> toggle LED) --------
    current_A = btnA.value
    if last_A and not current_A:       # falling edge = fresh press
        led.value = not led.value
        print("Button A pressed -> LED toggled")
    last_A = current_A

    # -------- BUTTON B (IO4) --------
    current_B = btnB.value
    if last_B and not current_B:
        print("Button B pressed!")
    last_B = current_B

    time.sleep(0.02)  # simple debounce / CPU relief
```

##### 🧪 Key Functions:

- `DigitalInOut(board.IOxx)` - Access a GPIO pin.
- `pull = Pull.UP` - Enables the internal pull-up, making input **idle = HIGH**, **pressed = LOW**.
- **Edge detection** (`last_state` vs `current_state`) - Detects a *new* press rather than firing repeatedly while held.
- `led.value = not led.value` - Flips the LED each valid press.

> 💡 Note:
> **Button A doubles as the BOOT pin.** Pressing it *during power-up / reset* puts the board into flashing mode (that's how we installed CircuitPython). Pressing it while your program is already running is perfectly safe and just acts as a normal button.

### Chapter 4:

#### 4.1: The Buzzer - Making Sound

**Everyone loves making noise!** Sound is produced when something **vibrates**, creating pressure waves in the air. Bear-Buddy has a buzzer on `IO10` that we can drive to make tones and melodies.

![4.1.1 - Buzzer_Location](assets/4.1.1%20-%20Buzzer_Location.png)

##### 🎶 How Tone Generation Works

Bear-Buddy uses a single passive buzzer to create tone, we make a tone by sending it a **square wave** with PWM. The **frequency** of that square wave sets the **pitch**, and how long we leave it running sets the **duration**. Set the PWM duty cycle to ~50% to make sound, and to 0% for silence.

##### 📍 Buzzer Pin Mapping

| Buzzer | ESP32-C3 Pin |
| ------ | ------------ |
| Signal | **IO10**     |

🔧 Insert the following code, we will reproduce the welcome melody found across many of TomatoCube's creations:

```python
import board
import pwmio
import time

# variable_frequency=True lets us change the pitch on the fly
buzzer = pwmio.PWMOut(board.IO10, variable_frequency=True)

def play_tone(frequency, duration_ms):
    buzzer.frequency = int(frequency)
    buzzer.duty_cycle = 32768      # 50% -> sound ON
    time.sleep(duration_ms / 1000.0)
    buzzer.duty_cycle = 0          # silence
    time.sleep(0.01)               # short rest between notes

# TomatoCube Welcome melody (E5, D5, F#4)
play_tone(659, 120)   # NOTE_E5
play_tone(587, 120)   # NOTE_D5
play_tone(370, 160)   # NOTE_FS4
```

###### 🧪 Key Concepts

- `pwmio.PWMOut(pin, variable_frequency=True)` - A PWM output whose frequency we can change (needed for different pitches).
- `buzzer.frequency` - Sets the pitch in Hz.
- `buzzer.duty_cycle` - `32768` (50%) makes sound, `0` is silent.

> 💡 Note:
> Bear-Buddy uses a **passive** buzzer, so *we* decide the pitch with `frequency`.

###### 📖 How the Note Corresponds to the Frequency

The **frequency** of a note is the number of vibrations per second. Higher frequency = higher pitch. For example **NOTE_A4** (440 Hz) is the standard tuning reference, and each **octave doubles** the frequency (so **A5** = 880 Hz).

| Note | 0     | 1     | 2      | 3      | 4      | 5      | 6       | 7       | 8       |
| ---- | ----- | ----- | ------ | ------ | ------ | ------ | ------- | ------- | ------- |
| C    | 16.35 | 32.7  | 65.41  | 130.81 | 261.63 | 523.25 | 1046.5  | 2093    | 4186    |
| C#   | 17.32 | 34.65 | 69.3   | 138.59 | 277.18 | 554.37 | 1108.73 | 2217.46 | 4434.92 |
| D    | 18.35 | 36.71 | 73.42  | 146.83 | 293.66 | 587.33 | 1174.66 | 2349.32 | 4698.63 |
| D#   | 19.45 | 38.89 | 77.78  | 155.56 | 311.13 | 622.25 | 1244.51 | 2489    | 4978    |
| E    | 20.6  | 41.2  | 82.41  | 164.81 | 329.63 | 659.25 | 1318.51 | 2637    | 5274    |
| F    | 21.83 | 43.65 | 87.31  | 174.61 | 349.23 | 698.46 | 1396.91 | 2793.83 | 5587.65 |
| F#   | 23.12 | 46.25 | 92.5   | 185    | 369.99 | 739.99 | 1479.98 | 2959.96 | 5919.91 |
| G    | 24.5  | 49    | 98     | 196    | 392    | 783.99 | 1567.98 | 3135.96 | 6271.93 |
| G#   | 25.96 | 51.91 | 103.83 | 207.65 | 415.3  | 830.61 | 1661.22 | 3322.44 | 6644.88 |
| A    | 27.5  | 55    | 110    | 220    | 440    | 880    | 1760    | 3520    | 7040    |
| A#   | 29.14 | 58.27 | 116.54 | 233.08 | 466.16 | 932.33 | 1864.66 | 3729.31 | 7458.62 |
| B    | 30.87 | 61.74 | 123.47 | 246.94 | 493.88 | 987.77 | 1975.53 | 3951    | 7902.13 |

#### 4.2: Button-Triggered Sound Effects

Let's combine Chapters 3 and 4: **Button A** plays a rising chirp, **Button B** plays a falling one.

```python
import board
import pwmio
import digitalio
import time

buzzer = pwmio.PWMOut(board.IO10, variable_frequency=True)

btnA = digitalio.DigitalInOut(board.IO9)
btnA.direction = digitalio.Direction.INPUT
btnA.pull = digitalio.Pull.UP

btnB = digitalio.DigitalInOut(board.IO4)
btnB.direction = digitalio.Direction.INPUT
btnB.pull = digitalio.Pull.UP

def play_tone(freq, ms):
    buzzer.frequency = int(freq)
    buzzer.duty_cycle = 32768
    time.sleep(ms / 1000.0)
    buzzer.duty_cycle = 0

last_A, last_B = True, True
print("Press A for a rising chirp, B for a falling chirp")

while True:
    a, b = btnA.value, btnB.value
    if last_A and not a:
        for f in (523, 659, 784):      # C5 E5 G5
            play_tone(f, 90)
    if last_B and not b:
        for f in (784, 659, 523):      # G5 E5 C5
            play_tone(f, 90)
    last_A, last_B = a, b
    time.sleep(0.02)
```



#### 4.3: Using an Existing RTTTL Melody

Writing out every note by hand (like we did in §4.1) is fine for a three-note jingle, but what about a whole tune? Back in the early mobile-phone era, people shared ringtones as short lines of text called **RTTTL** (Ring Tone Text Transfer Language). There are *thousands* of these little melody strings floating around the internet, and the best part is they are just text, so we can paste one straight into our code and play it.

##### 📦 Install the RTTTL Library

Using **§2.4**, upload into `/lib/`:

- `adafruit_rtttl.mpy`

*(It uses `pwmio`, which is built in, so there's nothing else to add.)*

##### 📍 Buzzer Pin Mapping

Same passive buzzer as before:

| Buzzer | ESP32-C3 Pin |
| ------ | ------------ |
| Signal | **IO10**     |

🔧 In the code entry section of the `Thonny` IDE, insert the following code:

```python
import board
import adafruit_rtttl

# A few classic, traditional Christmas tunes as RTTTL strings
TWINKLE   = "Twinkle:d=4,o=5,b=100:c,c,g,g,a,a,2g,f,f,e,e,d,d,2c"
ODE_TO_JOY = "OdeToJoy:d=4,o=5,b=120:e,e,f,g,g,f,e,d,c,c,d,e,8e.,8d,2d"
JINGLE    = "Jingle:d=8,o=5,b=120:e,e,4e,e,e,4e,e,g,c,d,2e"

# Hand the string straight to the buzzer on IO10
adafruit_rtttl.play(board.IO10, TWINKLE)
```

Hit `F5` to run the code. Bear-Buddy will play "Twinkle, Twinkle, Little Star" through its buzzer, note for note, no hand-written frequencies required. Swap in `ODE_TO_JOY` or `JINGLE` to hear the others.

##### 🧪 Key Concepts

- `adafruit_rtttl.play(pin, tune)` - Parses the RTTTL string and plays it on the given pin. Pass the **pin itself** (`board.IO10`), not a `PWMOut` object - the library creates and cleans up the PWM internally.
- It **blocks** - your program pauses until the whole tune has finished, then carries on.
- You can override the tune's built-in defaults, e.g. `adafruit_rtttl.play(board.IO10, TWINKLE, tempo=180)` to play it faster.

> 💡 Note:
> Because `play()` takes over `IO10` to make its own PWM, don't have a separate `buzzer = pwmio.PWMOut(board.IO10, ...)` (from §4.1) active at the same time, or the pin will already be "in use". In a program that does both, build the manual buzzer *after* your RTTTL playback, or call `buzzer.deinit()` before playing.



##### 🎹 Challenge: A Mini Jukebox

Combine this with the buttons from Chapter 3: play a different tune depending on which button is pressed.

```python
import board
import digitalio
import adafruit_rtttl

btnA = digitalio.DigitalInOut(board.IO9)
btnA.direction = digitalio.Direction.INPUT
btnA.pull = digitalio.Pull.UP

btnB = digitalio.DigitalInOut(board.IO4)
btnB.direction = digitalio.Direction.INPUT
btnB.pull = digitalio.Pull.UP

song = "Tetris:d=4,o=5,b=200:e6,8b,8c6,8d6,16e6,16d6,8c6,8b,a,8a,8c6,e6,8d6,8c6,b,8b,8c6,d6,e6,c6,a,2a,8p,d6,8f6,a6,8g6,8f6,e6,8e6,8c6,e6,8d6,8c6,b,8b,8c6,d6,e6,c6,a,a"
song2 = "MissionImpossible:o=5,d=16,b=100,b=100:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p,a#,g,2d,32p,a#,g,2c#,32p,a#,g,2c,p,a#4,c"


print("Press A or B to play a tune")

while True:
    if not btnA.value:                       # A pressed (active-low)
        adafruit_rtttl.play(board.IO10, song)
    elif not btnB.value:                     # B pressed
        adafruit_rtttl.play(board.IO10, song2)

```

> 💡 Note:
> Instead of using the Adafruit's RTTTL library which doesn't support "multi-threading", we have created a Non-blocking RTTTL parser which parses the tune once, then plays **one note per loop pass** using `time.monotonic()`. It will plays & sound identical to `adafruit_rtttl` library above - just without freezing everything.
>
> Look in the `adafruit-circuitpython-bundle-10.x-mpy-20261003_BearBuddy` for the `\example` folder for the `BackgroundRTTTL.py` script file.
>
> The `time.sleep(0.02)` at the end of the script just paces the loop - it's short enough that note boundaries stay accurate to ~20ms (inaudible), while the LEDs animate smoothly. Replace the LED block with button reads, IR polling, a clock tick... anything. That's the whole trick.

### Chapter 5:

#### 5.1: NeoPixel LEDs - The 5×5 Matrix

**Nothing catches the eye like glowing LEDs!** NeoPixels are colorful, programmable RGB LEDs that display **millions of colors** by mixing red, green, and blue. Bear-Buddy carries a **5×5 serpentine NeoPixel matrix** (25 pixels) on `IO7`, perfect for faces, icons, and scrolling text.

![5.1.2 - NeoPixel_matrix](assets/5.1.2%20-%20NeoPixel_matrix.png)



##### 🌈 How NeoPixels Work

Each NeoPixels (WS2812-type LEDs) are an **intelligent RGB LEDs** that daisy-chain. Each LED reads the first color off the incoming data stream, keeps it, and passes the rest down the chain to the next pixel. In CircuitPython the `neopixel` library handles all the tricky timing for us.

![5.1.1 - NeoPixel_die](assets/5.1.1%20-%20NeoPixel_die.png)

> 💡 Note:
> You can read more about the protocol in the [WS2812B datasheet](https://github.com/TomatoCube18/Lattice_FPGA_MacroKeys/blob/main/Relevant_Docs_DataSheets/WorldSemi-WS2812B-Mini.pdf).

##### 📦 Install the NeoPixel Libraries

Using the steps in **§2.4**, upload these from the bundle's `lib/` into your device `/lib/`:

- `neopixel.mpy`
- `adafruit_pixelbuf.mpy`

##### 📍 NeoPixel Pin Mapping

| NeoPixel Matrix | ESP32-C3 Pin |
| --------------- | ------------ |
| DIN             | **IO7**      |

#### 5.2: Light Them All Up (a Fancy Blink)

```python
import board
import neopixel
import time

pixel_pin  = board.IO7
num_pixels = 25   # 5 x 5
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

while True:
    pixels.fill((0, 0, 255))  # Blue
    time.sleep(0.5)
    pixels.fill((0, 0, 0))    # Off
    time.sleep(0.5)
```

##### 🧪 Key Concepts

- `NeoPixel(pin, count)` - Initializes the chain (25 pixels here).
- `.fill((R, G, B))` - Sets every LED at once.
- `.brightness` - Master brightness (keep it low, 25 LEDs at full white draw a lot of current!).
- `auto_write=True` - Changes show immediately.

> ⚠️ Note:
> Start with a low `brightness` (0.2–0.3). Running all 25 pixels bright white can pull more current than USB comfortably supplies.

#### 5.3: Addressing Individual Pixels - The Serpentine Layout

To light one pixel you index the chain: `pixels[n] = (R, G, B)`, where `n` runs `0 → 24`.

But our matrix is wired in a **serpentine** pattern, and on this panel the chain **starts at the top-right**: the first row runs **right-to-left**, the next row runs **left-to-right**, and so on, zig-zagging like a snake. So pixel *number* order is **not** a tidy grid. To think in (x, y) coordinates we convert with a small helper function:

![5.4.1 - Serpentine_Mapping](assets/5.4.1%20-%20Serpentine_Mapping.svg)

```python
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.IO7, 25, brightness=0.3, auto_write=True)

WIDTH = 5
HEIGHT = 5

def xy(x, y):
    """Convert (x, y) grid coordinates to a serpentine chain index.
       This panel starts top-right: even rows run right->left, odd rows left->right."""
    if y % 2 == 0:
        return y * WIDTH + (WIDTH - 1 - x)   # even rows: right -> left
    else:
        return y * WIDTH + x                 # odd rows:  left  -> right

# Walk a single green dot across the whole grid, row by row
while True:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pixels.fill((0, 0, 0))
            pixels[xy(x, y)] = (0, 255, 0)
            time.sleep(0.08)
```

> 💡 Note:
> Serpentine wiring can start from a different corner depending on orientation. If your dot jumps around, flip the logic (swap which rows reverse, or mirror `x`). Getting this right once is a great logic exercise for students!

#### 5.4: Displaying using PixelMap

Since we're already looking at `xy()`, let us now write a helper function to easily display a static pixel array pattern consisting of 5 rows and 5 columns PixelMap onto the 5x5 NeoPixel Matrix:

```python
import board
import neopixel
import time

WIDTH = HEIGHT = 5
pixels = neopixel.NeoPixel(board.IO7, WIDTH * HEIGHT, brightness=0.3, auto_write=False)

def xy(x, y):
    if y % 2 == 0:
        return y * WIDTH + (WIDTH - 1 - x)   # even rows: right -> left
    else:
        return y * WIDTH + x                 # odd rows:  left  -> right

def draw(pattern, color=(255, 0, 40), bg=(0, 0, 0)):
    for y, row in enumerate(pattern):
        for x, cell in enumerate(row):
            pixels[xy(x, y)] = color if cell in "1#xX*" else bg
    pixels.show()

# --- use it ---
# a beating heart: big frame, small frame, repeat
BIG   = ["01010","11111","11111","01110","00100"]
SMALL = ["00000","01010","01110","00100","00000"]
SMILE = ["00000","01010","00000","10001","01110"]

draw(SMILE, (0, 180, 255)); time.sleep(1.0)
while True:   
    draw(BIG,   (255, 0, 40)); time.sleep(0.4)
    draw(SMALL, (120, 0, 20)); time.sleep(0.4)

```




#### 5.5: ✨ PixelFramebuffer - Treat the Matrix Like a Tiny Screen

Mapping x/y by hand is fine for a dot, but for **text and shapes** it gets tedious. The `adafruit_pixel_framebuf` library wraps our NeoPixel strip in a **PixelFramebuffer** (built on the generic `PixelBuffer`/`framebuf` drawing engine). It gives us a true (x, y) canvas with `pixel()`, `line()`, `rect()`, `text()` and more, and, crucially, it knows how to handle **serpentine** wiring for us with `alternating=True`, so we no longer write our own `xy()` function.

##### 📦 Install the Framebuffer Libraries

Using **§2.4**, upload these into `/lib/` (in addition to `neopixel.mpy` and `adafruit_pixelbuf.mpy`):

- `adafruit_led_animation`
- `adafruit_pixel_framebuf.mpy`
- `adafruit_framebuf.mpy`

We will also need a suitable font file  for our 5x5 LED matrix, we have provided one for you here:
download [`font5x5.bin - https://www.tomatocube.com/file_dir/misc_files/font5x5.bin`](https://www.tomatocube.com/file_dir/misc_files/font5x5.bin) 
and upload `font5x5.bin` into the `/` (Not `/lib`)

* `font5x5.bin`

```python
import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

pixel_pin = board.IO7
WIDTH = 5
HEIGHT = 5

pixels = neopixel.NeoPixel(pixel_pin, WIDTH * HEIGHT,
                           brightness=0.3, auto_write=False)

# alternating=True tells the framebuffer our matrix is wired serpentine.
# Adjust rotation (0-3) / reverse_x / reverse_y if the image is mirrored.
framebuf = PixelFramebuffer(
    pixels, WIDTH, HEIGHT,
    alternating=True,
    reverse_x=True,     # panel starts top-right, so flip each row's start side
    rotation=0,
)

framebuf.fill(0x000000)              # clear to black
framebuf.line(0, 0, 4, 4, 0xFF0000)  # a red diagonal line (corner to corner)
framebuf.pixel(4, 0, 0x00FF00)       # a green pixel in the top-right corner
framebuf.display()                   # push the drawing to the LEDs
```

##### 🧪 Key Concepts

- `PixelFramebuffer(pixels, w, h, alternating=True)` - Wraps the strip as an (x, y) drawing surface and handles serpentine order.
- `framebuf.pixel(x, y, color)` / `line()` / `rect()` - Draw using grid coordinates and a `0xRRGGBB` color.
- `framebuf.text("A", x, y, color)` - Draws characters from the built-in font.
- `framebuf.display()` - Sends the frame to the LEDs (needed because `auto_write=False`).

##### 💬 Scrolling a Message

The built-in font is **5×8 pixels**, taller than our 5-pixel-high matrix, so a letter sitting still gets clipped at the bottom. The classic fix is to **scroll** text sideways so the whole word reads over time:

```python
import board
import neopixel
import time
from adafruit_pixel_framebuf import PixelFramebuffer

WIDTH = 5
HEIGHT = 5
pixels = neopixel.NeoPixel(board.IO7, WIDTH * HEIGHT, brightness=0.3, auto_write=False)
framebuf = PixelFramebuffer(pixels, WIDTH, HEIGHT, alternating=True, reverse_x=True, rotation=0)

message = "BEAR-BUDDY "
# text_width = len(message) * 5   # each character is ~5 px wide
CHAR_W = WIDTH + 1               # 5-px glyph + 1-px gap = 6 px per character
text_width = len(message) * CHAR_W

while True:
    for offset in range(WIDTH, -text_width, -1):
        framebuf.fill(0x000000)
        framebuf.text(message, offset, 0, 0x1030FF, font_name="font5x5.bin")
        framebuf.display()
        time.sleep(0.08)
```

> 💡 Note:
> Tweak `rotation`, the `y` offset, and `brightness` until your text reads cleanly in your Bear-Buddy's mounted orientation.

### Chapter 6:

#### 6.1: Infrared Remote Control (NEC)

Your kit includes an **infrared (IR) remote fob** that speaks the **NEC protocol**, the same scheme used by most TV remotes. Bear-Buddy has an IR receiver on `IO21`. In this chapter we read the remote's button codes and use them to control Bear-Buddy wirelessly.

![6.1.1 - IR_Receiver_Remote](assets/6.1.1%20-%20IR_Receiver_Remote.png)

##### 🔦 How IR / NEC Works

The remote blinks an invisible infrared LED on and off in a precise timed pattern. The receiver turns those blinks back into a stream of pulse lengths. A NEC message carries an **address** and a **command** byte (each sent twice, once inverted, for error checking). The `adafruit_irremote` library decodes those pulses into bytes for us.

##### 📦 Install the IR Library

Using **§2.4**, upload into `/lib/`:

- `adafruit_irremote.mpy`

*(`pulseio` is built into CircuitPython, no upload needed.)*

##### 📍 IR Pin Mapping

| IR Receiver | ESP32-C3 Pin |
| ----------- | ------------ |
| Signal OUT  | **IO21**     |

#### 6.2: Reading Your Remote's Codes

Run this **first** to discover what each button on *your* fob sends, you'll need those numbers for the next step.

```python
import board
import pulseio
import adafruit_irremote

# idle_state=True because the receiver output rests HIGH
ir = pulseio.PulseIn(board.IO21, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

print("Point the remote at Bear-Buddy and press buttons...")

while True:
    pulses = decoder.read_pulses(ir)
    try:
        code = decoder.decode_bits(pulses)
        print("Received:", [hex(b) for b in code])
    except adafruit_irremote.IRNECRepeatException:
        pass   # button is being held down
    except adafruit_irremote.IRDecodeException:
        pass   # noisy / partial signal, ignore
```

Write down the 4-byte code printed for each button you care about. The **last byte** is usually the unique command.

##### 🧪 Key Concepts

- `pulseio.PulseIn(pin, maxlen, idle_state=True)` - Captures the timing of the incoming IR pulses.
- `GenericDecode()` - Turns raw pulses into decoded bytes.
- `decode_bits(pulses)` - Returns the NEC bytes (raises on repeats/noise, which we safely ignore).

#### 6.3: Mapping Buttons to Actions

Now plug in *your* codes (from §6.2) to control the LED and the NeoPixel matrix.

```python
import board
import pulseio
import digitalio
import neopixel
import adafruit_irremote

ir = pulseio.PulseIn(board.IO21, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

led = digitalio.DigitalInOut(board.IO3)
led.direction = digitalio.Direction.OUTPUT

pixels = neopixel.NeoPixel(board.IO7, 25, brightness=0.3, auto_write=True)

# TODO: replace these example last-bytes with the codes YOU saw in 6.2
BTN_POWER = 0x45
BTN_1     = 0x16
BTN_2     = 0x19

while True:
    pulses = decoder.read_pulses(ir)
    try:
        code = decoder.decode_bits(pulses)
        command = code[-1]           # last byte = the button
        if command == BTN_POWER:
            led.value = not led.value
            print("Power -> toggle LED")
        elif command == BTN_1:
            pixels.fill((255, 0, 0))  # red
        elif command == BTN_2:
            pixels.fill((0, 0, 0))    # off
    except adafruit_irremote.IRNECRepeatException:
        pass
    except adafruit_irremote.IRDecodeException:
        pass
```

### Chapter 7:

#### 7.1: I²C Bus & the 1602 Character LCD

##### 7.1.1: 🐙 I²C Expansion Bus

**I²C** (Inter-Integrated Circuit) is a two-wire serial communication protocol invented by **Philips Semiconductor** (now NXP) in the early 1980s. It is widely used to connect low-speed peripherals like sensors, displays, and clocks to microcontrollers. Its superpower is that **many devices share the same two wires**, each one answering to a unique **address**.

Bear-Buddy brings the I²C bus out through the i2C Grove socket on:

- **SDA (Serial Data Line)** → `IO5`
- **SCL (Serial Clock Line)** → `IO6`

We will hang **two** devices on this one bus: a **1602 character LCD** and a **DS1307 real-time clock**.

![7.1.1 - i2C-location](assets/7.1.1%20-%20i2C-location.png)



##### 7.1.2: The 1602 Character LCD

A i2C 1602 segmented character LCD shows **16 characters across, 2 rows**, perfect for menus, sensor values, and messages. The kit's LCD uses an I²C connectivity so it needs only one grove or qwiic cable which could delivers both I²C signals & power in one shot.

![7.1.1 - LCD_1602](assets/7.1.1%20-%20LCD_1602.png)

You can connect the I²C grove cable to the LCD as such.

![7.1.1 - i2c_LCD_1602_RTC](assets/7.1.1%20-%20i2c_LCD_1602_RTC.png)



##### 📦 Install the LCD Library

Using **§2.4**, upload into `/lib/`:

- `adafruit_character_lcd`
- `adafruit_pcf8574.mpy`


##### 📍 I²C Pin Mapping

| I²C | ESP32-C3 Pin |
| --- | ------------ |
| SDA | **IO5**      |
| SCL | **IO6**      |

> 💡 Note:
> In CircuitPython, `busio.I2C()` takes the **clock first, then data**: `busio.I2C(board.IO6, board.IO5)`.

#### 7.2: Finding Devices & "Hello World" on the LCD

First, scan the bus so we know each device's address. I²C 1602 backpacks are usually `0x27` or `0x3F`.

```python
import board
import digitalio
import busio
import adafruit_pcf8574
import adafruit_character_lcd.character_lcd as characterlcd

# I2C bus: (SCL=IO6, SDA=IO5)
i2c = busio.I2C(board.IO6, board.IO5)

# --- Scan the bus (great for debugging!) ---
while not i2c.try_lock():
    pass
print("I2C devices found:", [hex(addr) for addr in i2c.scan()])
i2c.unlock()

# --- Create the LCD (adjust address if the scan shows 0x3F) ---
pcf = adafruit_pcf8574.PCF8574(i2c, address=0x27) 

rs = pcf.get_pin(0)
rw = pcf.get_pin(1)
en = pcf.get_pin(2)
bl = pcf.get_pin(3)
d4 = pcf.get_pin(4)
d5 = pcf.get_pin(5)
d6 = pcf.get_pin(6)
d7 = pcf.get_pin(7)

# The library doesn't drive RW, so tie it low (write mode)
rw.switch_to_output(value=False)

lcd = characterlcd.Character_LCD_Mono(
    rs, en, d4, d5, d6, d7,
    columns=16, lines=2,
    backlight_pin=bl, backlight_inverted=False,
)

lcd.backlight = True
lcd.message = "Hello Bear-Buddy\nCircuitPython!"

```

##### 🧪 Key Concepts

- `i2c.scan()` - Lists the addresses of every device on the bus (use it to confirm `0x27` vs `0x3F`).
- `I2cLcd(i2c, addr, rows, cols)` - Creates the LCD object.
- `lcd.putstr("...")` - Prints text at the cursor.
- `lcd.move_to(col, row)` - Moves the cursor (columns 0–15, rows 0–1).
- `lcd.clear()` - Wipes the screen.

#### 7.3: What Students Can Try Next

- **Change the message:** `lcd.clear(); lcd.putstr("New text")`
- **Show a live counter** that ticks up every second.
- **Mix in a button:** display which button was last pressed.

### Chapter 8:

#### 8.1: Keeping Time - The DS1307 Real-Time Clock

Many projects need **accurate timekeeping**, for clocks, logging, alarms, and timed automation. The ESP32-C3 does not keep good time on its own, and it forgets the time entirely when power is removed.

The **DS1307** RTC module which fit snugly behind the segmented 1602 Character LCD solves this. It keeps ticking on a small **backup battery (CR2032)** even when Bear-Buddy is switched off, and it communicates over the **same shared I²C bus** we just used for the LCD.

![8.1.1 - DS1307_Module](assets/8.1.1%20-%20DS1307_Module.png)

> 💡 Note:
> The DS1307 is simple and reliable but **not temperature-compensated**, so it drifts a little more than a DS3231 and has no built-in temperature sensor. For a learning clock that is perfectly fine, just expect a few seconds of drift over time.

##### 📦 Install the DS1307 Library

Using **§2.4**, upload into `/lib/`:

- `adafruit_register`
- `adafruit_ds1307.mpy`

##### 📍 Shared I²C Bus & Addresses

Both devices live on the **same two wires** (`SDA = IO5`, `SCL = IO6`); CircuitPython tells them apart by address:

| Device               | I²C Address   |
| -------------------- | ------------- |
| 1602 LCD (backpack)  | `0x27` / `0x3F` |
| DS1307 RTC           | `0x68`        |

#### 8.2: Setting & Reading the Time

```python
import time
import board
import busio
import adafruit_ds1307

i2c = busio.I2C(board.IO6, board.IO5)
rtc = adafruit_ds1307.DS1307(i2c)

# --- Set the clock ONCE, then comment this line out ---
# struct_time: (year, month, day, hour, min, sec, weekday, yearday, isdst)
# weekday: Monday=0 ... Sunday=6
# rtc.datetime = time.struct_time((2026, 10, 4, 15, 30, 0, 6, -1, -1))

while True:
    t = rtc.datetime
    print("{:04}-{:02}-{:02}  {:02}:{:02}:{:02}".format(
        t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(1)
```

> 💡 Note:
> Uncomment the `rtc.datetime = ...` line, run it **once** to set the clock, then **comment it out again** and re-upload, otherwise the time resets to that fixed value every time the program starts.

#### 8.3: A Real Clock - Time on the LCD

Finally, let's put the whole chapter together: read the RTC and show a live clock on the 1602 LCD.

```python
import time
import board
import busio
import adafruit_ds1307
import adafruit_pcf8574
import adafruit_character_lcd.character_lcd as characterlcd

# One shared I2C bus for BOTH devices
i2c = busio.I2C(board.IO6, board.IO5)

rtc = adafruit_ds1307.DS1307(i2c)
# --- Create the LCD (adjust address if the scan shows 0x3F) ---
pcf = adafruit_pcf8574.PCF8574(i2c, address=0x27) 

rs = pcf.get_pin(0)
rw = pcf.get_pin(1)
en = pcf.get_pin(2)
bl = pcf.get_pin(3)
d4 = pcf.get_pin(4)
d5 = pcf.get_pin(5)
d6 = pcf.get_pin(6)
d7 = pcf.get_pin(7)

# The library doesn't drive RW, so tie it low (write mode)
rw.switch_to_output(value=False)

lcd = characterlcd.Character_LCD_Mono(
    rs, en, d4, d5, d6, d7,
    columns=16, lines=2,
    backlight_pin=bl, backlight_inverted=False,
)

lcd.backlight = True
lcd.message = "  Bear-Buddy"
lcd.clear()

while True:
    t = rtc.datetime
    date_str = "{:04}-{:02}-{:02}".format(t.tm_year, t.tm_mon, t.tm_mday)
    time_str = "{:02}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec)

    # lcd.cursor_position(3, 0) # Move the cursor to (3, 0)
    lcd.message = date_str + "\n" + time_str
    
    time.sleep(1)

```

##### 🧪 Key Concepts

- **RTC stands alone:** thanks to its battery, the DS1307 keeps time even when Bear-Buddy is off.
- **Shares the I²C bus with the LCD:** multiple devices, one bus, unique addresses.
- **Reading time:** `rtc.datetime` returns a `time.struct_time`.
- **Setting time (run once!):** you only set it the first time (or after a battery change).



### Chapter 9:

#### 9.1: 🏆 Putting It All Together - Challenge Ideas

You now have every Bear-Buddy skill. Combine them into a mini-project:

- **Remote Mood Lamp:** use the IR remote to pick NeoPixel matrix colors and animations.
- **Alarm Buddy:** read the time from the DS1307, and when it hits a set minute, scroll "WAKE UP" across the matrix and chirp the buzzer.
- **Reaction Game:** flash a random matrix pixel, player presses Button A or B as fast as they can, show the reaction time on the LCD.
- **IR Clock Setter:** set the DS1307 time using the number buttons on your remote, no code edit needed.

Mix the chapters, break things, and try again, that is exactly how makers learn. Happy building! 🐻



### Chapter X: Appendix

#### 10.1:  🎼 Anatomy of an RTTTL String

An RTTTL tune has three parts separated by colons: **`name : defaults : notes`**

`TwinkleTwinkle:d=4,o=5,b=100:c,c,g,g,a,a,2g,f,f,e,e,d,d,2c
    name       :  defaults   :    notes    `


The **defaults** set the baseline for the whole tune:

- `d` = default note **duration** (`1`=whole, `2`=half, `4`=quarter, `8`=eighth...)
- `o` = default **octave** (4 to 7; octave 5 sits around middle C)
- `b` = tempo in **beats per minute** (higher = faster)

Each **note** is then written as `[duration] letter [octave] [.]`:

- an optional number in front sets *this* note's duration (overriding `d`), e.g. `2g` is a half-note G
- the letter is the pitch: `c c# d d# e f f# g g# a a# b`, and `p` means a **pause** (rest)
- an optional octave digit follows, e.g. `e6`
- a trailing `.` makes it a **dotted** note (1.5x as long)

So `8a#6.` means "a dotted eighth-note A-sharp in octave 6". It reads just like the note-frequency ideas from §4.1, only written compactly.
