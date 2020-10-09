import secret.api as api_key
import modules.func4map as func4map
import modules.func4extract as func4extract
import modules.func4savefiles as func4savefiles
import modules.func4start as func4start
from datetime import datetime,timedelta
from pubg_python import PUBG, Shard

def makeRosterList(match_id,region):
    ## get data from Server
    # region is "AS" or "TOURNAMENT"
    match=func4start.get_matchData_from_server(api_key.api_key(),match_id,region)
    # get roster
    roster_list=func4extract.extract_roster(match)
    return roster_list

## For debug
match_id="fc1097bc-ce85-4f8e-81a0-cdeb22270fa2"
region="tournament"
roster_list=makeRosterList(match_id, region)
print("")