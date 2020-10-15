import makeLandingPoint as mlp

# main
match_id_list=[
    # "9fb76056-c130-49d5-994f-475e022bf3a0",
    # "b8fc1c1c-42e5-4842-9de9-c781b6be6f82",
    # "5b49c5ea-ea25-49cc-b62f-706870024266",
    # "f5076cfd-4479-4df2-ad94-e57cc954700b",
    # "e227225a-e89a-4c49-818c-e81857a1d385",
        # "ececb188-f733-4242-b702-6709900e54b6",
    "205c5f4b-ab61-43ae-bcf0-f125f6c8947c",
    "19ce1dae-34a6-434f-bfe1-b65a6883dfa0",
    "1fd34b2a-2c9d-48d9-83de-55b8922d2a8a",
    "362523b4-5feb-44d1-bc5c-656e4faea441",
    "c634608d-7f14-40e9-b967-3d77eb77ce23",
    "15ac3f82-89cf-494d-b1cc-2f1e86d773eb",
    "ce675376-73d0-43fc-bc34-65988c8f0201",
    "fe400505-d09d-46b5-b102-eedfdb657aba",
    "1794abf7-2053-44e0-b9af-03c3a0015d8e",
    "34872775-495c-46e2-abfa-fcc1c066bbfe"
]
for match_id in match_id_list:
    # asia server
    # [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id,"as")

    # tournament server
    region="tournament"
    [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id, region)

    mlp.save_img(map_img, match_time_str, match.map_name, region, match_id)