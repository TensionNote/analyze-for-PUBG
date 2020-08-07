import makeRoutingPath as mrp

# main
match_id_list=[
    "54b4e7d1-8017-4b98-896d-3ce588da8622"
]
for match_id in match_id_list:
    # asia server
    [map_img, match_time_str, match]=mrp.makeRoutingPath(match_id,"as")

    # tournament server
    # [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id,"tournament")

    mrp.save_img(map_img, match_time_str, match.map_name)