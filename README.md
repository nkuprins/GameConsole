# Game Console

## 2 in 1

### Remote like Wii

![](video_remote.mp4)

### Handles like a tablet

![](video_handles.mp4)

## Structure
- **Transmitter** - our game controller with gyroscope. It reads *z,y* axes and sends the data to the server using TCP.
- **Receiver** - the core of our game console written in *CircuitPython*: games, display, server.

## Font

Default font comes from [matrix-fonts](https://github.com/trip5/Matrix-Fonts)

## Setup instructions

### Install libraries

Use the [asyncio](https://docs.circuitpython.org/projects/asyncio/en/latest/index.html) library
```bash
circup install asyncio
```

### Network issues

If you get **wifi connection error** or **socket error**, then a possible fix can be to unplug the board and wait for 10 seconds, then reconnect again.
