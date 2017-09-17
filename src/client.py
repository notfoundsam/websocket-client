import websocket
from threading import Thread
import time
import sys
import ir_devices
import json


def on_message(ws, message):
    request = json.loads(message)

    print request['device']

    if request['device'] == 'ligth_room_1':
        tmp = ir_devices.light_room_1()

        if tmp.run(request['command']) != True:
            send_error()

    if request['device'] == 'tv_1':
        tmp = ir_devices.tv_1()

        if tmp.run(request['command']) != True:
            send_error()

    else:
        print(message)
    

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print "aaaaa"
    # def run(*args):

def send_error():
    print("error")


if __name__ == "__main__":
    websocket.enableTrace(True)
    if len(sys.argv) < 2:
        host = "ws://localhost:9090/?key=py_secret_key"
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
