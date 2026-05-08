# Sharingan NIDS
**Network Intrusion Detection & Prevention System with Host‑based Blocking**

A production‑ready Network Intrusion Detection and Prevention System (NIDPS) that detects 15 types of network attacks with 96.5% accuracy and optionally blocks attacker IPs using the Linux firewall (iptables). Built with Random Forest, Streamlit, and deployed on Kali Linux.

---

## Features
- Detects **15 attack types**: DDoS, PortScan, Web Attacks, Infiltration, Bot, Heartbleed, DoS variants, FTP/SSH Patator, etc.
- **96.5% accuracy** using Random Forest (tested on balanced CIC‑IDS‑2017 dataset)
- **Active Response**: Automatically blocks attacker IPs via `iptables` (host‑based prevention)
- **Interactive Web Interface**: Upload CSV, view detection results, optionally enable IP blocking
- **Incident Reporting**: Download detailed reports of detected attacks
- **Optional** real‑time packet capture (can be extended with `scapy`)

---

## Repository Contents
| File | Description |
|------|-------------|
| `ids_app.py` | Main Streamlit web application |
| `rf_model.pkl` | Trained Random Forest model |
| `scaler.pkl` | StandardScaler fitted on training data |
| `label_encoder.pkl` | LabelEncoder for attack class mapping |
| `feature_columns.pkl` | List of 78 feature columns |
| `mixed_test_with_ip.csv` | Sample test CSV with source IPs for demo |
| `requirements.txt` | Python dependencies |

---

## System Requirements
- **Operating System**: Linux (Kali, Ubuntu, or any Debian‑based distro with `iptables`)
- **Python**: 3.9 or higher
- **Disk Space**: ~2 GB (including virtual environment and libraries)
- **Permissions**: `sudo` access for iptables blocking (optional)

---

## Installation & Environment Setup

### Step 1: Clone the repository (or download files)
```bash
git clone https://github.com/jannatuldev/Sharingan-NIDS.git
cd Sharingan-NIDS
