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

    # get map name
    map_img = func4map.load_map(match.map_name)
    # get roster
    roster_list=func4extract.extract_roster(match)
    # get lanfing point
    landing_point_list=func4extract.extract_landing_point(telemetry)
    # draw Routing Path
    routing_path_list=func4extract.extract_routing_path(telemetry)
    map_img = func4map.draw_routing_path(map_img, routing_path_list, landing_point_list, roster_list, 1)
    # # draw aircraft path
    # aircraft_path_list=func4extract.extract_aircraft_path(telemetry)
    # map_img = func4map.draw_aircraft_path(map_img, aircraft_path_list)
    map_img = func4map.resize_map(map_img)
    return [map_img, match_time_str, match]

def save_files(match):
    func4savefiles.save_files(match)

def save_img(map_img, match_time_str, match_map_name):
    map_img.save("./output_files/RoutingPath_"+match_time_str+"_"+match_map_name+".png")


match_id="9bf45f55-3f30-4e36-96a5-d1f850e89955"
region="tournament"
[map_img, match_time_str, match]=makeRoutingPath(match_id,region)
save_img(map_img, match_time_str, match.map_name)
