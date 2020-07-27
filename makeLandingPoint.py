import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard

# main
match_id_list=[
    "bed6d63d-3556-4bbb-a253-6e01c9d90373"
]
for match_id in match_id_list:
    [map_img, match_time_str, match]=makeLandigPoint(match_id)
    save_img(map_img, match_time_str, match.map_name)
    # save_files(match)


# function
def makeLandigPoint(match_id):
    # get data from Server
    [match,telemetry]=func4start.get_data_from_server(api_key.api_key(),match_id)

    # get match time
    match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
    match_time = match_time+timedelta(hours=9)
    match_time_str=match_time.strftime('%Y%m%d_%H%M%S')

    # get map name
    map_img = func4map.load_map(match.map_name)
    # draw Landing Points
    landing_point_list=func4extract.extract_landing_point(telemetry)
    map_img = func4map.draw_landing_point(map_img, landing_point_list)
    # draw aircraft path
    aircraft_path_list=func4extract.extract_aircraft_path(telemetry)
    map_img = func4map.draw_aircraft_path(map_img, aircraft_path_list)
    map_img = func4map.resize_map(map_img)
    return [map_img, match_time_str, match]

def save_files(match):
    func4savefiles.save_files(match)

def save_img(map_img, match_time_str, match_map_name):
    map_img.save("./output_files/LandingPoint_"+match_time_str+"_"+match_map_name+".png")
