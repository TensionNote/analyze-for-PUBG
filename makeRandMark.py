import secret.api as api_key
# from chicken_dinner.pubgapi import PUBG
import pprint
import csv
import modules.func4map as func4map
import modules.func4savefiles as func4savefiles
from pubg_python import PUBG, Shard

match_id="a42d3300-d3d5-46b5-b460-125cc013f75c"

# chicken_dinner
# shard="steam"
# pubg = PUBG(api_key.api_key(), shard)
# match = pubg.match(match_id)
# telemetry = pubg.telemetry(match.telemetry_url)

# pubg python
api = PUBG(api_key.api_key(), Shard.PC_AS)
match = api.matches().get(match_id)
asset = match.assets[0]
telemetry = api.telemetry(asset.url)

#save files
# func4savefiles.save_files(match)

## パラシュート降下地点を特定
landing_point_list=[]
for event in telemetry.events_from_type('LogParachuteLanding'):
    landing_point_list.append(
        [
            event.character.location.x,
            event.character.location.y,
            event.character.location.z,
            event.character.name,
            event.character.team_id
        ]
    )

# CSV出力（テスト用）
# with open('./output_files/landing_point.csv', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     writer.writerows(landing_point_list)

#マップ出力
# map_img = func4map.load_map(match.map_name)
# map_img = func4map.draw_landing_point(map_img, landing_point_list)
# map_img = func4map.resize_map(map_img)
# map_img.save("./output_files/20200714_Miramar_resize.png")


## サークル特定
# poisonGasWarningPosition ⇒発表される安全地帯、is_Gameが整数の時に切り替わる
# safetyZonePosition ⇒刻一刻と変わる安全地帯is_Gameが少数の時に現象し続ける
game_state_list=[]
game_state_list.append(
    [
        "safetyZonePosition_x",
        "safetyZonePosition_y",
        "safetyZonePosition_radius",
        "poisonGasWarningPosition_x",
        "poisonGasWarningPosition_y",
        "poisonGasWarningPosition_radius",
        "isGame"
    ]
)
for event in telemetry.events_from_type("LogGameStatePeriodic"):
    game_state_list.append(
        [
            event.game_state.safety_zone_position.store['x'],
            event.game_state.safety_zone_position.store['y'],
            event.game_state.safety_zone_radius,
            event.game_state.poison_gas_warning_position.store['x'],
            event.game_state.poison_gas_warning_position.store['x'],
            event.game_state.poison_gas_warning_radius,
            event.common.is_game
        ]
    )
# CSV出力（テスト用）
# with open('./output_files/game_state_list.csv', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     writer.writerows(game_state_list)


# 航路特定
airplane_path_list=[]
for event in telemetry.events_from_type("LogPlayerPosition"):
    try:
        if(event.vehicle.vehicle_type in "TransportAircraft"):
            airplane_path_list.append(
                [
                    event.character.location.x,
                    event.character.location.y,
                    event.character.location.z,
                    event.character.name,
                    event.character.team_id
                ]
            )
    except TypeError as err:
        pass
# CSV出力（テスト用）
with open('./output_files/airplane_path_list.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(airplane_path_list)