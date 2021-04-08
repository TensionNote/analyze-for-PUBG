import makeLandingPoint as mlp

# main
match_id_list=[
    "9b19453a-b405-4d6b-8520-00fc7e37b5f5",
    "5b07293d-f8b9-4cd8-8686-063578cc3449",
    "bc8ae0d0-8c24-4a54-b35e-6614d9c400fb",
    "1ae1f9b8-40e9-40ae-b61f-47d809ea4b2e",
    "d3724f65-1ecc-4046-af21-1de625986adb"
]
for match_id in match_id_list:
    # asia server
    region="as"
    [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id,region)

    # tournament server
    # region="tournament"
    # [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id, region)

    # mlp.save_img(map_img, match_time_str, match.map_name, region, match_id)