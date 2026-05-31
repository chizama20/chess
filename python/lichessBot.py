import berserk
import chess
from python.main import Engine

TOKEN = "lip_RRPuCrjOtIitAmazBv7M"

session = berserk.TokenSession(TOKEN)
client = berserk.Client(session)

for event in client.bots.stream_incoming_events():
    print(event)