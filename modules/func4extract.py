import csv
def extract_landing_point(telemetry):
    landing_point_list=[]
    for event in telemetry.events_from_type('LogParachuteLanding'):
        landing_point_list.append(
            {
                'x': event.character.location.x,
                'y': event.character.location.y,
                'z': event.character.location.z,
                'name': event.character.name,
                'team_id': event.character.team_id,
                'timestamp': event.timestamp
            }
        )
    # CSV出力（テスト用）
    # with open('./output_files/landing_point.csv', 'w') as file:
    #     writer = csv.writer(file, lineterminator='\n')
    #     writer.writerows(landing_point_list)
    return landing_point_list

def extract_circle_position(telemetry):
    # poisonGasWarningPosition ⇒発表される安全地帯、is_Gameが整数の時に切り替わる
    # safetyZonePosition ⇒刻一刻と変わる安全地帯is_Gameが少数の時に減少し続ける
    game_state_list=[]
    for event in telemetry.events_from_type("LogGameStatePeriodic"):
        game_state_list.append(
            {
                'safetyZonePosition_x': event.game_state.safety_zone_position.store['x'],
                'safetyZonePosition_y': event.game_state.safety_zone_position.store['y'],
                'safetyZonePosition_radius': event.game_state.safety_zone_radius,
                'poisonGasWarningPosition_x': event.game_state.poison_gas_warning_position.store['x'],
                'poisonGasWarningPosition_y': event.game_state.poison_gas_warning_position.store['x'],
                'poisonGasWarningPosition_radius': event.game_state.poison_gas_warning_radius,
                'isGame': event.common.is_game,
                'timestamp': event.timestamp
            }
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
                    {
                        'x': event.character.location.x,
                        'y': event.character.location.y,
                        'z': event.character.location.z,
                        'name': event.character.name,
                        'team_id': event.character.team_id,
                        'timestamp': event.timestamp
                    }
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
            {
                'x': event.character.location.x,
                'y': event.character.location.y,
                'z': event.character.location.z,
                'name': event.character.name,
                'team_id': event.character.team_id,
                'timestamp': event.timestamp
            }
        )
    # CSV出力（テスト用）
    # with open('./output_files/routing_path.csv', 'w') as file:
    #     writer = csv.writer(file, lineterminator='\n')
    #     writer.writerows(routing_path_list)
    return routing_path_list

def extract_roster(match):
    roster_list= [[] for i in range(len(match.rosters))]
    for i in match.rosters:
        for j in i.participants:
            roster_list[i.attributes['stats']['teamId']-1].append(
                {
                    'team_id': i.attributes['stats']['teamId'],
                    'name': j.name
                }
            )
    return roster_list