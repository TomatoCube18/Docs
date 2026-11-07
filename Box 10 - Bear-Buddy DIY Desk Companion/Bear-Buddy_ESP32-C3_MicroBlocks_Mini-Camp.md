## 🐻 ESP32-C3 Bear-Buddy D.I.Y Desktop Companion - MicroBlocks Mini-Camp



Last Updated: 7th Nov 2026


### Chapter 1:

#### 1.1: Introduction to MicroBlocks Programming

In this mini-camp, we will learn **MicroBlocks** using the **Bear-Buddy**, a solder-it-yourself desk companion built around the **ESP32-C3 SuperMini** board! This is a hands-on heavy, easy to follow guided workshop for **complete beginners** - no typing, no syntax errors, just snapping blocks together. If you have used **Scratch** before, you're already ahead! Now it's time to make your blocks interact with the real world: **Buttons**, **LEDs**, **Sound**, a glowing **NeoPixel matrix**, an **Infrared remote**, and so much more.

By the end of this guide, you'll be able to program your **fully assembled Bear-Buddy** complete with lights, sound, a scrolling pixel face, controllable via a remote control, and even use it as a clock using an I²C character display.

#### 1.2: What is MicroBlocks?

**MicroBlocks** is a free, blocks-based programming language designed for physical computing on microcontrollers. It looks a lot like Scratch, but your scripts run **directly on Bear-Buddy**, not on your computer.

##### 🔑 Key Features:

- **Live coding:** Click a block and Bear-Buddy runs it *instantly*, even while other scripts are running. No compiling, no uploading, no waiting.
- **Runs on the board:** Your program is stored on Bear-Buddy itself. Unplug the USB, power it from a power bank, and it keeps running.
- **Multitasking built in:** Each script runs at the same time as the others. Blinking an LED *and* playing music *and* reading buttons is easy.
- **Strong library support:** NeoPixels, tones, ringtones, IR remotes, I²C devices, displays and more, added with a couple of clicks.

##### 🧩 MicroBlocks vs Scratch vs CircuitPython

| | Scratch | MicroBlocks | CircuitPython |
|---|---|---|---|
| Where does the code run? | On your computer | On Bear-Buddy | On Bear-Buddy |
| How do you write it? | Blocks | Blocks | Typed text (Python) |
| Do I need to save/upload? | - | No, changes are live | Yes, save `code.py` |
| Multiple things at once? | Yes | Yes, every script runs in parallel | Needs careful loop design |

MicroBlocks is the **first step** of the Bear-Buddy learning path. Once you are comfortable here, the **CircuitPython Mini-Camp** covers the *exact same projects* in typed Python code, so you can compare the two side by side.

##### 📖 How Blocks Are Written in This Guide

Screenshots show each script, but we also write the blocks out as text so they are easy to read and copy. Indentation shows which blocks sit *inside* another block (like the mouth of a `forever` or `if` block). Inputs are written as:

| Notation | Meaning | Example |
|---|---|---|
| `( )` | A number slot | `wait (500) millisecs` |
| `< >` | A true/false slot | `set digital pin (3) to <true>` |
| `[ ]` | A text slot or dropdown | `say [Hello!]` |

#### 1.3: Meet Bear-Buddy & Its Peripherals

Everything on Bear-Buddy is already wired to a fixed predefined pin on the ESP32-C3, so there is no breadboard wiring to get wrong, you just use the right pin number in your blocks. In MicroBlocks, the **pin number is the GPIO number**, so `IO3` is simply pin `3`. Here is the full map we will use:

| Peripheral                           | ESP32-C3 Pin(s)        | MicroBlocks pin number |
| ------------------------------------ | ---------------------- | ---------------------- |
| **Simple LED**                       | `IO3`                  | `3`                    |
| **Button A** (also BOOT / strap)     | `IO9`                  | `9`                    |
| **Button B**                         | `IO4`                  | `4`                    |
| **Buzzer**                           | `IO10`                 | `10`                   |
| **NeoPixel 5×5 Matrix** (serpentine) | `IO7`                  | `7`                    |
| **IR Receiver**                      | `IO21`                 | `21`                   |
| **I²C bus**                          | `SDA = IO5`, `SCL = IO6` | handled automatically |

![1.3.1 - BearBuddy_Pinout](assets/1.3.1%20-%20BearBuddy_Pinout.png)

> 💡 Note:
> Keep this table handy. Whenever a chapter says "pin 7", it is talking about one of the pins above.

#### 1.4: Meet the ESP32-C3 Supermini board

Bear-Buddy's "brain" is a tiny off-the-shelf **ESP32-C3 SuperMini** development board, soldered onto the bear PCB through its pin headers. Smaller than a postage stamp, it still packs a surprising amount:

- A **32-bit RISC-V** processor running at up to **160 MHz**
- **Wi-Fi** and **Bluetooth LE** radios on board (your gateway to IoT later!)
- A **USB-C** connector for power, flashing, and talking to the MicroBlocks IDE
- 400 KB SRAM and 4 MB of flash storage

Every Bear-Buddy peripheral is wired to a fixed pin (see §1.3), but it is worth knowing the three things already on the SuperMini *itself*: two buttons and an LED. You'll use all three during this camp.

##### 🔘 The Two Onboard Buttons: BOOT and RESET

On the SuperMini you'll find two small tactile buttons, usually marked **BOOT** (or **B** / **IO9**) and **RST** (or **RESET** / **R**).

| Button    | Connected to          | What it does                                                 |
| --------- | --------------------- | ------------------------------------------------------------ |
| **RESET** | `EN` (chip enable)    | Restarts the board instantly and re-runs every `when started` script, like switching it off and on again. |
| **BOOT**  | `IO9` (strapping pin) | Held *during* reset / power-up, it drops the chip into **download mode** so new firmware can be flashed (see §2.2). While your program is already running, it is just an ordinary push-button. |

> 💡 Note:
> On Bear-Buddy, **Button A and the onboard BOOT button are the same pin (`IO9`)**, they are wired together. So "press Button A" and "press the SuperMini's BOOT button" do exactly the same thing. That is why §2.2 can say "hold Button A" to enter download mode.

Two handy habits for the whole camp:

- **Program acting weird? Click the red STOP sign** in the MicroBlocks IDE, or **tap RESET** on the board.
- **Need to re-flash or recover a stuck board?** Hold BOOT (Button A), tap RESET (or replug USB), then release BOOT.




### Chapter 2:

#### 2.1: MicroBlocks Quick Start Guide

##### 2.1.1: 🧰 What You'll Need to get started:

