# 🛡️ Solidity Security Scanner PRO (GitHub Action)

[![Security Scanner CI](https://github.com/mvmax-dev/solidity-security-scanner/actions/workflows/python-app.yml/badge.svg)](https://github.com/mvmax-dev/solidity-security-scanner/actions/workflows/python-app.yml)
[![Marketplace](https://img.shields.io/badge/GitHub-Marketplace-blue)](https://github.com/marketplace)
[![Web3 Paywall](https://img.shields.io/badge/Payment-Crypto_USDC-green)](#pro-version--web3-paywall)

**Automated Smart Contract Audit**, **DeFi Security**, **Web3 GitHub Action**, **Solidity Auditor**, **Smart Contract Security Bot**.

An advanced, open-source static analysis and AI vulnerability detection engine for Ethereum and Base smart contracts. Built for Web3 security researchers, auditors, and protocol developers. 

Now available as a seamless **GitHub Action** to automatically secure your Pull Requests!

## 🚀 Quick Start (GitHub Action)

Add the following workflow to your repository to automatically scan your smart contracts on every Pull Request:

```yaml
name: "Web3 Security Audit"
on: [pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Solidity Security Scanner PRO
        uses: mvmax-dev/solidity-security-scanner@main
        with:
          # Optional: Specify your wallet address to unlock AI Validation PRO features
          wallet_address: "0xYourWalletAddress"
```

## 💎 PRO Version & Web3 Paywall

The basic `Slither` structural analysis is 100% free. 
However, **AI Vulnerability Validation** (which suppresses false positives and detects deep logical flaws) is secured behind a decentralized Web3 Paywall.

**To Unlock PRO:**
1. Send **50 USDC** on the **Base Network** to `0x0000000000000000000000000000000000000000` (Replace with your actual payment address).
2. Add your wallet address to the `wallet_address` input in your GitHub workflow.
3. The Action will query the blockchain via RPC. Once payment is verified, the AI Validator automatically unlocks!

## 🏗️ Architecture

1. **Ingestion**: Fetches and indexes verified smart contract code.
2. **Detection**: Applies high-fidelity detection rules (Reentrancy, MEV vectors, Flash Loans).
3. **Web3 Paywall**: Verifies your subscription via Base RPC.
4. **AI Validation**: PRO feature that cross-references findings to suppress false positives.

## 🤝 Contributing & Security

Please see our [Contributing Guidelines](CONTRIBUTING.md) and [Security Policy](SECURITY.md).

## 📜 License
MIT License - see the [LICENSE](LICENSE) file for details.
