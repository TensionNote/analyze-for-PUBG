import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard
import csv,pprint,json,requests

def makeScrimResult(date):
    [year,month,day]=(int(s) for s in date.split('-'))
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
        "13":0,
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
                        high_pts="　"
                        if pts>9:
                            high_pts="★"
                        scrim_result_list.append(
                            {
                                'map_name': map_name_list[str(matchDetail.map_name)],
                                'rank': rosters.stats['rank'],
                                'pts': pts,
                                'id':matchDetail.id,
                                'high_pts':high_pts
                            })
                        break

    # send scrim result to Dscord
    result_list=[]
    result_list.append("**"+date+"**")
    for i in reversed(scrim_result_list):
        result_list.append('{high_pts} {map_name} {rank}位 {pts}pt'.format(
                high_pts=i['high_pts'],
                map_name=i['map_name'],
                rank=str(i['rank']),
                pts=str(i['pts']),
                )
        )
    resultStr="\r".join(result_list)
    webhook_url = api_key.discord4scrim_result()
    main_content = {'content': resultStr}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json.dumps(main_content), headers=headers)

    # send match id to Discord
    result_list=[]
    result_list.append("**"+date+"**")
    for i in reversed(scrim_result_list):
        result_list.append('{id}'.format(id=str(i['id']))
    )
    resultStr="\r".join(result_list)
    webhook_url  = api_key.discord4match_id()
    main_content = {'content': resultStr}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json.dumps(main_content), headers=headers)

    return scrim_result_list


def makeScrimResult_public(match_list):
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
        "13":0,
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
    region="as"
    for match_id in match_list:
        match=func4start.get_matchData_from_server(api_key.api_key(),match_id,region)
        match_time = datetime.strptime(match.attributes['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
        matchDetail=func4start.get_matchData_from_server(api_key.api_key(),match.id,"as")
        for rosters in matchDetail.rosters:
            for participants in rosters.participants:
                if( "zoo_sv" in participants.name.lower()):
                    pts=sum(item.kills for item in rosters.participants)+rank_pts_list[str(rosters.stats['rank'])]
                    high_pts="　"
                    if pts>9:
                        high_pts="★"
                    scrim_result_list.append(
                        {
                            'map_name': map_name_list[str(matchDetail.map_name)],
                            'rank': rosters.stats['rank'],
                            'pts': pts,
                            'id':matchDetail.id,
                            'high_pts':high_pts
                        })
                    break

    # send scrim result to Dscord
    result_list=[]
    result_list.append("**"+str(match_time.year)+"-"+str(match_time.month)+"-"+str(match_time.day)+"**")
    for i in reversed(scrim_result_list):
        result_list.append('{high_pts} {map_name} {rank}位 {pts}pt'.format(
                high_pts=i['high_pts'],
                map_name=i['map_name'],
                rank=str(i['rank']),
                pts=str(i['pts']),
                )
        )
    resultStr="\r".join(result_list)
    webhook_url = api_key.discord4scrim_result()
    main_content = {'content': resultStr}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json.dumps(main_content), headers=headers)

    # send match id to Discord
    result_list=[]
    result_list.append("**"+str(match_time.year)+"-"+str(match_time.month)+"-"+str(match_time.day)+"(public)"+"**")
    for i in reversed(scrim_result_list):
        result_list.append('{id}'.format(id=str(i['id']))
    )
    resultStr="\r".join(result_list)
    webhook_url  = api_key.discord4match_id()
    main_content = {'content': resultStr}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json.dumps(main_content), headers=headers)

    return scrim_result_list
