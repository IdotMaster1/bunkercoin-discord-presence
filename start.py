from pypresence import Presence
import time
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

user = "username"
password = "password"

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14201" % (user, password))
client_id = '1136437276612767795'
RPC = Presence(client_id)
RPC.connect()

def get_block_height():
    return rpc_connection.getblockcount()

def get_wallet_balance():
    return rpc_connection.getbalance()

while True:
    block_height = get_block_height()
    wallet_balance = get_wallet_balance()

    # Update the presence with state, details, and small_text
    RPC.update(
        state=f"Block Height: {block_height}",
        details=f"Wallet balance: {wallet_balance}",
        buttons=[{"label": "Website", "url": "https://bunkercoin.org"}, {"label": "Github", "url": "https://github.com/bunkercoin/bunkercoin"}]
    )

    time.sleep(15)