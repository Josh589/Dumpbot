from solathon import Client, Transaction, Wallet
from solathon.instructions import Transfer
from solathon.core import Keypair
import binascii

# Initialize the RPC client for Solana Devnet
client = Client("https://devnet.sonic.game", local= True)

# Your sender's private key as a hexadecimal string (replace with your actual private key string)
private_key_hex = "4dA1JvyG9JcjRex8VmQhY94QHMJmJUkHK2J8S2Numoa6etY7sxGDXDrmWFEaNrKk4NBVQxtrEMhY4pfpiu8KdEGZ"

# Decode the private key string from hex to bytes
private_key_bytes = binascii.unhexlify(private_key_hex)

# Create a Wallet from the private key
sender_wallet = Wallet(Keypair.from_secret_key(private_key_bytes))

# Recipient address (replace with actual recipient public key)
recipient_address = "D6ba2oGPfUgedVCWSciscsxrxKoRfpTUcSEzov6Qhc5P"

# Number of transactions
num_transactions = 100

# Amount to send (in lamports, where 1 SOL = 1_000_000_000 lamports)
amount_lamports = 1000000  # 0.001 SOL

# Function to send SOL
def send_sol():
    for _ in range(num_transactions):
        # Create a transfer instruction
        transfer_instruction = Transfer(
            from_public_key=sender_wallet.public_key,
            to_public_key=recipient_address,
            lamports=amount_lamports
        )
        
        # Create a transaction
        transaction = Transaction().add(transfer_instruction)
        
        # Send the transaction
        response = client.send_transaction(transaction, sender_wallet)
        
        # Print the response
        print(f"Transaction signature: {response['result']}")

# Send SOL 100 times
send_sol()
