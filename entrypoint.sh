#!/bin/bash
set -e

CONTRACT_ADDRESS=$1
WALLET_ADDRESS=$2
RPC_URL=$3
GITHUB_TOKEN=$4
ENTERPRISE_KEY=$5

echo "=========================================================="
echo "🛡️ Starting Automated Smart Contract Auditor Pro"
echo "=========================================================="

export WALLET_ADDRESS
export RPC_URL
export GITHUB_TOKEN
export ENTERPRISE_KEY

if [ -z "$CONTRACT_ADDRESS" ]; then
    echo "Scanning entire repository workspace..."
    python /app/security_scanner.py --workspace ${GITHUB_WORKSPACE}
else
    echo "Scanning specific contract: $CONTRACT_ADDRESS"
    python /app/security_scanner.py --address $CONTRACT_ADDRESS
fi
