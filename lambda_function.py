from datetime import datetime,timedelta
import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from pubg_python import PUBG, Shard
from PIL import Image,ImageDraw,ImageFont
import makeLandingPoint
import makeRoutingPath
import makeScrimResult
import boto3
import requests, json

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    if('date' in event):
        scrim_result_list = makeScrimResult.makeScrimResult(event['date'])
        [year,month,day]=event['date'].split('-')
        newfilepath="/tmp/scrimResult_zoo_"+year+month+day+".txt"
        bucket = "make-landing-point"
        r=json.dumps(scrim_result_list,indent=3)
        with open(newfilepath, mode='w') as f:
            f.write(r)
        key = "output_files/scrimResult_zoo_"+year+month+day+".json"
        s3_client.upload_file(newfilepath, bucket, key)
        return {
            'statusCode': 200,
        }

    elif('teamid' in event):
        match_id=event['match']
        region=event['region']
        team_id=int(event['teamid'])
        [map_img, match_time_str, match, roster_list]=makeRoutingPath.makeRoutingPath(match_id,region,team_id)
        newfilepath="/tmp/RoutingPath_"+match_time_str+"_"+match.map_name+str(roster_list[team_id][0]['team_id']).zfill(2)+".png"
        map_img.save(newfilepath)
        bucket = "make-landing-point"
        key = "output_files/RoutingPath_"+match_time_str+"_"+match.map_name+"_"+region+"_"+match_id+"_"+str(roster_list[team_id][0]['team_id']).zfill(2)+".png"
        s3_client.upload_file(newfilepath, bucket, key)

    else:
        match_id=event['match']
        region=event['region']
        [map_img, match_time_str, match]=makeLandingPoint.makeLandigPoint(match_id,region)
        newfilepath="/tmp/LandingPoint_"+match_time_str+"_"+match.map_name+".png"
        map_img.save(newfilepath)
        bucket = "make-landing-point"
        key = "output_files/LandingPoint_"+match_time_str+"_"+match.map_name+"_"+region+"_"+match_id+".png"
        s3_client.upload_file(newfilepath, bucket, key)

    # return download link
    s3_client.get_object(Bucket=bucket, Key=key)
    url = s3_client.generate_presigned_url(
        ClientMethod = 'get_object',
        Params = {
            'Bucket' : bucket,
            'Key' : key
        },
        ExpiresIn = 3600,
        HttpMethod = 'GET'
    )
    return {
        'statusCode': 200,
        'body': url
    }