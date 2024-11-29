# Game Console

## Setup instructions

### Install libraries

Use the [asyncio](https://docs.circuitpython.org/projects/asyncio/en/latest/index.html) library
```bash
circup install asyncio
```

### Network issues and solution

If you get **wifi connection error** or **socket error**, then a possible fix can be to unplug the board and wait for 10 seconds, then reconnect again.

## Structure
- **Transmitter** - our game controller with gyroscope. It reads *z,y* axes and sends the data to the server using TCP.
- **Receiver** - the core of our game console: games, display, server.