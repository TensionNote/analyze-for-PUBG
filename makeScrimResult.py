import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard
import csv,pprint

def makeScrimResult(year,month,day):
    api = PUBG(api_key.api_key(), Shard.PC_TOURNAMENT)
    scrim_result_list=[]
    rank_pts_list={
        "1":10,
        "2":6,
        "3":5,
        "4":4,
        "5":3,
        "6":2,
        "7":1,
        "8":1,
        "9":0,
        "10":0,
        "11":0,
        "12":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0
    }
    map_name_list={
        "Desert_Main":"Miramar",
        "Baltic_Main":"Erangel"
    }
    name="test-pjssc"
    for match in (api.tournaments().get(name)).matches:
        match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
        if([match_time.year, match_time.month, match_time.day] == [year, month ,day]):
            matchDetail=func4start.get_matchData_from_server(api_key.api_key(),match.id,"tournament")
            for rosters in matchDetail.rosters:
                for participants in rosters.participants:
                    if( "zoo" in participants.name.lower()):
                        pts=sum(item.kills for item in rosters.participants)+rank_pts_list[str(rosters.stats['rank'])]
                        scrim_result_list.append(
                            {
                                'map_name': map_name_list[str(matchDetail.map_name)],
                                'rank': rosters.stats['rank'],
                                'pts': pts
                            })
                        break
    return scrim_result_list
