import modules.api as api_key
import pprint
from pubg_python import PUBG, Shard
import json
import requests

api = PUBG(api_key.api_key(), Shard.PC_AS)

match = api.matches().get('2fe06742-cf8a-41b6-8c82-db66af70bfd8')
asset = match.assets[0]
# telemetry = api.telemetry(asset.url)
# json_file = open('test.json', 'w')
# json.dump(telemetry, telemetry.events, indent=2)
# pprint.pprint(telemetry.events)

try:
    r = requests.get(asset.url)
    with open('test.json', mode='w') as f:
        json.dump(r.json(),f, indent=3)
except requests.exceptions.RequestException as err:
    print(err)