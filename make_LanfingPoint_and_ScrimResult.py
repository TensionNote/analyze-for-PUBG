import makeLandingPoint as mlp
import makeScrimResult as msr

match_id_list=[
    "a6848794-c2bc-406d-bb43-5a5bb84cec8f",
    "e47ce7bc-f313-4139-af98-5df979e2f5ee",
    "08906ee7-1f32-49de-bde0-fae3c67397b1",
    "d1d16426-11b2-44db-9d5e-5baf4a76537d",
    "c5d6bb4c-7c1b-4ec3-98a6-5fce09e44d96"
]

for match_id in match_id_list:
    # region="tournament"
    # region="as"
    [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id, region)
    mlp.save_img(map_img, match_time_str, match.map_name, region, match_id)

msr.makeScrimResult_public(match_id_list)