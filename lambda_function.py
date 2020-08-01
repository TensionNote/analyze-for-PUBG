from datetime import datetime,timedelta
import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from pubg_python import PUBG, Shard
from PIL import Image,ImageDraw,ImageFont
import makeLandingPoint
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    match_id=event['match']

    [map_img, match_time_str, match]=makeLandingPoint.makeLandigPoint(match_id)

    newfilepath="/tmp/LandingPoint_"+match_time_str+"_"+match.map_name+".png"
    map_img.save(newfilepath)

    bucket = "make-landing-point"
    key = "output_files/LandingPoint_"+match_time_str+"_"+match.map_name+".png"
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