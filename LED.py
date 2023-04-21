#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)

def turn_on():
    GPIO.output(18,GPIO.HIGH)

def turn_off():
    GPIO.output(18,GPIO.LOW)

def get_lamp_state():
    state = GPIO.input(18)
    if state == GPIO.HIGH:
        return "ON"
    else:
        return "OFF"

def get_web_page():
    web_page = """
    <html>
    <title>Robocaz!</title>
    <body>
    Lamp state: {}<br>
    <a href="/on">ON</a><br>
    <a href="/off">OFF</a>
    </body>
    </html>
    """.format(get_lamp_state())

    return web_page


setup()

app = FastAPI()

@app.get("/")
async def root():
    web_page = get_web_page()
    return HTMLResponse(content=web_page)

@app.get("/on")
async def web_on():
    turn_on()
    web_page = get_web_page()
    return HTMLResponse(content=web_page)

@app.get("/off")
async def web_off():
    turn_off()
    web_page = get_web_page()
    return HTMLResponse(content=web_page)
