# Startup file
from src.wifi import connectToWiFi, startServer
from src.led.pwmLed import pwmLedSetColor

# Disable LEDs
pwmLedSetColor(0, 0, 0)


def init():
    connectToWiFi()
    startServer()
