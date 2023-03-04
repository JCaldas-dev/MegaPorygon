import websocket
import ssl
import json
import time

# Change these variables to your own login information
USERNAME = "MegaPorygonBot"
PASSWORD = "password"

# URL to log in to the Pokemon Showdown server
LOGIN_URL = "https://play.pokemonshowdown.com/action.php"

# Payload for logging in
login_payload = {
    "act": "login",
    "name": USERNAME,
    "pass": PASSWORD,
    "challstr": "",
}

# Event called when the WebSocket connection is opened
def on_open(ws):
    print("WebSocket connected.")
    # Send the login payload
    ws.send(json.dumps(login_payload))

# Event called when a message is received through the WebSocket connection
def on_message(ws, message):
    print(message)

# Event called when an error occurs in the WebSocket connection
def on_error(ws, error):
    print(error)

# Event called when the WebSocket connection is closed
def on_close(ws):
    print("WebSocket disconnected.")

# Connect to the Pokemon Showdown WebSocket server
ws_url = "wss://sim.smogon.com/showdown/websocket"
ws = websocket.WebSocketApp(
    ws_url,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    on_open=on_open,
)

# Start the WebSocket connection
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