- Your assembled **Bear-Buddy** (with an installed ESP32-C3 SuperMini development board)
- A **USB-C** cable (a *data* cable, not charge-only)
- **Google Chrome** or **Microsoft Edge** on a laptop or desktop
- The MicroBlocks IDE, either:
  - the **online editor** at https://microblocks.fun/run (nothing to install), *or*
  - the **desktop app** from https://microblocks.fun/download (Windows, macOS, Linux)
- The **TomatoCube ESP32-C3 Firmware Flasher** at https://tomatocube.com/file_dir/misc_files/ESP32-C3_Flasher/

#### 2.2: 🚀 Install MicroBlocks on the ESP32-C3

MicroBlocks needs a small piece of firmware (the **MicroBlocks virtual machine**) on Bear-Buddy before the IDE can talk to it. Use the TomatoCube build: it already knows where Bear-Buddy's LED, buttons, I²C bus and NeoPixel matrix are.

##### 🔘 Entering Download (Bootloader) Mode

Some computers need the board put into download mode before flashing:

1. Press and **hold Button A (`IO9` / BOOT)**.
2. While still holding it, plug the USB-C cable in (or tap the RESET button).
3. Release **Button A**.

The board is now waiting to receive firmware.

##### Flashing with the Web Loader

1. Open **Google Chrome** or **Microsoft Edge** (they support Web Serial).
2. Go to the **TomatoCube ESP32-C3 Firmware Flasher** at https://tomatocube.com/file_dir/misc_files/ESP32-C3_Flasher/
3. **Which board do you have?** - choose the **5x5 NeoPixel matrix** version (Bear-Buddy).
4. **What should it run?** - choose **MicroBlocks**.
5. Tick **Erase everything first** if the board previously ran CircuitPython or MicroPython.
6. Press **Flash firmware**, pick the serial port, and wait for **100%**.
7. Tap **RESET** (or unplug and replug).

✅ When it finishes, Bear-Buddy is running MicroBlocks and is ready to connect.

> 💡 Note:
> Always use the **TomatoCube** MicroBlocks build from the web loader. A generic ESP32-C3 build won't know that the NeoPixel matrix lives on pin 7 or that Button B is on pin 4.

#### 2.3: Connecting to the MicroBlocks IDE

