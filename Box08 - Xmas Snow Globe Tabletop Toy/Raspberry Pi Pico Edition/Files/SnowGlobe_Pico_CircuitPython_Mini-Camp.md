## 🎄 Raspberry Pi Pico (CircuitPython) X'MAS SnowGlobe Table-Top Toy - Mini-Camp



Last Updated: 9th Dec 2025

### Chapter 1:

#### 1.1: Introduction to CircuitPython Programming

In this mini-camp, we will learn **CircuitPython** using the **X’MAS SnowGlobe TableTop-Toy for Raspberry Pi PiCO**! This is a hands-on heavy, easy to follow guided workshop for **Python** users who are curious about **physical computing** & how Python could be used in said field. If you've used Python before, you're already ahead! Now it's time to make your code interact with the real world: **Sensors**, **LEDs**, **Sound**, and much much more.

By the end of this guide, you'll be able to configure your **fully programmable** X’MAS SnowGlobe TableTop-Toy complete with lights and sound effects.



#### 1.2: What is CircuitPython?

**CircuitPython** is a version of Python designed to run on resource constrained device/microcontrollers class devices, aka, small computers embedded inside everyday devices. Developed by Adafruit, CircuitPython brings Python’s simplicity into various maker friendly hardware projects.

##### 🔑 Key Features:

- Live coding: Just edit and save `code.py` to run your changes.
- No compiler or special toolchain needed.
- Strong hardware library support (LEDs, buttons, NeoPixels, HID, sensors, audio...)

##### 🐍 CircuitPython vs Python

While the syntax is similar to standard Python 3, CircuitPython uses special modules to interact with various Hardware peripherals:

- `board` - pin mapping (e.g. `board.GP13`)
- `digitalio`, `analogio`, `pwmio` - for physical I/O
- `neopixel`, `adafruit_hid`, `audiomp3` - CircuitPython libraries for peripherals (hold on to your horses, We will be looking all of them)



### Chapter 2:

#### 2.1: CircuitPython Quick Start Guide with Thonny IDE:

##### 2.1.1: 🧰 What You’ll Need to get started:

