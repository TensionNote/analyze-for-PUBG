from pubg_python import PUBG, Shard
def get_data_from_server(api_key,match_id,region):
    if region in "tournament":
        api = PUBG(api_key, Shard.PC_TOURNAMENT)
    else:
        api = PUBG(api_key, Shard.PC_AS)
    match = api.matches().get(match_id)
    asset = match.assets[0]
    telemetry = api.telemetry(asset.url)
    return [match,telemetry]