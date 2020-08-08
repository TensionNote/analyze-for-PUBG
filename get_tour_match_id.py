# 20200801 調整中

import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard

api = PUBG(api_key.api_key(), Shard.PC_TOURNAMENT)

## get list
# tournaments = api.tournaments()
# for tournament in tournaments:
#     print(tournament)

# get match id
tournament = api.tournaments().get('jp-pjs20')
for match_object in tournament.matches:
    print(match_object.id)

print("")
