import makeRoutingPath as mrp

match_id_list=[
    "fc1097bc-ce85-4f8e-81a0-cdeb22270fa2"
]
region="tournament"
team_id=12 # Lag gaming

for match_id in match_id_list:
    [map_img, match_time_str, match, roster_list]=mrp.makeRoutingPath(match_id,region,team_id)
    mrp.save_img(map_img, match_time_str, match.map_name, roster_list[team_id])
    # for num,team_roster_list in enumerate(roster_list):
    #         mrp.save_img(map_img_list[num], match_time_str, match.map_name, team_roster_list)
