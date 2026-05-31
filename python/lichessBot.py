import berserk
import chess
from python.main import Engine

TOKEN = "your_lichess_api_token_here"

session = berserk.TokenSession(TOKEN)
client = berserk.Client(session)

for event in client.bots.stream_incoming_events():
    print(event)