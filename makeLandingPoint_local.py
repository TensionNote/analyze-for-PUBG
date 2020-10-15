import makeLandingPoint as mlp

# main
match_id_list=[
    "d4e68fef-cb83-4de8-96d3-51f8eccdfc55"
]
for match_id in match_id_list:
    # asia server
    # [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id,"as")

    # tournament server
    region="tournament"
    [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id, region)

    mlp.save_img(map_img, match_time_str, match.map_name, region, match_id)