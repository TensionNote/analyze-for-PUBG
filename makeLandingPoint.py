import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard

match_id="a42d3300-d3d5-46b5-b460-125cc013f75c"

# get data from Server
[match,telemetry]=func4start.get_data_from_server(api_key.api_key(),match_id)

# for save match and telemetry
# func4savefiles.save_files(match)

#get match time
match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
match_time = match_time+timedelta(hours=9)
match_time_str=match_time.strftime('%Y%m%d_%H%M%S')

landing_point_list=func4extract.extract_landing_point(telemetry)
map_img = func4map.load_map(match.map_name)
map_img = func4map.draw_landing_point(map_img, landing_point_list)
map_img = func4map.resize_map(map_img)
map_img.save("./output_files/LandingPoint_"+match_time_str+"_"+match.map_name+".png")
