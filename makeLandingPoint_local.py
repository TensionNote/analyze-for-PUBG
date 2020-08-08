import makeLandingPoint as mlp

# main
match_id_list=[
    # "273bc463-29ac-4de3-82af-de914ddd22e9",
    # "8afb0de3-56d3-489a-b671-2c414a3d248f",
    # "96f32aa4-da23-44fe-bfbe-93a9bc2eaeb8",
    # "e234730b-ace5-4a66-9b49-75f394183d96",
    "54b4e7d1-8017-4b98-896d-3ce588da8622"
]
for match_id in match_id_list:
    # asia server
    [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id,"as")

    ## tournament server
    # [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id,"tournament")

    mlp.save_img(map_img, match_time_str, match.map_name)