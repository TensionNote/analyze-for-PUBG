import secret.api as api_key
from chicken_dinner.pubgapi import PUBG
import json
import requests
import pprint
import modules.CharacterPosition as CP
import csv

match_id="2fe06742-cf8a-41b6-8c82-db66af70bfd8"
shard="steam"

pubg = PUBG(api_key.api_key(), shard)
match = pubg.match(match_id)
telemetry = pubg.telemetry(match.telemetry_url)

# # match,をjsonに保存
# r=json.dumps(match.data,indent=3)
# with open('./json/'+match_id+'_match.json', mode='w') as f:
#     f.write(r)

# # telemetryをjsonに保存(urlから取得)
# try:
#     r = requests.get(match.telemetry_url)
#     with open('./json/'+match_id+'_telemetry.json', mode='w') as f:
#         json.dump(r.json(),f, indent=3)
# except requests.exceptions.RequestException as err:
#     print(err)

# key確認用
# pprint.pprint(telemetry.event_types())

# フィルタ(chiken dinner)
player_position_events=telemetry.filter_by("log_parachute_landing")
# pprint.pprint(player_position_events[0])
landing_point_list=[]
for event in player_position_events:
    landing_point_list.append([event.character.location.x, event.character.location.y, event.character.location.z, event.character.name])
with open('./output_files/landing_point.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(landing_point_list)
