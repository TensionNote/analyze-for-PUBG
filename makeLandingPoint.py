import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard

match_id_list=[
    "42fdc4a7-9f71-42d7-9ffe-f907a94a126a",
    "de5eaaec-9630-48ee-8882-371990e71dc9",
    "effcbe97-65ca-4643-8d63-875835841b5c",
    "d8c95e48-666a-4cce-b0cc-8f6544f2ba28",
    "9f66d629-5d0c-4a77-860a-5d3593a44730",
]

for match_id in match_id_list:
    # get data from Server
    [match,telemetry]=func4start.get_data_from_server(api_key.api_key(),match_id)

    # for save match and telemetry
    # func4savefiles.save_files(match)

    #get match time
    match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
    match_time = match_time+timedelta(hours=9)
    match_time_str=match_time.strftime('%Y%m%d_%H%M%S')


    map_img = func4map.load_map(match.map_name)

    landing_point_list=func4extract.extract_landing_point(telemetry)
    map_img = func4map.draw_landing_point(map_img, landing_point_list)

    aircraft_path_list=func4extract.extract_aircraft_path(telemetry)
    map_img = func4map.draw_aircraft_path(map_img, aircraft_path_list)

    map_img = func4map.resize_map(map_img)
    map_img.save("./output_files/LandingPoint_"+match_time_str+"_"+match.map_name+".png")
