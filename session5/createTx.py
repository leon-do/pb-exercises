from ecc import PrivateKey
from helper import decode_base58, p2pkh_script, SIGHASH_ALL
from script import Script
from tx import TxIn, TxOut, Tx

prev_tx_1 = bytes.fromhex('89cbfe2eddaddf1eb11f5c4adf6adaa9bca4adc01b2a3d03f8dd36125c068af4')
prev_index_1 = 0
prev_tx_2 = bytes.fromhex('19069e1304d95f70e03311d9d58ee821e0978e83ecfc47a30af7cd10fca55cf4')
prev_index_2 = 0
target_address = 'muvpVznkBtk8rRSxLRVQRdUhsMjS7aKRne'
target_amount = 1.71
secret = 61740721216174072121
priv = PrivateKey(secret=secret)

# initialize inputs
tx_ins = []
# create the first tx input with prev_tx_1, prev_index_1, blank script_sig and max sequence
tx_ins.append(TxIn(
    prev_tx=prev_tx_1,
    prev_index=prev_index_1,
    script_sig=b'',
    sequence=0xffffffff,
))
# create the second tx input with prev_tx_2, prev_index_2, blank script_sig and max sequence
tx_ins.append(TxIn(
    prev_tx=prev_tx_2,
    prev_index=prev_index_2,
    script_sig=b'',
    sequence=0xffffffff,
))

# initialize outputs
tx_outs = []
# decode the hash160 from the target address
h160 = decode_base58(target_address)
# convert hash160 to p2pkh script
script_pubkey = p2pkh_script(h160)
# convert target amount to satoshis (multiply by 100 million)
target_satoshis = int(target_amount*100000000)
# create a single tx output for target with amount and script_pubkey
tx_outs.append(TxOut(
    amount=target_satoshis,
    script_pubkey=script_pubkey,
))

# create the transaction
tx_obj = Tx(1, tx_ins, tx_outs, 0, testnet=True)

# sign both inputs with the private key using SIGHASH_ALL using sign_input
tx_obj.sign_input(0, priv, SIGHASH_ALL)
tx_obj.sign_input(1, priv, SIGHASH_ALL)

# SANITY CHECK: output's script_pubkey is the same one as your address
if tx_ins[0].script_pubkey(testnet=True).elements[2] != decode_base58(priv.point.address(testnet=True)):
    raise RuntimeError('Output is not something you can spend with this private key. Check that the prev_tx and prev_index are correct')

# SANITY CHECK: fee is reasonable
if tx_obj.fee(testnet=True) > 0.05*100000000 or tx_obj.fee(testnet=True) <= 0:
    raise RuntimeError('Check that the change amount is reasonable. Fee is {}'.format(tx_obj.fee()))

# serialize and hex()
print(tx_obj.serialize().hex())