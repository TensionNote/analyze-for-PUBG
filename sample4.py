import modules.api as api_key
from pubg_python import PUBG, Shard
api = PUBG(api_key.api_key(), Shard.PC_AS)

players = api.players().filter(player_names=['E_Nabejunbi'])
player = players[0]

for match in player.matches:
    print(match)
