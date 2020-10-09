import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard
import csv,pprint

# serch date
[year, month, day]=[2020, 10, 7]

api = PUBG(api_key.api_key(), Shard.PC_TOURNAMENT)

# get list
tournaments = api.tournaments()
match_list=[]

name="test-pjssc"
for i,match in enumerate((api.tournaments().get(name)).matches):
    match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
    if([match_time.year, match_time.month, match_time.day] == [year, month ,day]):
        match_list.append(func4start.get_matchData_from_server(api_key.api_key(),match.id,"tournament"))
        pprint.pprint(match_list)

# get match timematch_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
# match_time = match_time+timedelta(hours=9)
# match_time_str=match_time.strftime('%Y%m%d_%H%M%S')



# チームメンバー抽出
match.rosters[0].participants[0].name
match.rosters[0].participants[0].kills
# チームランク抽出
match.rosters[0].stats['rank']
