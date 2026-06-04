import os
import sys
import json
from web3 import Web3

# Define the expected payment contract (e.g., an ERC20 token or an NFT subscription contract on Base)
PAYMENT_CONTRACT_ADDRESS = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913" # USDC on Base (example)
REQUIRED_BALANCE = 50 * 10**6 # 50 USDC (6 decimals)
MY_WALLET = "0x0000000000000000000000000000000000000000" # Replace with real dev wallet

# Minimal ERC20 ABI for balance check
ERC20_ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]')

def verify_subscription(user_wallet: str, rpc_url: str) -> bool:
    if not user_wallet or not rpc_url:
        print("[PAYWALL] No wallet or RPC provided. Access to AI Validation PRO denied.")
        return False

    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not w3.is_connected():
            print(f"[PAYWALL] Failed to connect to RPC: {rpc_url}")
            return False
        
        user_wallet = w3.to_checksum_address(user_wallet)
        contract = w3.eth.contract(address=w3.to_checksum_address(PAYMENT_CONTRACT_ADDRESS), abi=ERC20_ABI)
        
        balance = contract.functions.balanceOf(user_wallet).call()
        
        if balance >= REQUIRED_BALANCE:
            print(f"[PAYWALL] Subscription verified for {user_wallet}. AI Validation PRO unlocked!")
            return True
        else:
            print(f"[PAYWALL] Wallet {user_wallet} does not have the required Pro subscription balance.")
            print(f"[PAYWALL] Required: {REQUIRED_BALANCE / 10**6} USDC. Found: {balance / 10**6} USDC.")
            return False
    except Exception as e:
        print(f"[PAYWALL] Verification error: {e}")
        return False

if __name__ == "__main__":
    wallet = os.environ.get("WALLET_ADDRESS", "")
    rpc = os.environ.get("RPC_URL", "https://mainnet.base.org")
    
    if verify_subscription(wallet, rpc):
        sys.exit(0) # Success
    else:
        sys.exit(1) # Paywall blocked
