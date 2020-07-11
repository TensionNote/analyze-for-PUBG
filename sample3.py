import secret.api as api
from chicken_dinner.pubgapi import PUBG

api_key=api.api_key()
region="pc-as"
player_name="Zoo_SV"

pubg = PUBG(api_key, region)
player = pubg.players_from_names(player_name)[0]


# 一覧取得（44試合分格納）
for i,match_id in enumerate(player.match_ids):
    print(match_id)
    # match_telemetry=pubg.match(match_id).get_telemetry()
    # match_telemetry.playback_animation(format(i)+"_"+match_id+".html")


# 最新分だけ取得
# recent_match_id = player.match_ids[0]
# recent_match = pubg.match(recent_match_id)
# recent_match_telemetry = recent_match.get_telemetry()
# recent_match_telemetry.playback_animation("recent_match.html")