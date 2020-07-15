import secret.api as api_key
from chicken_dinner.pubgapi import PUBG
import json
import requests
import pprint
import modules.CharacterPosition as CP
import csv

from pubg_python import Telemetry as loding_local_telemetry

telemetry = loding_local_telemetry.from_json('./json/2fe06742-cf8a-41b6-8c82-db66af70bfd8_telemetry.json', shard='pc')

# フィルタ(pubg python)
player_position_events=telemetry.events_from_type('LogParachuteLanding')
landing_point_list=[]
for event in player_position_events:
    landing_point_list.append([event.character.location.x, event.character.location.y, event.character.location.z, event.character.name])
with open('./output_files/landing_point_local.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(landing_point_list)