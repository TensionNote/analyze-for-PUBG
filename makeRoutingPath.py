import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard

# function
def makeRoutingPath(match_id,region):
    ## get data from Server
    # region is "AS" or "TOURNAMENT"
    [match,telemetry]=func4start.get_data_from_server(api_key.api_key(),match_id,region)

    # get match time
    match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
    match_time = match_time+timedelta(hours=9)
    match_time_str=match_time.strftime('%Y%m%d_%H%M%S')
    # get roster
    roster_list=func4extract.extract_roster(match)
    map_img_list=[]

    for team_roster_list in roster_list:
        # get map name
        map_img = func4map.load_map(match.map_name)

        # draw aircraft path
        aircraft_path_list=func4extract.extract_aircraft_path(telemetry)
        map_img = func4map.draw_aircraft_path(map_img, aircraft_path_list)

        # draw circle position
        game_state_list=func4extract.extract_circle_position(telemetry)
        map_img = func4map.draw_circle_position(map_img, game_state_list)

        # get lanfing point
        landing_point_list=func4extract.extract_landing_point(telemetry)

        # draw Routing Path
        routing_path_list=func4extract.extract_routing_path(telemetry)
        map_img = func4map.draw_routing_path(map_img, routing_path_list, landing_point_list, team_roster_list, game_state_list)
        map_img = func4map.resize_map(map_img)
        map_img_list.append(map_img)

    return [map_img_list, match_time_str, match, roster_list]

def save_files(match):
    func4savefiles.save_files(match)

def save_img(map_img, match_time_str, match_map_name, team_roster_list):
    map_img.save("./output_files/RoutingPath_"+match_time_str+"_"+match_map_name+str(team_roster_list[0]['team_id']).zfill(2)+".png")


match_id="9bf45f55-3f30-4e36-96a5-d1f850e89955"
region="tournament"
[map_img_list, match_time_str, match, roster_list]=makeRoutingPath(match_id,region)
for num,team_roster_list in enumerate(roster_list):
    save_img(map_img_list[num], match_time_str, match.map_name, team_roster_list)
