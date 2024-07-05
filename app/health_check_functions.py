from app.cosmos.cosmos import cosmos_health
from app.evm.ethereum import ethereum_health
from app.solana.solana import solana_health

switch = {
    "45": ethereum_health,
    "57": cosmos_health,
    "17": cosmos_health,
    "90": cosmos_health,
    "99": solana_health,
}