- **X’MAS SnowGlobe TableTop-Toy for Raspberry Pi PiCO** with any **official Raspberry Pi Pico/Pico2** development board.
- micro-USB cable
- Thonny IDE (Download: https://thonny.org)

- (Optional for Manual Installation) CircuitPython firmware for RP2040 (https://circuitpython.org/board/raspberry_pi_pico/) or RP2350 (https://circuitpython.org/board/raspberry_pi_pico2/) 


##### 2.1.2: 🚀 Install CircuitPython on RP2040 or RP2350

###### [Option A]: Install CircuitPython on RP2040 Manually or RP2350

1. **Enter Bootloader Mode**
   - Hold the **BOOTSEL** button, on your Raspberry Pi Pico Development Board.
   - While holding **BOOTSEL Button**, press **RESET** to reset the Pico – the **RESET button** is located on the bottom of the Carrier Board.
   - Release the BOOTSEL button.
   - A new drive named **`RPI-RP2`** will appear.

2. **Copy CircuitPython UF2**
   - Download the latest CircuitPython UF2 for RP2040 from the official site Adafruit’s Page - [**Download for Raspberry Pi Pico / RP2040**](https://circuitpython.org/board/raspberry_pi_pico/) or [**Download for Raspberry Pi Pico2 / RP2350**](https://circuitpython.org/board/raspberry_pi_pico2/)
   - Drag and drop it into the `RPI-RP2` drive.
   - ✅ The board will reboot and mount as `CIRCUITPY`.



###### [Option B]: Install CircuitPython via Thonny

1. Plug your **X’MAS SnowGlobe TableTop-Toy for Raspberry Pi PiCO** with any **official Raspberry Pi Pico/Pico2** development board into your computer via USB.
   - (Hold the **BOOTSEL**, while plugging in only if you're flashing it for the first time.)
2. Open **Thonny IDE**.
3. Go to **Tools > Options > Interpreter**.
4. Set:
   - **Interpreter**: `CircuitPython (generic)`
5. If CircuitPython isn’t already installed, Thonny will prompt you to install it.
6. Click **Install or update CircuitPython(UF2)**, then:
   - Choose your board you have installed with the Carrier board, e.g."variant: Raspberry Pi Pico/Pico-H" or "variant: Raspberry Pi Pico2" or its wireless variant.
   - Choose the CircuitPython version, "version 10.0.3" as of the writing of this guide
   - Click **Install**

✅ Your board will reboot and appear as a `CIRCUITPY` USB drive.

![2.1.2.1 - BootSel_Button](assets/2.1.2.1%20-%20BootSel_Button.png)



#### 2.2: 👋🏻 Digital Output/Hello-World - Blinking an LED (GPIO16)

Before we embark on the full journey into CircuitPython or any Programming Language, we will do a quick and simple test to verify all setup, both hardware and software, and set up correctly. So let’s start with something simple, blinking the user LED on `GPIO 16`, or the Hello-World of the Embedded Hardware world.

In this section, we will cover how to access your board's pins through CircuitPython. 

<img src="assets/2.2.1%20-%20LED1_Location.png" alt="2.2.1 - LED1_Location" width="500" height="auto"/>


##### 🔌 Wiring of the LED1 (GPIO16) to Pico Dev Board

LED Pinout as follows:

| LED1       | Connect to PICO                |
| ---------- | ------------------------------ |
| Anode (+)  | **3.3V** (with a 1kΩ resistor) |
| Cathod (-) | **GPIO 16**                    |


🔧 In the code entry section of the `Thonny` IDE, insert the following code:

```python
import board
import digitalio
import time

# Configure GP16 as an output pin
led1 = digitalio.DigitalInOut(board.GP16)
led1.direction = digitalio.Direction.OUTPUT

while True:
    led1.value = True   # Turn on LED
    time.sleep(0.5)
    led1.value = False  # Turn off LED
    time.sleep(0.5)
```

#####  🧪 Key Functions:

- `digitalio.DigitalInOut()` - Access a digital pin of the MCU
- `Direction.OUTPUT` - Set the MCU pin as output
- `led.value = True/False` - Control the voltage on the pin, `True` is `HIGH` or 3.3V & `False` is `LOW` or 0V

Hit `F5` or the Green Run button on the tool panel to write the script to the onboard CircuitPython interpreter. If Everything works correctly, the user LED connected to **GPIO 16** should start blinking every half-second!

> 💡 Note:
> To see all the available board-specific objects and pins for your board, in the REPL console (`>>>`), run the following commands:
>
> ```python
> import board
> dir(board)
> ```



##### ㊔ Naming Your Program File:

CircuitPython looks for a code file on the board to run. There are four options: `code.txt`, `code.py`, `main.txt` and `main.py`. CircuitPython looks for those files, in that order, and then runs the first one it finds. 

While `code.py` is the recommended name for your code file, it is important to know that the other options exist. 



#### 2.3: 👋🏻 Sending Message to the User - Hello World (Serial Console)

One of the staples of CircuitPython (and programming in general!) is something called a "print statement". This is a line you include in your code that causes your code to output text. A print statement in CircuitPython (and Python) looks like this:

`print("Hello, world!")`

This line in your `code.py` would result in:

`Hello, world!`

However, these print statements need somewhere to display. That's where the serial console comes in!

The serial console receives output from your CircuitPython board sent over USB and displays it so you can see it.



🔧 In the code entry section of the `Thonny` IDE, insert the updated code:

```python
import board
import digitalio
import time

# Configure GP16 as an output pin
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("Hello, CircuitPython!")
    led.value = True   # Turn off
    time.sleep(0.5)
    led.value = False  # Turn on
    time.sleep(0.5)
```

##### 🧪 Key Functions

 - `print()` - Pass a textual information to the designer with the REPL console

In the CircuitPython environment, the `print()` function serves as a simple yet indispensable debugging tool during the embedded development workflow by providing real-time feedback directly through the serial console (REPL) over USB, without the need for external hardware or debuggers. It allows designers to monitor sensor readings, input states, variable values, and program flow, making it easier to debug/diagnose issues and verify logic within the code. 



#### 2.4: Analog Output – LED Fading

Most GPIO pins on the Raspberry Pi Pico operate using **digital signals**—either ON (3.3V) or OFF (0V). However, many real-world devices require **analog signals**, which can vary smoothly over a range of values. To approximate analog behavior, we use **Pulse Width Modulation (PWM)**, a modulation technique by which the width of pulse is varied while keeping the frequency constant.

We can simulate an analog output by rapidly switching a digital signal between ON and OFF states using PWM. Adjusting the ratio of ON-time to OFF-time changes the LED brightness.




###### 0% Duty Cycle (PWM on a 0 ~ 3v3 Scale)

<svg width="600" height="100" style="zoom: 75%;" >
  <!-- 0V Line -->
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <!-- 0% duty (always low) -->
  <polyline points="
    0,80 600,80
  " fill="none" stroke="blue" stroke-width="2" />
  <!-- Voltage labels -->
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 25% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <!-- 0V Line -->
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <!-- Average voltage line at 25% -->
  <line x1="0" y1="60" x2="600" y2="60" stroke="green" stroke-width="1" stroke-dasharray="5,5" />
  <text x="80" y="55" font-size="10" fill="green">Average ~0.825V</text>
  <!-- 25% duty -->
  <polyline points="
    0,80 0,20 50,20 50,80 200,80 200,20 250,20 250,80 400,80 400,20 450,20 450,80 600,80
  " fill="none" stroke="blue" stroke-width="2" />
  <!-- Voltage labels -->
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 50% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <!-- 0V Line -->
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <!-- Average voltage line at 50% -->
  <line x1="0" y1="50" x2="600" y2="50" stroke="orange" stroke-width="1" stroke-dasharray="5,5" />
  <text x="10" y="45" font-size="10" fill="orange">Average ~1.65V</text>
  <!-- 50% duty -->
  <polyline points="
    0,80 0,20 100,20 100,80 200,80 200,20 300,20 300,80 400,80 400,20 500,20 500,80 600,80
  " fill="none" stroke="blue" stroke-width="2" />
  <!-- Voltage labels -->
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 75% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <!-- 0V Line -->
  <line x1="0" y1="80" x2="600" y2="80" stroke="black" stroke-width="1" />
  <!-- 75% duty -->
  <polyline points="
    0,80 0,20 150,20 150,80 200,80 200,20 350,20 350,80 400,80 400,20 550,20 550,80 600,80
  " fill="none" stroke="blue" stroke-width="2" />
  <!-- Voltage labels -->
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>

###### 100% Duty Cycle

<svg width="600" height="100" style="zoom: 75%;">
  <!-- 3.3V Line -->
  <line x1="0" y1="20" x2="600" y2="20" stroke="black" stroke-width="1" />
  <!-- 100% duty (always high) -->
  <polyline points="
    0,20 600,20
  " fill="none" stroke="blue" stroke-width="2" />
  <!-- Voltage labels -->
  <text x="0" y="15" font-size="12">3.3V</text>
  <text x="0" y="90" font-size="12">0V</text>
</svg>


```python
import board
import pwmio
import time

# Configure GP16 as an PWM output pin
led = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)

while True:
    for i in range(65535, 0, -512):
        led.duty_cycle = i
        time.sleep(0.01)
    for i in range(0, 65535, 512):
        led.duty_cycle = i
        time.sleep(0.01)

```

###### 🧪 Key Functions:

- `PWMOut()` - Configure a pin for PWM output
- `duty_cycle` - Controls brightness of the LED (0 = full brightness, 65535 = off, Asserted `LOW` connected LED)



### Chapter 3:

#### 3.1: Capacitive Input Interaction - Detecting Touch

The Pico Carrier board has 2 dedicated capacitive touch inputs sensing ICs. This means we can detect when a student lightly touches the touch sensitive screws with a finger.

Your body acts like a small capacitor, and the sensor chip senses this tiny change in electrical charge. In this activity, touching the touch sensitive screws will toggle the state of two LEDs on the board. This creates a simple, intuitive interaction:

- Touch Sensitive screw → MCU senses change → LED toggles ON/OFF

<img src="assets/3.1.1%20-%20Touch_Sensing.png" alt="3.1.1 - Touch_Sensing" width="500" height="auto"/>


##### 🔌 Wiring of the LED2 (GPIO17) & LED3 (GPIO18) to Pico Dev Board

LED & Cap-Touch Pinout as follows:

| LED & Cap-Touch                                      | Connect to Pico |
| -------------------------- | --------------------------- |
| **LED2**                   | **GPIO 17**     |
| **LED3**                  | **GPIO 18**     |
| **Touch1**                   | **GPIO 6**     |
| **Touch2**                  | **GPIO 7**     |

🔧 In the code entry section of the `Thonny` IDE, insert the following code:

```python
import time
import board
import digitalio

# Configure GP17 & GP18 as an output pin
led1 = digitalio.DigitalInOut(board.GP17)
led1.direction = digitalio.Direction.OUTPUT
led1.value = False

led2 = digitalio.DigitalInOut(board.GP18)
led2.direction = digitalio.Direction.OUTPUT
led2.value = False

# Configure GP6 & GP7 as an input pin, Given both pins are active-low
btn1 = digitalio.DigitalInOut(board.GP6)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP7)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

# Track last states for edge detection
last_btn1 = True  # pull-up idle = True
last_btn2 = True

print("Ready: GP6 toggles GP17, GP7 toggles GP18")

while True:
    # -------- BUTTON 1 (GP6 → GP17) --------
    current1 = btn1.value
    if last_btn1 and not current1:       # detect falling edge (press)
        led1.value = not led1.value      # toggle LED
        print("GP6 pressed → Toggle GP17")
    last_btn1 = current1

    # -------- BUTTON 2 (GP7 → GP18) --------
    current2 = btn2.value
    if last_btn2 and not current2:       # detect falling edge (press)
        led2.value = not led2.value      # toggle LED
        print("GP7 pressed → Toggle GP18")
    last_btn2 = current2

    time.sleep(0.02)  # prevent busy-wait

```

##### 🧪 Key Functions:

- `DigitalInOut(board.GPxx)` — Access a GPIO pin on the Raspberry Pico.
- `pull = Pull.UP` — Activates internal pull-up resistor, making input **idle = HIGH**, **pressed/touched = LOW**.
- **Edge detection logic** (`last_state` vs `current_state`) — Allows the program to detect a *new* touch event rather than repeated triggers.
- `led.value = not led.value` — Toggles the LED state each time a valid touch is detected.



#### 3.2: Analog Input  “Let there be Light” - Detecting ambient light intensity💡

In this activity, we will measure **ambient light brightness** using an analog light sensor connected to the RP2040’s ADC (Analog-to-Digital Converter).

The ADC reads a value between **0 → 65535**, representing voltage from **0 → 3.3V**. As the surrounding light increases, the voltage level rises. This makes it perfect for interactive environmental sensing projects.

<img src="assets/3.2.1%20-%20Light_Sensing.png" alt="3.2.1 - Light_Sensing" width="400" height="auto"/>


##### 🔌 Wiring of Light Sensor (GPIO26) to Pico Dev Board

Light-Sensor Pinout as follows:

| Light Sensor       | Connect to PICO                |
| ---------- | ------------------------------ |
| Signal | **GPIO 26**                    |

🔧 In the code entry section of the `Thonny` IDE, insert the following code:

```python
import time
import board
import digitalio
import analogio

# Configure GP17 as an output pin
led1 = digitalio.DigitalInOut(board.GP17)
led1.direction = digitalio.Direction.OUTPUT

# Configure GP26 an analog input pin
light = analogio.AnalogIn(board.GP26)

def analog_voltage(channel):
    return (channel.value * 3.3) / 65535

# Timer for 500ms reading
last_read_time = time.monotonic()

while True:

    now = time.monotonic()
    if now - last_read_time >= 0.5:  # 500 ms
        raw = light.value
        voltage = analog_voltage(light)
        print(f"Light Sensor ADC raw={raw}  approx_voltage={voltage:.3f} V")
        last_read_time = now
        
        if raw < 1000:
            led1.value = 0
        else:
            led1.value = 1

    time.sleep(0.02)  # debounce + CPU relief

```

##### 🧪 Key Functions:

- `analogio.AnalogIn(board.GP26)` — Reads analog voltage from an ADC-capable pin.
- `.value` — Returns a 16-bit ADC reading (0–65535).
- `analog_voltage()` — Converts raw ADC values into human-readable voltage (approx. 0–3.3V).
- `time.monotonic()` — Provides stable timing for periodic sensor reads (avoids issues with time resets).
- `time.sleep(0.02)` — Reduces CPU load and stabilizes readings.



### Chapter 4:

#### 4.1: OnBoard I2S DAC Amplifier & Speaker - Sound Generation

**Everyone loves making sound** (noise), **Sound & Music is produced** when an object **vibrates**, creating a varying pressure wave. This pressure wave causes particles in the surrounding medium, such as air around us, to have **vibrational** motion. 
As the particles **vibrate**, they move nearby particles, propagating the **sound** further & further away **through** the medium. 

##### 🎶 How Tone Generation Works

In the microcontroller world, **audio tones** are typically generated by toggling a GPIO pin rapidly to create a square wave. This wave will then drives a **speaker** through an **amplifier + speaker setup**, converting the electrical pulses into audible sound.

The **frequency** of the square wave determines the pitch (note), and the **duration** determines how long it plays. In CircuitPython, we use the `synthio.Synthesizer` to generate the tone and `audiobusio.I2SOut` to send this audio to your I²S DAC + amplifier



##### 🔌 Updated Wiring of the I²S Amplifier & Speaker to Raspberry Pico

Amplifier / I²S Pinout as follows:

| OnBoard I²S DAC + Amplifier & Speaker                | Connect to Raspberry Pico |
| ---------------------------------------------------- | ------------------------- |
| **I²S Bit Clock (BCLK)**                             | **GPIO 14**               |
| **I²S Word Select (LRCLK / WS)**                     | **GPIO 15**               |
| **I²S Data**                                         | **GPIO 13**               |



🔧 In the code entry section of the `Thonny` IDE, insert the following code, we will reproduce welcome melody found in a variety of TomatoCube's Creation using CircuitPython:

```python
import board
import digitalio
import time
import audiobusio
import synthio

# Create I2SOut object on GP13/14/15 for audio output
i2s = audiobusio.I2SOut(
    bit_clock=board.GP14,
    word_select=board.GP15,
    data=board.GP13
)

# Create a basic synthesizer
synth = synthio.Synthesizer(sample_rate=22050)
i2s.play(synth)

def play_tone(frequency, duration_ms):
    # Create a note on the fly
    note = synthio.Note(frequency=frequency, amplitude=0.5)
    synth.press(note)
    time.sleep(duration_ms / 1000.0)
    synth.release(note)
    time.sleep(0.01)  # Short rest between notes

# TomatoCube Welcome melody (E5, D5, F#4)
play_tone(659, 90)  # NOTE_E5
time.sleep(0.01)
play_tone(587, 90)  # NOTE_D5
time.sleep(0.01)
play_tone(370, 90)  # NOTE_FS4
time.sleep(0.01)

```



###### 🧪 Key Concepts (I²S Version)

- `I2SOut(bit_clock, word_select, data)` – Sends **digital audio** to an external I²S DAC/amplifier.
- `synthio.Synthesizer` – Generates audio waveforms for us (no manual square wave needed).
- `synthio.Note(frequency, amplitude)` – Represents one musical note at a given pitch & loudness.
- `synth.press()` / `synth.release()` – Start and stop individual notes.

Upload the above code to your SnowGlobe, and when the board starts, you should hear a short welcome jingle.



###### 📖 How the Note Corresponds to the Frequency:

The **frequency** of a note is the number of vibrations (cycles) per second that the sound wave produces. Higher frequencies correspond to higher notes, while lower frequencies correspond to lower notes.

For example:

- The **NOTE_A4** note (440 Hz) is a reference pitch used in tuning musical instruments. It is the standard pitch used to tune instruments like pianos and violins.
- Each **octave** doubles the frequency of the note. So, **NOTE_A5** (880 Hz) is the same note as **NOTE_A4**, but it is one octave higher, producing a higher pitch.
- The **NOTE_C4** (261.63 Hz) is commonly known as Middle C, and it's often used as a reference in music theory and tuning.

The table below can help you understand how the pitch of the note is related to the frequency in Hertz (Hz).

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

- The **top row** represents the **octave** (from 0 to 8).
- The **leftmost column** shows the note names, ranging from **C** to **B**.
- The values inside the table are in **Hertz (Hz)**, representing the frequency of each note across different octaves.





#### 4.2: Playing MP3 Audio with Touch

**Let’s go beyond beeps**, now it's time to play real audio clips! Using CircuitPython’s `audiomp3` and audiobusio, you can play high-quality MP3 sounds directly from your Raspberry PICO base SnowGlobe.

In this example, we’ll play either `egg-shaker.mp3` or `harp-ascending.mp3` sound clip when Cap-Touch `GP6` or `GP7`  is pressed.

##### 🎧 Get the MP3 files needed

Download this example MP3 file and save it directly into your CIRCUITPY root directory:

👉 Download [egg-shaker.mp3](assets/egg-shaker.mp3) &  [harp-ascending.mp3](assets/harp-ascending.mp3) 

> If you use your own mp3 file, please remember to rename the target mp3 filename in the source code  before uploading to your board for the code to work correctly.



🔧 In the code entry section of the `Thonny` IDE, insert the following code, 

```python
import board
import digitalio
import time

import audiobusio
import audiomp3

# Configure GP6 & GP7 as an input pin, Given both pins are active-low
btn1 = digitalio.DigitalInOut(board.GP6)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP7)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn1_value = btn1.value
old_btn1_value = btn1.value
btn2_value = btn2.value
old_btn2_value = btn2.value

# --- (C) I2S MP3 playback on GP13/14/15 ---
mp3file1 = "egg-shaker.mp3"
mp3file2 = "harp-ascending.mp3"
i2s = audiobusio.I2SOut(bit_clock=board.GP14, word_select=board.GP15, data=board.GP13)

while True:
    btn1_value = btn1.value
    btn2_value = btn2.value

    # Detect button press (falling edge)
    if not btn1_value and old_btn1_value:
        if not i2s.playing:
            print("Playing egg-shaker.mp3 via I2S...")
            with open(mp3file1, "rb") as f:
                mp3 = audiomp3.MP3Decoder(f)
                i2s.play(mp3)
                while i2s.playing:
                    time.sleep(0.05)            
        else:
            i2s.stop()
    elif not btn2_value and old_btn2_value:
        if not i2s.playing:
            print("Playing harp-ascending.mp3 via I2S...")
            with open(mp3file2, "rb") as f:
                mp3 = audiomp3.MP3Decoder(f)
                i2s.play(mp3)
                while i2s.playing:
                    time.sleep(0.05)            
        else:
            i2s.stop()

    old_btn1_value = btn1_value
    old_btn2_value = btn2_value

time.sleep(0.02)  # debounce + CPU relief        


```

🧪 Key Concepts

- `I2SOut(...)` – Outputs high-quality **digital audio** to an I²S DAC / amplifier.
- `MP3Decoder(open("xxx.mp3", "rb"))` – Decodes compressed MP3 data into raw audio samples on the fly.
- `i2s.play(decoder)` – Streams the decoded audio out over I²S.
- `decoder.file = open(mp3file, "rb")` – Rewinds the MP3 by reopening it, so the clip can be replayed.

Using the Mp3Decoder engine, the Raspberry Pico sends the decoded audio signal to the speaker through the I²S amplifier. We toggle the playback of the decoded audio by touching either the Left or the Right Screw.



### Chapter 5: 

#### 5.1: NeoPixel LED – Addressable RGB LEDs

**Nothing catches the eye like glowing LEDs!** NeoPixels are colorful, programmable RGB LEDs that allow you to display **millions of colors** by adjusting the brightness of red, green, and blue channels. These LEDs are popular in wearables, keyboards, and creative lighting projects as RGB lighting strips.

In our X'MAS SnowGlobe Table-Top Toy, we have 3 **dedicated RGB NeoPixel**, the big Star on the tree being the first NeoPixel and 2 more are illuminating the acrylic diffuser of the SnowGlobe

##### 🌈 How NeoPixels Work

NeoPixels (WS2812-type LEDs) are **intelligent RGB LEDs** (IC controller build-in) that can be daisy-chained. Each LED listens to a **precise digital timing signal** and updates its color based on the received data. Once the data is Passed & Processed, it automatically shifts the rest of the data down the chain to the next pixel.

<img src="assets/5.1.1 - NeoPixel_die.png" alt="5.1.1 - NeoPixel_die" width="300" height="auto"/>


In CircuitPython, we use the `neopixel` library, which handles all the timing for us.

You just:

- Specify the pin and number of LEDs
- Set brightness
- Call `.fill()` or assign individual colors using `.pixels[n] = (R, G, B)`

>💡 Note: 
>One can read more about the data protocol from the [WS2812b official data-sheet](https://github.com/TomatoCube18/Lattice_FPGA_MacroKeys/blob/main/Relevant_Docs_DataSheets/WorldSemi-WS2812B-Mini.pdf)




##### 📦 Install NeoPixel Library

1. Download the [CircuitPython Library Bundle](https://circuitpython.org/libraries), we will be using the zip file under "Bundle for Version 10.x".
2. From the bundle *`lib/`* folder, copy:
   - `neopixel.mpy` & `adafruit_pixelbuf.mpy` → to `CIRCUITPY/lib/`  
     *(Create a `lib/` folder if it doesn’t exist)*

Your `CIRCUITPY/lib/` folder should now contain:

```bash
/lib/
├── adafruit_pixelbuf.mpy
├── neopixel.mpy
└── ...
```

Without these, you'll get errors when trying to run `neopixel` code.



##### 🔌 Wiring of NeoPixels to Raspberry Pico

NeoPixel Signal Input:

| NeoPixel Input                       | Connect to Raspberry Pico |
| ------------------------------------ | ------------------------- |
| **DIN ** (via voltage level shifter) | **GPIO 20**               |
| **+5V **                             |                           |
| **GND **                             |                           |

>  💡 Note:
>  The NeoPixels are powered by **5V** (USB voltage), 



##### ⚠️ Why Level Shift the Signal is needed?

NeoPixels **operate at 5V logic levels**, but the Raspberry Pico outputs signals at **3.3V**. While some NeoPixels might *kind of* work with 3.3V signals, **reliable operation is not guaranteed**.

To solve this, the signal from the Raspberry Pico (GPIO20) is passed through a **voltage level shifter** to shift it from **3.3V to 5V** on the SnowGlobe peripheral board, ensuring solid and reliable communication with the NeoPixels.

> 💡 Note: 
> Without level-shifting, you may see flickering or non-functional LEDs.



🔧 In the code entry section of the `Thonny` IDE, insert the following code, we will make the keys glow blue, then off, repeatedly (Effectively, a fancy Blink):

```python
import board
import neopixel
import time

pixel_pin = board.GP20
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=True)

while True:
    pixels.fill((0, 0, 255))  # Blue
    time.sleep(0.5)
    pixels.fill((0, 0, 0))    # Off
    time.sleep(0.5)

```

##### 🧪 Key Concepts

- `NeoPixel(pin, count)` – Initializes the LED chain
- `.fill((R, G, B))` – Set color for all LEDs at once
- `.brightness` – Controls the maximum brightness
- `auto_write=True` – Changes apply immediately

With NeoPixels, you can create animated effects, custom color states for keys, or even light-based feedback for macros. The possibilities are endless!



#### 5.2: Controlling individual Neopixels

##### 💫 Concept: List-Base NeoPixel Control

To light an **individual NeoPixel**, you use **indexing** with the NeoPixel object. Each LED in the chain is addressed starting from index `0`.

Here’s the structure:

```python
pixels[index] = (R, G, B)
```

- `index` = which LED (0 to n-1)
- `(R, G, B)` = the color tuple (0–255 per channel)


🔧 In the code entry section of the `Thonny` IDE, update with the following code:

```python
import board
import neopixel
import time

pixel_pin = board.GP20
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=True)

while True:
    for i in range(3):
        pixels[i] = (255, 0, 255)  # Purple
        time.sleep(0.2)
        pixels[i] = (0, 0, 0)    # Turn off

```

This🕺 disco code above will light each LED **one at a time**, with a cool purple flash🍆.

> 💡 Note:
>
> if `auto_write` is disabled, you will need to invoke `pixels.show()` to request a refresh of the NeoPixels LED color. Disabling auto write would give greater control over the sequencing of the NeoPixels.



#### 5.3: Aurora Ambient Lighting – Colors of the Northern Lights

Instead of lighting NeoPixel LEDs with a solid color and doing some simple strobbing effect. Now Imagine relaxing as the ambient lighting mimics the ever-changing colors of the Northern Lights. 

Using the on-board NeoPixels, we will now create a smooth, fading transition between colors inspired by the aurora borealis. Below is a sample color palette with the corresponding color hex codes:

**Aurora Color Palette (Lakeside Aurora Borealis)** (Reference: [paperheartdesign](https://paperheartdesign.com/blog/color-palette-northern-lights))

- \#1d1640
- \#3d276f
- \#001d83
- \#39977f
- \#b4dac3

<img src="https://camo.githubusercontent.com/0c321b004cf9b7f4421f4230af473698f00809ec7d378015d41784998d0a9141/68747470733a2f2f696d616765732e73717561726573706163652d63646e2e636f6d2f636f6e74656e742f76312f3537323065646535353535393836623136663134363634322f39663662666238352d313334312d346663662d616635622d3035636531626532623837652f4e6f72746865726e2b4c69676874732b342e6a70673f666f726d61743d3235303077" alt="LakeSide Aurora" width="500" height="auto"/>





🔧 In the code entry section of the `Thonny` IDE, update with the following code:

```python
import board
import neopixel
import time

# NeoPixel setup
pixel_pin  = board.GP20
num_pixels = 3
pixels     = neopixel.NeoPixel(pixel_pin, num_pixels,
                               brightness=0.4,
                               auto_write=False)

# A little aurora-inspired palette of greens/blues/teals
aurora_palette = [
    ( 29,  22,  64),   # #1d1640
    ( 61,  39, 111),   # #3d276f
    (  0,  29, 131),   # #001d83
    ( 57, 151, 127),   # #39977f
    (180, 218, 195),   # #b4dac3
#     (  0,  30,  60),
#     (  0,  90, 120),
#     (  0, 150, 200),
#     ( 20, 200, 255),
#     ( 80, 255, 200),
#     (  0, 200, 120),
]

# Build a smooth gradient between each pair
gradient = []
steps_per_segment = 20  # more steps = smoother

for start, end in zip(aurora_palette, aurora_palette[1:]):
    sr, sg, sb = start
    er, eg, eb = end
    for step in range(steps_per_segment):
        t = step / steps_per_segment
        # linear interpolation for each channel:
        r = int(sr + (er - sr) * t)
        g = int(sg + (eg - sg) * t)
        b = int(sb + (eb - sb) * t)
        gradient.append((r, g, b))

# close the loop back to the first color so the animation cycles smoothly 
first = aurora_palette[0]
last  = aurora_palette[-1]
for step in range(steps_per_segment):
    t = step / steps_per_segment
    r = int(last[0] + (first[0] - last[0]) * t)
    g = int(last[1] + (first[1] - last[1]) * t)
    b = int(last[2] + (first[2] - last[2]) * t)
    gradient.append((r, g, b))

# Now `gradient` should have 100 colors smoothly blended together to form the aurora.

offset = 0
delay  = 0.05  # seconds per frame (tweak to speed up/slow down)

while True:
    # Light up each of the 6 pixels from a different point in the gradient
    for i in range(num_pixels):
        idx = (offset + i) % len(gradient)
        pixels[i] = gradient[idx]
    pixels.show()

    # Move the “window” along the gradient
    offset = (offset + 1) % len(gradient)
    time.sleep(delay)


```

Feel free to change or add more colors to `aurora_palette` or tweak `delay` for a different look & feel! Now Sit back & Relax 💤





### Chapter 6:

#### 6.1: I²C Bus & Controlling the OLED display

##### 6.1.1: 🐙 I²C Expansion Bus

**I²C** (Inter-Integrated Circuit) is a two-wire serial communication protocol invented by **Philips Semiconductor** (now NXP) in the early 1980s. It is widely used to connect low-speed peripherals like sensors, displays, and EEPROMs to microcontrollers.

I²C stands out because it allows **multiple devices** (both masters and slaves) to share the same two communication lines.



##### 6.1.2: SSD1306-based OLED Display

OLED screens allow the Raspberry Pi Pico to *show* information instead of only blinking LEDs. This enables richer interactions: menus, sensor values, animations, and user instructions. In this chapter, students will learn how to initialize and draw text on a small I²C OLED display using CircuitPython.


##### 📦 Install OLED Display Library

1. Download the [CircuitPython Library Bundle](https://circuitpython.org/libraries), we will be using the zip file under "Bundle for Version 10.x".
2. From the bundle *`lib/`* folder, copy:
   - `adafruit_bus_device`, `adafruit_display_text` & `adafruit_displayio_ssd1306.mpy` → to `CIRCUITPY/lib/`  
     *(Create a `lib/` folder if it doesn’t exist)*

Your `CIRCUITPY/lib/` folder should now contain:

```bash
/lib/
├── adafruit_bus_device
├── adafruit_display_text
├── adafruit_displayio_ssd1306.mpy
└── ...
```

Without these, you'll get errors when trying to run `OLED` code.



##### 🔌 Wiring of the I2C OLED (GPIO4 & 5) to Pico Dev Board

This X'mas SnowGlobe project uses an SSD1306-based OLED panel with a resolution of 128×64 pixels on the Peripheral board.

I²C uses just two wires with a supply `+3v3` with `ground`:

- **SCL (Serial Clock Line)** — Clock signal generated by the master.
- **SDA (Serial Data Line)** — Bi-directional data line.

| OLED Pin | Connect to Pico |
| -------- | --------------- |
| SDA      | **GP4**         |
| SCL      | **GP5**         |
| VCC      | 3.3V            |
| GND      | GND             |

CircuitPython’s `displayio` library handles the drawing system, while `adafruit_displayio_ssd1306` manages the display hardware.



#### 6.2: Initializing the OLED Display

Before the OLED can be used, CircuitPython must:

1. Release old display connections
2. Initialize the I²C bus
3. Scan for connected I²C devices (optional but useful for debugging)
4. Create the SSD1306 display object
5. Create a display “group” to contain text and graphics



#### 6.3: OLED Example – "Hello World!"


```python
import board
import busio

import displayio
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306

# --- I2C on GP4/GP5 ---
# Release any existing displays to avoid conflicts
displayio.release_displays()

i2c = busio.I2C(board.GP5, board.GP4)    # Pi RP2040 MacroKeyPad
while not i2c.try_lock():
    pass
try:
    print(	
        "I2C devices with addresses found:",
        [hex(device_address) for device_address in i2c.scan()],
    )
finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()

# Create the SSD1306 OLED class.
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT, rotation=180)
# Our Peripheral board OLED defaulted its I2C addresses to 0x3C. Adjust 'addr' if necessary.

# Make the display context
splash = displayio.Group()
display.root_group = splash
# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
splash.append(text_area)

```



##### 🧪 Key Concepts

- **`displayio.release_displays()`** – Resets any previously active displays so the OLED can initialize cleanly.
- **`busio.I2C(board.GP5, board.GP4)`** – Creates the I²C connection on pins **GP5 (SCL)** and **GP4 (SDA)**, used to communicate with the OLED.
- **`I2CDisplayBus(i2c, device_address=0x3C)`** – Connects the SSD1306 OLED driver to the Pico via its I²C address (usually **0x3C**).
- **`displayio.Group()`** – A “canvas” that holds everything drawn on the screen—text, shapes, animations.
- **`label.Label(terminalio.FONT, text="Hello")`** – Creates a text object that can be positioned anywhere on the display.

These concepts allow you to draw text and graphics on the OLED, creating visual feedback for touch inputs, menus, alerts, or real-time sensor values. Once mastered, the OLED becomes a powerful output tool that brings your project to life!





#### 6.4: What Students Can Try Next

Once the screen is working, students can explore:

##### ✔ Changing text

```
text_area.text = "New Message!"
```

##### ✔ Moving text around

```
text_area.x = 0
text_area.y = 10
```

##### ✔ Showing sensor readings (e.g., temperature, touch state)





###  **Chapter 7: **



#### **7.1: What Is an Real-Time Clock (RTC) and Why Do We Need One?**

Many electronics projects need **accurate timekeeping** - for logging data, alarms, reminders, or timed automation.
Microcontrollers like the Raspberry Pi Pico do *not* keep accurate time by themselves: when power is lost, the internal clock resets.

To solve this, engineers use an **RTC (Real-Time Clock)** chip with a **backup battery**.

One of the most reliable and popular modules, and also the prefered module for our X'mas SnowGlobe is the **DS3231**, a temperature-compensated RTC that keeps extremely accurate time, even over months or years.
Thanks to its onboard **backup battery** included on the module, the DS3231 continues ticking even when the main board is powered off.

<img src="assets/7.1.1%20-%20RTC-3231.jpg" alt="7.1.1 - RTC-3231" width="300" height="auto"/>



##### 📦 Install DS3231 RTC Library

1. Download the [CircuitPython Library Bundle](https://circuitpython.org/libraries), we will be using the zip file under "Bundle for Version 10.x".
2. From the bundle *`lib/`* folder, copy:
   - `adafruit_ds3231.mpy` → to `CIRCUITPY/lib/`  
     *(Create a `lib/` folder if it doesn’t exist)*

Your `CIRCUITPY/lib/` folder should now contain:

```bash
/lib/
├── adafruit_ds3231.mpy
└── ...
```

This library allows you to:

- Read the current time and date
- Set the time once on initial setup
- Read temperature from the RTC’s internal sensor
- Use alarm functions (optional advanced topic)

Without it, you'll get errors when trying to run `RTC` code.



##### 🔌 Wiring of the I2C Real-Time Clock (RTC) (GPIO4 & 5) to Pico Dev Board

Just like the OLED display discuessed in Chapter 6, the DS3231 communicates using the **I²C bus**.
This means it shares the same **SDA** and **SCL** lines, allowing multiple devices to be connected at once.


<img src="assets/7.1.2%20-%20RTC-location.png" alt="7.1.2 - RTC-location" width="700" height="auto"/>


The module used in this project is a standard commonly available **DS3231 RTC module**, and the Raspbery Pico carrier board includes a **pre-installed pin-header** where the student plugs the RTC module directly.

### **RTC I²C Connection Pins**

| DS3231 Pin | Connects to Pico |
| ---------- | ---------------- |
| SDA        | **GP4**          |
| SCL        | **GP5**          |
| VCC        | 3.3V             |
| GND        | GND              |

Both the OLED (SSD1306) and DS3231 live together on the same I²C bus.
CircuitPython handles this automatically—they simply have different I²C **addresses**.

I²C addresses of the components:

- **SSD1306 OLED** → `0x3C`
- **DS3231 RTC** → `0x68`



#### **7.2: Accessing the RTC Over I²C**

Because the DS3231 shares the same I²C bus as the OLED, the initialization steps look familiar:

1. Create an I²C object
2. Scan the bus for devices
3. Create the DS3231 object using that I²C connection

The RTC becomes accessible as a Python object that behaves like a clock.



#### **7.5: Example – Reading and Displaying the Current Time**

This example:

- Initializes I²C
- Connects to the DS3231
- Reads the time each second
- Displays it on the OLED

```python
import time
import board
import busio

import displayio
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306
import adafruit_ds3231

# --- I2C SETUP ON GP4/GP5 ---
displayio.release_displays()
i2c = busio.I2C(board.GP5, board.GP4)

# Scan for devices (optional, good for debugging)
while not i2c.try_lock():
    pass
print(
    "I2C devices found:",
    [hex(device_address) for device_address in i2c.scan()]
)
i2c.unlock()

# --- OLED DISPLAY INITIALIZATION ---
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32, rotation=180)

splash = displayio.Group()
display.root_group = splash

clock_label = label.Label(terminalio.FONT, text="Current Time:", color=0xFFFFFF, x=20, y=13)
splash.append(clock_label)
time_label = label.Label(terminalio.FONT, text="--:--:--", color=0xFFFFFF, x=20, y=25)
splash.append(time_label)

# --- RTC INITIALIZATION ---
rtc = adafruit_ds3231.DS3231(i2c)

# Uncomment this line ONLY ONCE to set the RTC:
# rtc.datetime = time.struct_time((2025, 1, 1, 12, 0, 0, 0, -1, -1))

# --- MAIN LOOP ---
while True:
    now = rtc.datetime  # Read time from DS3231
    time_str = "{:02}:{:02}:{:02}".format(now.tm_hour, now.tm_min, now.tm_sec)
    time_label.text = time_str
    time.sleep(1)

```



#### 🧪 **Key Concepts**

- **RTC stands alone**
  Thanks to its battery, the DS3231 keeps time even when the system is powered off.
- **Shares I²C bus with OLED**
  Multiple devices → one bus → unique addresses.
- **Reading Time**
  `rtc.datetime` returns a `time.struct_time` object.
- **Setting Time (Run Once!)**
  You only need to set the time the first time you install the battery.
  After that, the RTC keeps time permanently.
- **Temperature Sensor**
  The DS3231 also includes a surprisingly accurate temperature reading:
  `rtc.temperature`

