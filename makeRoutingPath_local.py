import makeRoutingPath as mrp

match_id_list=[
    "fc1097bc-ce85-4f8e-81a0-cdeb22270fa2",
    "90ad4ffc-1b8c-447e-9cda-10f53e68428c",
    "ee107d05-824b-4e85-bfdd-52f607037f5a",
    "27428f64-f218-4a3f-9209-b360164a8257",
    "6d2e5529-c292-4719-827e-e66f75039de1",
    "c300cd9d-9a15-4e1b-a523-8da297e96ab0",
    "a66e49ae-598e-4751-bd1c-a51c09cffb34",
    "9bf45f55-3f30-4e36-96a5-d1f850e89955",
    "0c4bee5e-a90e-415e-b632-a764071eb20f",
    "f9d6fccf-1810-4653-8ab2-16e3e2363016",
    "404c9b50-a5e1-4ef2-9464-0ee0f18083ab",
    "436c50b8-edd1-4748-930a-b0a26348415b",
    "4fcddc50-5679-4a89-a3bb-977a6b14a23b",
    "f29cfb5f-ae8f-4fd6-8acb-0edb8384be80",
    "77372ae6-159e-448b-bb26-158611e7c27a",
    "77372ae6-159e-448b-bb26-158611e7c27a",
    "5047ded9-82c0-485f-bca2-bc9563e06ae3",
    "55f406d9-e1a1-48ab-9a7e-72701a8fdd96"
]
region="tournament"
team_id=12 # Lag gaming

for match_id in match_id_list:
    [map_img_list, match_time_str, match, roster_list]=mrp.makeRoutingPath(match_id,region,team_id)
    mrp.save_img(map_img_list[0], match_time_str, match.map_name, roster_list[team_id])
    # for num,team_roster_list in enumerate(roster_list):
    #         mrp.save_img(map_img_list[num], match_time_str, match.map_name, team_roster_list)
