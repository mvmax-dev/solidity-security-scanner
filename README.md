# 🛡️ Solidity Security Scanner (AST-Powered)

[![Security Scanner CI](https://github.com/mvmax-dev/solidity-security-scanner/actions/workflows/python-app.yml/badge.svg)](https://github.com/mvmax-dev/solidity-security-scanner/actions/workflows/python-app.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

An advanced, open-source static analysis and vulnerability detection engine for Ethereum and Base smart contracts. Built for Web3 security researchers, auditors, and protocol developers to proactively identify and remediate critical attack vectors.

## 🌟 Key Features
- **AST-Based Analysis**: Deep structural inspection of Solidity code rather than simple regex matching.
- **False-Positive Suppression**: Advanced validation pipelines to filter out noise and focus on real threats.
- **Automated Bounty Integration**: Seamlessly hooks into Immunefi, CodeHawks, and Sherlock for threat intel.
- **Multi-Vector Detection**: Reentrancy, Oracle Manipulation, Flash Loan vectors, and Unprotected Self-Destructs.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Etherscan/Basescan API Keys (for live contract fetching)

### Installation
```bash
git clone https://github.com/mvmax-dev/solidity-security-scanner.git
cd solidity-security-scanner
pip install -r requirements.txt
```

### Usage
Run the scanner against a live contract on Base:
```bash
python security_scanner.py --address 0xYourContractAddress --chain base
```

## 🏗️ Architecture
The system operates in a 3-phase pipeline:
1. **Ingestion**: `codebase_analyzer.py` fetches and indexes verified smart contract code.
2. **Detection**: `security_scanner.py` applies high-fidelity detection rules.
3. **Validation**: `vulnerability_validator.py` cross-references findings to suppress false positives.

## 🤝 Contributing
We welcome contributions from the Web3 security community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit Pull Requests.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Developed by Maxwell Voss | Sovereign Security Intelligence*
