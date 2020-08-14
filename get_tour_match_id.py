# 20200801 調整中

import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard
import csv,pprint

api = PUBG(api_key.api_key(), Shard.PC_TOURNAMENT)

# get list
tournaments = api.tournaments()
match_list=[]
# for tournament in tournaments:
#     match_list.append([tournament.id])
# with open('./output_files/tournament_match_list.csv') as f:
#     reader = csv.reader(f)
#     l = [row for row in reader]

# for name in l:
#     match_list=[]
name="sea-pis2"
for i,match in enumerate((api.tournaments().get(name)).matches):
    match_list.append([match.id,match.attributes['createdAt']])
    if i>5:
        break
pprint.pprint(match_list)


# CSV出力（テスト用）
# with open('./output_files/tournament_match_list_'+name+'.csv', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     writer.writerows(match_list)
