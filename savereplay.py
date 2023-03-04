import websocket
import ssl

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("{'event':'challstr'}")
        ws.send("{'event':'chat','data':'/join global'}")
        ws.send("{'event':'chat','data':'/nick PokemonBot'}")
        ws.send("{'event':'chat','data':'!code jibxjhdw'}")
        ws.send("{'event':'chat','data':'/join battle-gen8randombattle-1234567890'}")
        ws.send("{'event':'chat','data':'!pick random'}")
        ws.send("{'event':'chat','data':'Hi, I am a bot!'}")
        ws.send("{'event':'chat','data':'Good luck and have fun!'}")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws_url = "wss://sim.smogon.com/showdown/websocket"
    ws = websocket.WebSocketApp(
        ws_url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open,
        header={'User-Agent': 'Mozilla/5.0'}
    )
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
