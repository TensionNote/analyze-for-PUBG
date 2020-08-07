import csv
def extract_landing_point(telemetry):
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
    return landing_point_list

def extract_circle_position(telemetry):
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
    return game_state_list

def extract_aircraft_path(telemetry):
    aircraft_path_list=[]
    for event in telemetry.events_from_type("LogPlayerPosition"):
        try:
            if(event.vehicle.vehicle_type in "TransportAircraft"):
                aircraft_path_list.append(
                    [
                        event.character.location.x,
                        event.character.location.y,
                        event.character.location.z,
                        event.character.name,
                        event.character.team_id
                    ]
                )
        except TypeError:
            pass
    # CSV出力（テスト用）
    # with open('./output_files/aircraft_path_list.csv', 'w') as file:
    #     writer = csv.writer(file, lineterminator='\n')
    #     writer.writerows(aircraft_path_list)
    return aircraft_path_list

def extract_routing_path(telemetry):
    routing_path_list=[]
    for event in telemetry.events_from_type('LogPlayerPosition'):
        routing_path_list.append(
            [
                event.character.location.x,
                event.character.location.y,
                event.character.location.z,
                event.character.name,
                event.character.team_id,
                event.timestamp
            ]
        )
    # CSV出力（テスト用）
    # with open('./output_files/routing_path.csv', 'w') as file:
    #     writer = csv.writer(file, lineterminator='\n')
    #     writer.writerows(routing_path_list)
    return routing_path_list

def extract_roster(match):
    roster_list=[]
    for i in match.rosters:
        for j in i.participants:
            roster_list.append([i.attributes['stats']['teamId'], j.name])
    return roster_list