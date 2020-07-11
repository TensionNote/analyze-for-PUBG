import modules.api as api_key
import modules.CharacterPosition as CP
import pprint
import json
from pubg_python import PUBG, Shard
api = PUBG(api_key.api_key(), Shard.PC_AS)
from pubg_python import Telemetry

def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

telemetry = Telemetry.from_json('a1082e64-c113-11ea-bab1-ea795b67a3d4-telemetry.json', shard='pc')
# json_file = open('test.json', 'w')
print(json.dumps(telemetry, default=default_method, indent=2))


player_position_events = telemetry.events_from_type('LogPlayerPosition')
pprint.pprint(player_position_events)
first_position_list=[]
for event in player_position_events:
    CP.CharacterPosition(event.x, event.y, event.z, event.name)