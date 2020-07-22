import os
import json
import requests

def save_files(match):
    # dirを作成
    # new_dir_path=match.id
    # os.makedirs("./json/"+new_dir_path, exist_ok=True)
    new_dir_path="./"

    # matchをjsonに保存
    # match,assetsオブジェクトのみを格納
    match_data=[]
    match_data.append({"match_type":match.type})
    match_data.append({"match_id":match.id})
    match_data.append(match.attributes)
    match_data.append({"assets_type":match.assets[0].type})
    match_data.append({"assets_id":match.assets[0].id})
    match_data.append(match.assets[0].attributes)
    r=json.dumps(match_data,indent=3)
    with open('./json/'+new_dir_path+'/'+match.id+'_match.json', mode='w') as f:
        f.write(r)

    # telemetryをjsonに保存(urlから取得)
    try:
        asset = match.assets[0]
        r = requests.get(asset.url)
        with open('./json/'+new_dir_path+'/'+match.id+'_telemetry.json', mode='w') as f:
            json.dump(r.json(),f, indent=3)
    except requests.exceptions.RequestException as err:
        print(err)