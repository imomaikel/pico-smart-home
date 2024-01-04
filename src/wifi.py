# Connect Pi Pico with the network
from src.config import WIFI_SSID, WIFI_PASSWD
from src.led.pwmLed import pwmLedSetColor
from src.html import htmlContent
from machine import Pin
import network
import socket
import json
import time

boardLed = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWD)


def connectToWiFi():
    maxAttempts = 10
    while maxAttempts > 0:
        if wlan.status() == 3:
            break
        maxAttempts -= 1
        boardLed.toggle()
        print('WiFi connecting...')
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('WiFi connection failed!')
    else:
        boardLed.value(1)
        addr = wlan.ifconfig()[0]
        print(f'WiFi connected! ({addr})')


def startServer():
    s = socket.socket()
    s.bind(('0.0.0.0', 80))
    s.listen(1)

    while True:
        c, addr = s.accept()
        request = c.recv(8192)

        try:
            args = str(request).split(' ')
            lastArg = args[len(args) - 1]
            _body = lastArg[lastArg.find('{'):lastArg.rfind('}')+1]
            body = json.loads(_body)

            command = body['command']

            if command == 'pwmLed':
                r, g, b = body['red'], body['green'], body['blue']
                pwmLedSetColor(int(r), int(g), int(b))

        except:
            pass

        c.send('HTTP/1.0 200 OK\n')
        c.send('Content-Type: text/html\n')
        c.send('\n')
        c.send(htmlContent)
        c.close()
