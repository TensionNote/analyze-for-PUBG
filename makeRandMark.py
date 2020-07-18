import secret.api as api_key
from chicken_dinner.pubgapi import PUBG
import json
import requests
import pprint
import csv
import modules.func4map as func4map

match_id="a42d3300-d3d5-46b5-b460-125cc013f75c"
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

# フィルタ(chiken dinner)
player_position_events=telemetry.filter_by("log_parachute_landing")
landing_point_list=[]
for event in player_position_events:
    landing_point_list.append(
        [
            event.character.location.x,
            event.character.location.y,
            event.character.location.z,
            event.character.name,
            event.character.team_id
        ]
    )
# with open('./output_files/landing_point.csv', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     writer.writerows(landing_point_list)

map_img = func4map.load_map(match.map_name)
map_img = func4map.draw_landing_point(map_img, landing_point_list)
map_img = func4map.resize_map(map_img)
print("hoge")