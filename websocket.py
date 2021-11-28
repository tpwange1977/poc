# pip install websocket-client
import websocket
from threading import Thread
import time
import sys


def on_message(ws, message):
    print("######################Message: ".format(message))


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            # send the message, then wait
            # so thread doesn't exit and socket
            # isn't closed
            ws.send("pong")
            time.sleep(10)

        time.sleep(1)
        ws.close()
        print("Thread terminating...")

    Thread(target=run).start()


if __name__ == "__main__":
    websocket.enableTrace(True)
    host = "wss://open.rocket.chat/websocket"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


#asyncio.run(hello("wss://open.rocket.chat"))
