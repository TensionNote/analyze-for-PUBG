import makeLandingPoint as mlp
import makeScrimResult as msr

match_id_list=[


# 11/26
# "17e56327-4ab9-40a2-8b8b-7abaa4ce60d3",
# "150222d2-4b4d-49a3-8d8c-32b1d9a267c4",
# "6db0da98-43d0-4275-a0e9-2a1e60e21949",
# "153f7794-1008-403b-9ddf-0c29225905b6",
# "e6a0107a-d942-40ef-a069-abbbe14a400d"

# 11/27
# "1636b3ce-31c4-4656-819c-550aec448a52",
# "dc26baeb-4cca-4f11-a22f-014df38ce3a2",
# "aa6fb2e7-07a0-4325-8876-9c4cc5633b11",
# "709b7869-77da-435c-91c6-1ddd7f41c1be",
# "d68da603-d55a-4b0c-a4e9-0dbfd30fa129"

# 12/1
# "978beee0-cec8-4d28-b6ca-1ae500643159",
# "54959e58-9ccb-4d63-b63c-8eef5462fe7d",
# "c4f9ee1c-9e80-4afd-8165-0d877008d2b4",
# "95a6c923-e89f-4f1d-865a-5df5b5c57c63",
# "c2f489a6-b568-471c-9136-91589a110ee0"

# 12/5
"bcd8f93d-a3ea-45fc-9291-6d3f3ff67346",
"8839bb20-159c-4c57-87d3-85bd9d98e5e9",
"e4f43639-55e9-47b8-8a6c-4df5ee1a2304",
"02520af6-ff07-463a-ba45-81b3f87c6000",
"08aba395-c462-493e-9376-2c6648539fbf"
]

# for match_id in match_id_list:
#     # region="tournament"
#     region="as"
#     [map_img, match_time_str, match]=mlp.makeLandigPoint(match_id, region)
#     mlp.save_img(map_img, match_time_str, match.map_name, region, match_id)

msr.makeScrimResult_public(match_id_list)