1. Plug Bear-Buddy into your computer with the USB-C cable.
2. Open the MicroBlocks IDE (https://microblocks.fun/run, or the desktop app).
3. Close any other program using the board (Thonny, Arduino IDE, the web flasher tab, a serial monitor).
4. Click the **USB / connect icon** at the top of the IDE. In the browser version, a pop-up appears: choose your board's serial port (e.g. *USB JTAG/serial debug unit*) and click **Connect**.
   ![2.3.0 - MB_Connect](assets/2.3.0%20-%20MB_Connect.png)
5. When the connection succeeds, the icon gets a **green circle** and the board name appears in the IDE.

![2.3.1 - MB_Connect_Full](assets/2.3.1%20-%20MB_Connect_Full.png)

##### 🗺️ A Quick Tour of the IDE

![2.3.2 - MB_IDE_Tour](assets/2.3.2%20-%20MB_IDE_Tour.png)

| Area | What it is |
|---|---|
| **Categories** (left) | Output, Input, Pins, Comm, Control, Operators, Variables, My Blocks... |
| **Palette** | The blocks in the selected category. Drag them out to use them. |
| **Scripting area** (middle) | Where you build your scripts. |
| **Libraries** (bottom left) | Extra block sets. Click **+** next to *Libraries* to add more. |
| **Start (green flag) / Stop (red sign)** (top right) | Start runs every `when started` script. Stop halts everything. |

> 💡 Note:
> **There is no "upload" step in MicroBlocks.** Every block you add is sent to Bear-Buddy straight away and stored there. When you unplug and plug back in later, your program is still on the board and starts by itself. To keep a copy on your computer as well, use **File > Save** (this saves a `.ubp` project file).

#### 2.4: ⭐ Adding Libraries

The basic categories cover pins, timing and logic. For things like the buzzer melodies, NeoPixels or the IR remote, we add a **library**. This is the MicroBlocks equivalent of uploading `.mpy` files in CircuitPython, but it is just a couple of clicks:

1. In the bottom left of the IDE, click the **+** next to **Libraries**.
2. The library browser opens. Libraries are grouped in folders (e.g. *Sound*, *Displays*, *Input*, *Other*).
3. Click a library to see a description, then click **Open** (or double-click it).
4. Its blocks now appear under **Libraries** in the category list.

![2.4.1 - MB_Add_Library](assets/2.4.1%20-%20MB_Add_Library.png)

Each later chapter simply says *"add the **X** library (see §2.4)"*. The libraries you add are saved with your project.

#### 2.5: 👋🏻 Digital Output / Hello-World - Blinking the LED (IO3)

Before we embark on the full journey, we will do a quick test to verify that both hardware and software are set up correctly. Let's start with the **Hello-World of the embedded world**: blinking the LED on `IO3`.

![2.5.1 - LED_Location](assets/2.5.1%20-%20LED_Location.png)

##### 📍 LED Pin Mapping

| Bear-Buddy | ESP32-C3 Pin | MicroBlocks |
| ---------- | ------------ | ----------- |
| User LED   | **IO3**      | pin `3`     |

🔧 Build this script. `when started` is in **Control**, `set digital pin` is in **Pins**, and `wait` is in **Control**:

![2.5.2 - MB_Blink](assets/2.5.2%20-%20MB_Blink.png)

```text
when started
  forever
    set digital pin (3) to <true>
    wait (500) millisecs
    set digital pin (3) to <false>
    wait (500) millisecs
```

Click the script (or the green **Start** flag). A **yellow glow** appears around it while it is running, and the LED on **IO3** should blink every half-second!

##### 🧪 Key Blocks:

- `when started` - Runs this script whenever Bear-Buddy powers up, resets, or you click the green flag.
- `forever` - Repeats the blocks inside it, over and over.
- `set digital pin (3) to <true/false>` - `true` is `HIGH` or 3.3V, `false` is `LOW` or 0V.
- `wait (500) millisecs` - Pause for 500 milliseconds (half a second).

> 💡 Note:
> Try changing `500` to `100` *while the script is running*. The blink speeds up immediately - that is live coding!

> 💡 Note:
> If your LED turns on when you expect it off (and vice-versa), it is wired **active-low**. Just swap the `true`/`false` values.

#### 2.6: 👋🏻 Sending a Message to the User - Hello World (say & graph)

One of the staples of programming is showing a message so you know what your program is doing. In MicroBlocks, the `say` block (in **Output**) shows a **speech bubble** next to the script in the IDE.

🔧 Update the script:

![2.6.1 - MB_HelloMicroBlocks](assets/2.6.1%20-%20MB_HelloMicroBlocks.png)

```text
when started
  forever
    say [Hello, MicroBlocks!]
    set digital pin (3) to <true>
    wait (500) millisecs
    set digital pin (3) to <false>
    wait (500) millisecs
```

##### 🧪 Key Blocks

- `say [ ]` - Shows a value in a speech bubble in the IDE. Drop *any* block into it (a variable, a sensor reading, a calculation) to see its value.
- `graph ( )` - (also in **Output**) Sends a number to the **graph** window (click the graph icon in the IDE). Great for watching values change over time.

Just like `print()` in Python, `say` is an indispensable debugging tool: it gives real-time feedback over USB with no extra hardware, letting you check input states, counters and program flow.

> 💡 Note:
> You can also click any **reporter** (rounded) block on its own, e.g. `read digital pin (4)`, and MicroBlocks shows its current value right there. Try it with the buttons in Chapter 3!

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

In MicroBlocks, the PWM block is `set pin ( ) to ( )` in **Pins**. It takes a value from **0** (always off) to **1023** (always on). We'll use a **variable** called `brightness` (make it in **Variables > Add a variable**):

![2.7.1 - MB_Fade](assets/2.7.1%20-%20MB_Fade.png)

```text
when started
  forever
    for (brightness) in (range (0) to (1023) by (16))
      set pin (3) to (brightness)
      wait (10) millisecs
    for (brightness) in (range (0) to (1023) by (16))
      set pin (3) to (1023 - brightness)
      wait (50) millisecs
```

###### 🧪 Key Blocks:

- `set pin (3) to (n)` - PWM output, `0` = off, `1023` = full brightness (for an active-high LED).
- `for (i) in (range ...)` - Counts through a range of numbers, running the blocks inside once for each value. (`range` is in **Data** / **Lists**; you can also simply use `for (i) in (100)` to count 1 to 100.)

> 💡 Note:
> Compare this to CircuitPython, where `duty_cycle` runs from 0 to 65535. Same idea, different scale.



#### 2.8: 💡 The ESP32-C3 Supermini Onboard LED - Your Free Second Debug LED

The SuperMini also carries its own small **LED on `IO8`**, which is *separate* from Bear-Buddy's Simple LED on `IO3`. That means you actually have **two** LEDs to play with: the big one on the bear's body (`IO3`) and this tiny one on the brain board (`IO8`). The onboard one makes an excellent **second debugging indicator**, e.g. blink `IO8` to signal "this script just ran" while `IO3` shows something else.

One quirk: the onboard LED is wired **active-low**, so you turn it **on** by driving the pin **LOW** (`false`) and **off** by driving it **HIGH** (`true`), the opposite of what you might expect.

![2.8.1 - MB_Blink_OnBoard](assets/2.8.1%20-%20MB_Blink_OnBoard.png)

```text
when started
  forever
    set digital pin (8) to <false>     -- LOW  = LED ON  (active-low)
    wait (500) millisecs
    set digital pin (8) to <true>      -- HIGH = LED OFF
    wait (500) millisecs
```

> 💡 Note:
> MicroBlocks also has a ready-made `set user LED <true>` block in **Output**. On the TomatoCube build it drives the board's user LED for you, so you don't have to remember the pin number or whether it is active-low.

Because MicroBlocks runs **every script at the same time**, try building the §2.5 blink script *and* this one, with different `wait` times. Click the green flag: both LEDs blink at their own speed, with no extra effort. That trick is much harder in CircuitPython!

There is usually a second, **always-on** LED (often red) near the USB-C port, that one is just the **power indicator** and isn't programmable.



### Chapter 3:

#### 3.1: Digital Input - Reading the Buttons

Bear-Buddy has two tactile push-buttons. In this activity, each button does something different, a simple, intuitive interaction:

- Press Button → MCU senses the change → LED toggles ON/OFF

![3.1.1 - Buttons_Location](assets/3.1.1%20-%20Buttons_Location.png)

##### 📍 Button Pin Mapping

| Button       | ESP32-C3 Pin | MicroBlocks block |
| ------------ | ------------ | ----------------- |
| **Button A** | **IO9**      | `button A`        |
| **Button B** | **IO4**      | `button B`        |

On the TomatoCube build, the **Input** category's `button A` and `button B` blocks already know which pins the buttons are on, and that they are **active-low**. They simply report `true` while the button is pressed.

> 💡 Note:
> **Button A *is* the SuperMini's onboard BOOT button** (both are `IO9`, see §1.4). So whatever you build for Button A here, the little BOOT button on the brain board does the exact same thing.

##### 3.1.1: The Easy Way - Event Hat Blocks

MicroBlocks has **hat blocks** that wait for something to happen. We'll use a variable `led on` to remember the LED's state:

![3.1.2 - MB_Buttons_Hat](assets/3.1.2%20-%20MB_Buttons_Hat.png)

```text
when started
  set (led on) to <false>
  set digital pin (3) to (led on)

when <button A> pressed
  set (led on) to <not (led on)>
  set digital pin (3) to (led on)
  say [Button A pressed -> LED toggled]

when <button B> pressed
  say [Button B pressed!]
```

Press the buttons and watch the LED and the speech bubbles.

##### 3.1.2: Under the Hood - Reading the Pins Yourself

The `button A` block is a handy shortcut. Here is what it does for you, using the raw **Pins** blocks:

![3.1.3 - MB_Buttons_Raw](assets/3.1.3%20-%20MB_Buttons_Raw.png)

```text
when started
  forever
    if <not (read digital pin (4) pull (up))>
      say [Button B is held down]
    else
      say [ ]
    wait (20) millisecs
```

Because the button is **active-low**, the pin reads `true` (HIGH) when idle and `false` (LOW) when pressed, so we flip it with `not`.

##### 🧪 Key Blocks:

- `when <button A> pressed` - Hat block: runs its script **once per press** (it waits for a fresh press, so you don't need to handle "edges" yourself).
- `button A` / `button B` - Reporter: `true` while the button is held.
- `read digital pin (4)` - Reads a pin directly, `true` = HIGH, `false` = LOW.
- `not < >` - Flips true to false and vice versa.
- `when < >` (in **Control**) - A general hat block: runs whenever *any* condition becomes true.

> 💡 Note:
> **Button A doubles as the BOOT pin.** Pressing it *during power-up / reset* puts the board into flashing mode. Pressing it while your program is already running is perfectly safe and just acts as a normal button.

### Chapter 4:

#### 4.1: The Buzzer - Making Sound

**Everyone loves making noise!** Sound is produced when something **vibrates**, creating pressure waves in the air. Bear-Buddy has a buzzer on `IO10` that we can drive to make tones and melodies.

![4.1.1 - Buzzer_Location](assets/4.1.1%20-%20Buzzer_Location.png)

##### 🎶 How Tone Generation Works

Bear-Buddy uses a single **passive** buzzer to create tone. We make a tone by sending it a **square wave**. The **frequency** of that square wave sets the **pitch**, and how long we leave it running sets the **duration**. The **Tone** library takes care of the square wave for us.

##### 📦 Add the Tone Library

Using **§2.4**, add the **Tone** library (in the *Sound* folder).

![4.1.1 - MB_Tone_Library](assets/4.1.1%20-%20MB_Tone_Library.png)

##### 📍 Buzzer Pin Mapping

| Buzzer | ESP32-C3 Pin | MicroBlocks |
| ------ | ------------ | ----------- |
| Signal | **IO10**     | pin `10`    |

🔧 Build the following script, we will reproduce the welcome melody found across many of TomatoCube's creations:

![4.1.2 - MB_Welcome_Melody](assets/4.1.2%20-%20MB_Welcome_Melody.png)

```text
when started
  attach buzzer to pin (10)
  play frequency (659) for (120) ms     -- NOTE_E5
  play frequency (587) for (120) ms     -- NOTE_D5
  play frequency (370) for (160) ms     -- NOTE_FS4
```

Or, using musical note names instead of frequencies:

![4.1.3 - MB_Welcome_Melody_Note](assets/4.1.3%20-%20MB_Welcome_Melody_Note.png)

```text
when started
  attach buzzer to pin (10)
  play note [E] octave (1) for (120) ms
  play note [D] octave (1) for (120) ms
  play note [F#] octave (0) for (160) ms
```

###### 🧪 Key Blocks

- `attach buzzer to pin (10)` - Tells the Tone library where the buzzer is. Do this **once**, at the start.
- `play frequency (Hz) for (ms) ms` - Plays an exact pitch.
- `play note [ ] octave ( ) for (ms) ms` - Plays a named note. Octave `0` is the octave containing **middle C** (C4, 261.63 Hz), `1` is one octave higher, `-1` is one lower.

> 💡 Note:
> Bear-Buddy uses a **passive** buzzer, so *we* decide the pitch. An active buzzer could only make one fixed beep.

###### 📖 How the Note Corresponds to the Frequency

The **frequency** of a note is the number of vibrations per second. Higher frequency = higher pitch. For example **A4** (440 Hz) is the standard tuning reference, and each **octave doubles** the frequency (so **A5** = 880 Hz). In MicroBlocks' `play note` block, scientific octave **4** is octave **0**, octave **5** is **1**, and so on.

| Note | 3      | 4 (MB 0) | 5 (MB 1) | 6 (MB 2) | 7 (MB 3) |
| ---- | ------ | -------- | -------- | -------- | -------- |
| C    | 130.81 | 261.63   | 523.25   | 1046.5   | 2093     |
| C#   | 138.59 | 277.18   | 554.37   | 1108.73  | 2217.46  |
| D    | 146.83 | 293.66   | 587.33   | 1174.66  | 2349.32  |
| D#   | 155.56 | 311.13   | 622.25   | 1244.51  | 2489     |
| E    | 164.81 | 329.63   | 659.25   | 1318.51  | 2637     |
| F    | 174.61 | 349.23   | 698.46   | 1396.91  | 2793.83  |
| F#   | 185    | 369.99   | 739.99   | 1479.98  | 2959.96  |
| G    | 196    | 392      | 783.99   | 1567.98  | 3135.96  |
| G#   | 207.65 | 415.3    | 830.61   | 1661.22  | 3322.44  |
| A    | 220    | 440      | 880      | 1760     | 3520     |
| A#   | 233.08 | 466.16   | 932.33   | 1864.66  | 3729.31  |
| B    | 246.94 | 493.88   | 987.77   | 1975.53  | 3951     |

#### 4.2: Button-Triggered Sound Effects

Let's combine Chapters 3 and 4: **Button A** plays a rising chirp, **Button B** plays a falling one.

![4.2.1 - MB_Up_Down_Melody](assets/4.2.1%20-%20MB_Up_Down_Melody.png)

```text
when started
  attach buzzer to pin (10)

when <button A> pressed
  play note [C] octave (1) for (90) ms
  play note [E] octave (1) for (90) ms
  play note [G] octave (1) for (90) ms

when <button B> pressed
  play note [G] octave (1) for (90) ms
  play note [E] octave (1) for (90) ms
  play note [C] octave (1) for (90) ms
```

Compare this with the CircuitPython version: no edge detection, no `last_A` / `last_B` variables. The hat blocks do all of that for us.



#### 4.3: Using an Existing RTTTL Melody

Writing out every note by hand (like we did in §4.1) is fine for a three-note jingle, but what about a whole tune? Back in the early mobile-phone era, people shared ringtones as short lines of text called **RTTTL** (Ring Tone Text Transfer Language). There are *thousands* of these little melody strings floating around the internet, and the best part is they are just text, so we can paste one straight into a block and play it.

##### 📦 Add the Ringtone Library

Using **§2.4**, add the **Ringtone** library (in the *Sound* folder). It uses the Tone library, which is added automatically if it isn't already.

![4.3.0 - MB_RingTone_Library](assets/4.3.0%20-%20MB_RingTone_Library.png)

🔧 Build the following script:

![4.3.1 - MB_Ringtone](assets/4.3.1%20-%20MB_Ringtone.png)

```text
when started
  attach buzzer to pin (10)
  play ringtone [Twinkle:d=4,o=5,b=100:c,c,g,g,a,a,2g,f,f,e,e,d,d,2c]
```

Click the script. Bear-Buddy will play "Twinkle, Twinkle, Little Star" through its buzzer, note for note, no hand-written frequencies required. Try pasting in one of these instead:

```text
OdeToJoy:d=4,o=5,b=120:e,e,f,g,g,f,e,d,c,c,d,e,8e.,8d,2d
Jingle:d=8,o=5,b=120:e,e,4e,e,e,4e,e,g,c,d,2e
```

##### 🧪 Key Blocks

- `play ringtone [ ]` - Parses the RTTTL text and plays it on the attached buzzer.
- It **waits** until the tune has finished before the next block in *that* script runs. But other scripts keep running - see the challenge below!

> 💡 Note:
> See the **Appendix (§10.1)** for how an RTTTL string is put together.

##### 🎹 Challenge: A Mini Jukebox (with a light show!)

Combine this with the buttons from Chapter 3: play a different tune depending on which button is pressed. And because MicroBlocks runs every script at the same time, we can blink the LED **while the music plays** - something that needed a special non-blocking player in CircuitPython.

![4.3.2 - MB_Jukebox](assets/4.3.2%20-%20MB_Jukebox.png)

```text
when started
  attach buzzer to pin (10)
  forever
    set digital pin (3) to <true>
    wait (150) millisecs
    set digital pin (3) to <false>
    wait (150) millisecs

when <button A> pressed
  play ringtone [Tetris:d=4,o=5,b=200:e6,8b,8c6,8d6,16e6,16d6,8c6,8b,a,8a,8c6,e6,8d6,8c6,b,8b,8c6,d6,e6,c6,a,2a]

when <button B> pressed
  play ringtone [MissionImp:d=16,o=5,b=100:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p]
```

> 💡 Note:
> What happens if you press Button B while Button A's tune is still playing? Both scripts try to use the buzzer at once. Try it, then think about how you could stop that (hint: a variable like `playing` that each script checks first).

### Chapter 5:

#### 5.1: NeoPixel LEDs - The 5×5 Matrix

**Nothing catches the eye like glowing LEDs!** NeoPixels are colorful, programmable RGB LEDs that display **millions of colors** by mixing red, green, and blue. Bear-Buddy carries a **5×5 serpentine NeoPixel matrix** (25 pixels) on `IO7`, perfect for faces, icons, and scrolling text.

![5.1.2 - NeoPixel_matrix](assets/5.1.2%20-%20NeoPixel_matrix.png)



##### 🌈 How NeoPixels Work

Each NeoPixel (WS2812-type LED) is an **intelligent RGB LED** that daisy-chains. Each LED reads the first color off the incoming data stream, keeps it, and passes the rest down the chain to the next pixel. In MicroBlocks the **NeoPixel** library handles all the tricky timing for us.

![5.1.1 - NeoPixel_die](assets/5.1.1%20-%20NeoPixel_die.png)

> 💡 Note:
> You can read more about the protocol in the [WS2812B datasheet](https://github.com/TomatoCube18/Lattice_FPGA_MacroKeys/blob/main/Relevant_Docs_DataSheets/WorldSemi-WS2812B-Mini.pdf).

##### 🎁 Two Ways to Use the Matrix

The TomatoCube MicroBlocks build gives you **two** ways to drive the matrix, and this chapter uses both:

| Library | Best for | Thinks in |
|---|---|---|
| **NeoPixel_Serpentine** (Cloud *Github* link) | Full color, every pixel its own color, rainbows, animations | Pixel numbers 1 to 25 |
| **LED Display** (*Displays* folder) | Pictures, faces, scrolling text, plotting x/y points | A 5×5 grid, like the micro:bit |

> 💡 Note:
> Use **one or the other in a program**, not both at the same time, since they both drive pin 7.

##### 📍 NeoPixel Pin Mapping

| NeoPixel Matrix | ESP32-C3 Pin | MicroBlocks |
| --------------- | ------------ | ----------- |
| DIN             | **IO7**      | pin `7`     |

#### 5.2: Light Them All Up (a Fancy Blink)

##### 📦 Add the NeoPixel Library from the cloud

Using **§2.4**, add the **NeoPixel Serpentine** library from the cloud. (Remember to Choose **Cloud** and install the library from the following Github link): [NeoPixel Serpentine - https://raw.githubusercontent.com/TomatoCube18/test/main/NeoPixelTomatoCube.ubl](https://raw.githubusercontent.com/TomatoCube18/test/main/NeoPixelTomatoCube.ubl)

![5.2.1 - MB_NeoPixel_Library](assets/5.2.1%20-%20MB_NeoPixel_Library.png)

🔧 Build the following script:

![5.2.2 - MB_NeoPixel_BlueBlink](assets/5.2.2%20-%20MB_NeoPixel_BlueBlink.png)

```text
when started
  attach (25) LED NeoPixel strip to pin (7)
  forever
    set all NeoPixels color (color r (0) g (0) b (80))     -- Blue
    wait (500) millisecs
    clear NeoPixels
    wait (500) millisecs
```

##### 🧪 Key Blocks

- `attach (25) LED NeoPixel strip to pin (7)` - Initializes the chain (25 pixels here). Do this once, at the start.
- `color r ( ) g ( ) b ( )` - Mixes a color from red, green and blue, each **0 to 255**.
- `set all NeoPixels color ( )` - Sets every LED at once. (You can also click the color swatch in the block to pick a color visually.)
- `clear NeoPixels` - Turns them all off.

> ⚠️ Note:
> Keep colors **dim** while learning, values around 30 to 80 are plenty bright. Running all 25 pixels at full white (255, 255, 255) can pull more current than USB comfortably supplies.

#### 5.3: Addressing Individual Pixels - The Serpentine Layout

To light one pixel you use `set NeoPixel (n) color ( )`, where **`n` runs `1 → 25`** (MicroBlocks counts from **1**, not 0 like Python).

But our matrix is wired in a **serpentine** pattern, and on this panel the chain **starts at the top-right**: the first row runs **right-to-left**, the next row runs **left-to-right**, and so on, zig-zagging like a snake. So pixel *number* order is **not** a tidy grid. To think in (x, y) coordinates we make our own block!

![5.4.1 - Serpentine_Mapping](assets/5.4.1%20-%20Serpentine_Mapping.svg)

##### 🛠️ Making Your Own Block (Advanced!)

1. Go to **My Blocks** and click **Add a reporter block**.
2. Name it `pixel x y`. Click the **+** at the end of the name to add two inputs, `x` and `y`.
3. Build its definition (x and y both go from **0 to 4**, with (0, 0) at the top-left):

![5.3.1 - MB_PixelXY](assets/5.3.1%20-%20MB_PixelXY.png)

```text
define (pixel (x) (y))
  if <((y) mod (2)) = (0)>
    return (((y) × (5)) + ((4) − (x)) + (1))     -- even rows: right -> left
  else
    return (((y) × (5)) + (x) + (1))             -- odd rows:  left  -> right
```

(The `+ 1` at the end turns the 0-based maths into MicroBlocks' 1-based pixel numbers.)

Now walk a single green dot across the whole grid, row by row:

```text
when started
  attach (25) LED NeoPixel strip to pin (7)
  forever
    for (y) in (range (0) to (4))
      for (x) in (range (0) to (4))
        clear NeoPixels
        set NeoPixel (pixel (x) (y)) color (color r (0) g (80) b (0))
        wait (80) millisecs
```

> 💡 Note:
> Serpentine wiring can start from a different corner depending on orientation. If your dot jumps around, flip the logic (swap which rows reverse, or mirror `x`). Getting this right once is a great logic exercise for students!

#### 5.4: Displaying Pictures with the LED Display Library

Drawing pictures pixel by pixel is a lot of work. The **LED Display** library (the same one used for the BBC micro:bit's 5×5 display) does the serpentine mapping for us, and gives us a **clickable 5×5 grid** to draw pictures on.

##### 📦 Add the LED Display Library

Using **§2.4**, add the **LED Display** library (in the *Displays* folder).

![5.4.1 - MB_LED_Display_Library](assets/5.4.1%20-%20MB_LED_Display_Library.png)

🔧 Drag out the `display` block and **click squares in its 5×5 grid** to draw a picture. Here is a beating heart:

![5.4.2 - MB_Heart](assets/5.4.2%20-%20MB_Heart.png)

```text
when started
  display [happy]         -- draw a happy smile in the grid
  wait (1000) millisecs
  forever
    display [heart]   -- draw a regular heart in the grid
    wait (400) millisecs
    display [small heart] -- draw a small heart in the grid
    wait (400) millisecs
```

Patterns used in the screenshot (`#` = lit):

```text
 SMILE       BIG HEART    SMALL HEART
 . . . . .   . # . # .    . . . . .
 . # . # .   # # # # #    . # . # .
 . . . . .   # # # # #    . # # # .
 # . . . #   . # # # .    . . # . .
 . # # # .   . . # . .    . . . . .
```

##### 🧪 Key Blocks

- `display [5×5 grid]` - Shows the picture you drew in the block.
- `clear display` - Turns every pixel off.
- `plot x ( ) y ( )` / `unplot x ( ) y ( )` - Turn a single pixel on/off by its grid position (**1 to 5**, with (1, 1) at the top-left).
- `point x ( ) y ( )` - Reports whether that pixel is currently lit.

> 💡 Note:
> Try rewriting the §5.3 "walking dot" with `plot` and `unplot`. No custom block needed this time - the library already knows about the serpentine wiring.



#### 5.5: ✨ Scrolling a Message

The LED Display library can also **scroll text** across the matrix, letter by letter, using a built-in 5×5 font:

![5.5.1 - MB_ScrollText](assets/5.5.1%20-%20MB_ScrollText.png)

```text
when started
  forever
    scroll text [Hello,BearBuddy!]
		wait (100) millisecs
```

That's it - one block! 🎉

##### 🧪 Key Blocks

- `scroll text [ ]` - Scrolls the text across the display, waits until it has finished.
- `scroll text [ ] pausing (ms)` - (click the arrow on the block) Changes the scroll speed.
- `display character [ ]` - Shows a single letter or digit, without scrolling.

> 💡 Note:
> Try `scroll text` with a **number** or a **variable** dropped into the slot, you will quickly realize the cost & limitation of running a MicroBlocks VM on a ESP32-C3 processor, an occasional flashing of the NeoPixel Pixel which will not be seen when we develop the same example in circuitPython or C/C++. But, as with many open-source software, future relase of the firmware might bring with it optimization, so hopefully this will go away in future releases.

### Chapter 6:

#### 6.1: Infrared Remote Control (NEC)

Your kit includes an **infrared (IR) remote fob** that speaks the **NEC protocol**, the same scheme used by most TV remotes. Bear-Buddy has an IR receiver on `IO21`. In this chapter we read the remote's button codes and use them to control Bear-Buddy wirelessly.

![6.1.1 - IR_Receiver_Remote](assets/6.1.1%20-%20IR_Receiver_Remote.png)

##### 🔦 How IR / NEC Works

The remote blinks an invisible infrared LED on and off in a precise timed pattern. The receiver turns those blinks back into a stream of pulse lengths. A NEC message carries an **address** and a **command** byte (each sent twice, once inverted, for error checking). The **IR Remote** library decodes those pulses into a number for us.

##### 📦 Add the IR Library

Using **§2.4**, add the **IR Remote** library (in the *Others* folder).

![6.1.1 - MB_IR_Library](assets/6.1.1%20-%20MB_IR_Library.png)

##### 📍 IR Pin Mapping

| IR Receiver | ESP32-C3 Pin | MicroBlocks |
| ----------- | ------------ | ----------- |
| Signal OUT  | **IO21**     | pin `21`    |

#### 6.2: Reading Your Remote's Codes

Run this **first** to discover what each button on *your* fob sends, you'll need those numbers for the next step.

![6.2.1 - MB_IR_Read](assets/6.2.1%20-%20MB_IR_Read.png)

```text
when started
  attach IR receiver to pin (21)
  forever
    say (receive IR code)
```

Point the remote at Bear-Buddy and press buttons. Write down the number shown in the speech bubble for each button you care about.

##### 🧪 Key Blocks

- `attach IR receiver to pin (21)` - Tells the library where the receiver is. Do this once, at the start.
- `receive IR code` - **Waits** for a button press, then reports its **command** number (the unique button byte).
- `IR code received?` - Reports `true` if a new code has arrived, without waiting. Handy inside a `forever` loop that is also doing other things.

> 💡 Note:
> MicroBlocks shows the codes as **decimal** numbers. The CircuitPython camp shows the same codes in **hex**, so `0x45` there is `69` here, `0x16` is `22`, and `0x19` is `25`.

#### 6.3: Mapping Buttons to Actions

Now plug in *your* codes (from §6.2) to control the LED and the NeoPixel matrix.

![6.3.1 - MB_IR_Actions](assets/6.3.1%20-%20MB_IR_Actions.png)

```text
when started
  attach IR receiver to pin (21)
  attach (25) LED NeoPixel strip to pin (7)
  clear NeoPixels
  set (led on) to <false>
  et digital pin (3) to (led on)
  forever
    set (code) to (receive IR code)
    if <(code) = (64)>                     -- POWER (replace with your code!)
      set (led on) to <not (led on)>
      set digital pin (3) to (led on)
      say [Power -> toggle LED]
    else if <(code) = (25)>                -- button 1
      set all NeoPixels color (color r (80) g (0) b (0))     -- red
    else if <(code) = (24)>                -- button 2
      clear NeoPixels
```

> 💡 Note:
> To get the `else if` branches, click the small arrow at the bottom of the `if` block.

### Chapter 7 (Advanced) :

#### 7.1: I²C Bus & the 1602 Character LCD

##### 7.1.1: 🐙 I²C Expansion Bus

**I²C** (Inter-Integrated Circuit) is a two-wire serial communication protocol invented by **Philips Semiconductor** (now NXP) in the early 1980s. It is widely used to connect low-speed peripherals like sensors, displays, and clocks to microcontrollers. Its superpower is that **many devices share the same two wires**, each one answering to a unique **address**.

Bear-Buddy brings the I²C bus out through the I²C Grove socket on:

- **SDA (Serial Data Line)** → `IO5`
- **SCL (Serial Clock Line)** → `IO6`

The TomatoCube MicroBlocks build already knows these pins, so **you never need to set them** - every I²C block just works.

We will hang **two** devices on this one bus: a **1602 character LCD** and a **DS1307 real-time clock**.

![7.1.1 - i2C-location](assets/7.1.1%20-%20i2C-location.png)



##### 7.1.2: The 1602 Character LCD

An I²C 1602 character LCD shows **16 characters across, 2 rows**, perfect for menus, sensor values, and messages. The kit's LCD uses I²C connectivity so it needs only one Grove or Qwiic cable, which delivers both I²C signals and power in one shot.

![7.1.1 - LCD_1602](assets/7.1.1%20-%20LCD_1602.png)

You can connect the I²C Grove cable to the LCD as such.

![7.1.1 - i2c_LCD_1602_RTC](assets/7.1.1%20-%20i2c_LCD_1602_RTC.png)

##### 📍 I²C Addresses

In MicroBlocks, I²C addresses are typed as **decimal** numbers:

| Device              | Address (hex) | Address (decimal, for MicroBlocks) |
| ------------------- | ------------- | ---------------------------------- |
| 1602 LCD (backpack) | `0x27`        | `39`                               |
| DS1307 RTC          | `0x68`        | `104`                              |

#### 7.2: Finding Devices & "Hello World" on the LCD

##### 🔍 Is the Device There?

The **Comm** category has the raw I²C blocks. `i2c get device ( ) register ( )` reads one byte from a device. If nothing answers at that address, it reports a **negative** number:

![7.2.1 - MB_ScanI2C](assets/7.2.1%20-%20MB_ScanI2C.png)

```text
when started
  say (i2c get device (39) register (0))
```

Click it: a value of `0` or more means the LCD answered at `39` (0x27). A negative number means "nobody home", so try `63` (0x3F) instead, if a value of `0` is returned then... 😱.

##### 📦 Add the LCD Library

Using **§2.4**, open the *Graphics & Displays* folder and add the **LCD Display** library.

![7.2.2 - MB_LCD_Library](assets/7.2.2%20-%20MB_LCD_Library.png)

🔧 Build the following script:

![7.2.3 - MB_LCD_Hello](assets/7.2.3%20-%20MB_LCD_Hello.png)

```text
when started
  clear LCD
  write [Hello Bear-Buddy] on LCD Line (1)
  write [MicroBlocks!] on LCD Line (2)
```



##### 🧪 Key Blocks

- `i2c get device ( ) register ( )` - Read one byte from an I²C device (also a quick "is it there?" test).
-  write [ ] on LCD Line ( )` - Prints text at a specific row (1 or 2).
- `clear LCD` - Wipes the screen.

#### 7.3: What Students Can Try Next

- **Change the message:** clear the screen and write new text.
- **Show a live counter** that ticks up every second (use a variable and `join` it with some text).
- **Mix in a button:** display which button was last pressed.

### Chapter 8 (Advanced) :

#### 8.1: Keeping Time - The DS1307 Real-Time Clock

Many projects need **accurate timekeeping**, for clocks, logging, alarms, and timed automation. The ESP32-C3 does not keep good time on its own, and it forgets the time entirely when power is removed.

The **DS1307** RTC module which fits snugly behind the 1602 Character LCD solves this. It keeps ticking on a small **backup battery (CR2032)** even when Bear-Buddy is switched off, and it communicates over the **same shared I²C bus** we just used for the LCD.

![8.1.1 - DS1307_Module](assets/8.1.1%20-%20DS1307_Module.png)

> 💡 Note:
> The DS1307 is simple and reliable but **not temperature-compensated**, so it drifts a little more than a DS3231. For a learning clock that is perfectly fine, just expect a few seconds of drift over time.

##### 🧠 Talking to the DS1307

Luckily for us. the existing Real Time Clock library that comes with microblocks supports the DS1307, we will use the library to communicate with the DS1307 over the **I²C** communication bus, shared with the LCD display.

The clock keeps the time in **registers** (numbered memory slots) at address `104` (0x68):

| Register | Holds | Notes |
| -------- | ----- | ----- |
| `0` | Seconds | Top bit is the "clock halt" flag - keep it 0 |
| `1` | Minutes | |
| `2` | Hours | 24-hour mode |
| `3` | Day of week | 1 to 7 |
| `4` | Date | 1 to 31 |
| `5` | Month | 1 to 12 |
| `6` | Year | 0 to 99 (i.e. 2000 to 2099) |



##### 📦 Add the Real Time Clock Library

Using **§2.4**, add the **Real Time Clock** library (in the *Others* folder).

![8.1.1 - MB_RTC_Library](assets/8.1.1%20-%20MB_RTC_Library.png)


##### 🔢 BCD - Binary Coded Decimal

The DS1307 stores numbers in **BCD**: each decimal digit gets its own 4 bits. So the number **45** is stored as `0100 0101` - a `4` in the top half and a `5` in the bottom half. We need two small custom blocks to convert back and forth (make them in **My Blocks**, see §5.3). The `>>`, `<<` and `&` blocks are in **Operators** (click the arrow on the `mod`/math blocks to find the bitwise ones):

#### 8.2: Setting & Reading the Time

##### ⏰ Set the clock (run once!)

![8.2.1 - MB_RTC_SetTime](assets/8.2.1%20-%20MB_RTC_SetTime.png)

Change the numbers to the current date and time, then **click this script once**:

```text
when started
  Init Clock (DS1307)
when <button B> pressed
  set year (2026) month (11) day (2)			-- year (20)26, month, date
  set day of week (1)    									-- day of week
  set hours (5) minutes (0) seconds (0)   -- hours (24h)
  say [Clock Set!]
```

We put it under `when <button B> pressed` so it doesn't run by accident when Bear-Buddy powers up. Press Button B once to set the time.

> 💡 Note:
> Writing the seconds register **last** also clears the "clock halt" flag, which starts a brand-new DS1307 ticking.

##### 🕐 Read the clock

![8.2.2 - MB_RTC_ReadTime](assets/8.2.2%20-%20MB_RTC_ReadTime.png)

🔧 Build the following script:

```text
when started
	Init Clock (DS1307)
  forever
    say (clock [time (H:M:S)])
    wait (1000) millisecs
```



#### 8.3: A Real Clock - Time on the LCD

Finally, let's put the whole chapter together: read the RTC and show a live clock on the 1602 LCD. 
It will display "Bear-Clock: 2026" on LCD `row 1` and "(02/11) 05:17" on LCD `row 2`.

![8.3.1 - MB_LCD_Clock](assets/8.3.1%20-%20MB_LCD_Clock.png)

🔧 Build the following script:

```text
when started
	Init Clock (DS1307)
  write [join [Bear-Clock: ] (clock [year]) ] on LCD Line (1)
  forever
    write [join [(] (clock [day]) [/] (clock [month]) [)] [ ] (clock [time (H:M:S)]) ] on LCD Line (2)
    wait (500) millisecs
```



##### 🧪 Key Concepts

- **RTC stands alone:** thanks to its battery, the DS1307 keeps time even when Bear-Buddy is off.
- **Shares the I²C bus with the LCD:** multiple devices, one bus, unique addresses.
- **Setting time (once!):** you only set it the first time (or after a battery change).
- `join [ ] [ ]` - Glue text and numbers together.



### Chapter 9:

#### 9.1: 🏆 Putting It All Together - Challenge Ideas

You now have every Bear-Buddy skill. Combine them into a mini-project:

- **Remote Mood Lamp:** use the IR remote to pick NeoPixel matrix colors and animations.
- **Alarm Buddy:** read the time from the DS1307, and when it hits a set minute, scroll "WAKE UP" across the matrix and play a ringtone.
- **Reaction Game:** light a random matrix pixel (try the `random ( ) to ( )` block in **Operators**), the player presses Button A or B as fast as they can, show the reaction time on the LCD (the `timer` and `reset timer` blocks in **Input** will help).
- **IR Clock Setter:** set the DS1307 time using the number buttons on your remote, no block edits needed.
- **Matrix Clock:** no LCD? Scroll the time across the 5×5 matrix instead.

Mix the chapters, break things, and try again, that is exactly how makers learn.

#### 9.2: 🚀 What's Next? Graduating to CircuitPython

Once you're comfortable with MicroBlocks, you're ready to **type** your programs. The **Bear-Buddy CircuitPython Mini-Camp** walks through *every project in this guide* again, in Python. Because you already know what each project should do, you can focus on learning the code.

To switch, reflash Bear-Buddy with **CircuitPython** using the web loader (§2.2), and pick **CircuitPython** instead of MicroBlocks. You can always come back to MicroBlocks the same way.

Happy building! 🐻



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



#### 10.2: 🧠 Talking to the DS1307 Directly (Raw - Bare Metal)

This time we won't use a library. The DS1307 is simple enough that we can talk to it with the raw **I²C blocks**, and learn how real hardware stores data along the way.

The clock keeps the time in **registers** (numbered memory slots) at address `104` (0x68):

| Register | Holds       | Notes                                        |
| -------- | ----------- | -------------------------------------------- |
| `0`      | Seconds     | Top bit is the "clock halt" flag - keep it 0 |
| `1`      | Minutes     |                                              |
| `2`      | Hours       | 24-hour mode                                 |
| `3`      | Day of week | 1 to 7                                       |
| `4`      | Date        | 1 to 31                                      |
| `5`      | Month       | 1 to 12                                      |
| `6`      | Year        | 0 to 99 (i.e. 2000 to 2099)                  |

##### 🔢 BCD - Binary Coded Decimal

The DS1307 stores numbers in **BCD**: each decimal digit gets its own 4 bits. So the number **45** is stored as `0100 0101` - a `4` in the top half and a `5` in the bottom half. We need two small custom blocks to convert back and forth (make them in **My Blocks**, see §5.3). The `>>`, `<<` and `&` blocks are in **Operators** (click the arrow on the `mod`/math blocks to find the bitwise ones):

![10.2.1 - MB_RTC_RawBCD](assets/10.2.1%20-%20MB_RTC_RawBCD.png)

```text
define (from BCD (n))
  return ((((n) >> (4)) × (10)) + ((n) & (15)))

define (to BCD (n))
  return ((((n) / (10)) << (4)) + ((n) mod (10)))
```

##### ⏰ Set the clock (run once!)

Change the numbers to the current date and time, then **click this script once**:

![10.2.2 - MB_RTC_RawSetTime](assets/10.2.2%20-%20MB_RTC_RawSetTime.png)

```text
when <button B> pressed
  i2c set device (104) register (6) to (to BCD (26))    -- year (20)26
  i2c set device (104) register (5) to (to BCD (11))    -- month
  i2c set device (104) register (4) to (to BCD (2))     -- date
  i2c set device (104) register (3) to (to BCD (2))     -- day of week
  i2c set device (104) register (2) to (to BCD (15))    -- hours (24h)
  i2c set device (104) register (1) to (to BCD (30))    -- minutes
  i2c set device (104) register (0) to (to BCD (0))     -- seconds (also starts the clock)
  say [Clock set!]
```

We put it under `when <button B> pressed` so it doesn't run by accident when Bear-Buddy powers up. Press Button B once to set the time.

> 💡 Note:
> Writing the seconds register **last** also clears the "clock halt" flag, which starts a brand-new DS1307 ticking.

##### 🕐 Read the clock

![10.2.3 - MB_RTC_RawReadTime](assets/10.2.3%20-%20MB_RTC_RawReadTime.png)

```text
when started
  forever
    set (h) to (from BCD ((i2c get device (104) register (2)) & (63)))
    set (m) to (from BCD (i2c get device (104) register (1)))
    set (s) to (from BCD ((i2c get device (104) register (0)) & (127)))
    say (join (h) [:] (m) [:] (s))
    wait (1000) millisecs
```

##### 🧪 Key Blocks

- `i2c set device ( ) register ( ) to ( )` - Write one byte to a device register.
- `i2c get device ( ) register ( )` - Read one byte from a device register.
- `( ) & ( )` - Bitwise AND, keeps only the bits we want (`& 127` drops the clock-halt bit, `& 63` drops the 12/24-hour bits).
- `( ) >> ( )` / `( ) << ( )` - Shift bits right/left (`>> 4` moves the top digit down).
- `join [ ] [ ]` - Glue text and numbers together.



#### 10.3: 🧩 Block Quick Reference

| I want to... | Block | Category |
|---|---|---|
| Run blocks at power-up | `when started` | Control |
| Repeat forever | `forever` | Control |
| Pause | `wait ( ) millisecs` | Control |
| Turn a pin on/off | `set digital pin ( ) to < >` | Pins |
| Dim an LED (PWM) | `set pin ( ) to (0-1023)` | Pins |
| Read a pin | `read digital pin ( )` | Pins |
| React to a button | `when <button A> pressed` | Input / Control |
| Show a value in the IDE | `say [ ]` / `graph ( )` | Output |
| Play a tone | `play note [ ] octave ( ) for ( ) ms` | Tone library |
| Play a tune | `play ringtone [ ]` | Ringtone library |
| Light NeoPixels | `set all NeoPixels color ( )` | NeoPixel library |
| Draw on the matrix | `display [grid]` / `plot x y` | LED Display library |
| Scroll text | `scroll text [ ]` | LED Display library |
| Read the IR remote | `receive IR code` | IR Remote library |
| Talk I²C | `i2c get device / i2c set device` | Comm |
