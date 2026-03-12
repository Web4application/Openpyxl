export RUNNER_VERSION=$(curl -X 'GET' https://data.forgejo.org/api/v1/repos/forgejo/runner/releases/latest | jq .name -r | cut -c 2-)

wget -O forgejo-runner https://code.forgejo.org/forgejo/runner/releases/download/v${RUNNER_VERSION}/forgejo-runner-${RUNNER_VERSION}-linux-amd64

chmod +x forgejo-runner

wget -O forgejo-runner.asc https://code.forgejo.org/forgejo/runner/releases/download/v${RUNNER_VERSION}/forgejo-runner-${RUNNER_VERSION}-linux-amd64.asc

gpg --keyserver keys.openpgp.org --recv EB114F5E6C0DC2BCDD183550A4B61A2DC5923710

gpg --verify forgejo-runner.asc forgejo-runner

#!/bin/bash
set -e

# 1️⃣ Fetch latest version
RUNNER_VERSION=$(curl -s https://data.forgejo.org/api/v1/repos/forgejo/runner/releases/latest | jq -r .name | cut -c2-)
echo "Latest Forgejo Runner version: $RUNNER_VERSION"

# 2️⃣ Download binary and signature
wget -O forgejo-runner https://code.forgejo.org/forgejo/runner/releases/download/v${RUNNER_VERSION}/forgejo-runner-${RUNNER_VERSION}-linux-amd64
wget -O forgejo-runner.asc https://code.forgejo.org/forgejo/runner/releases/download/v${RUNNER_VERSION}/forgejo-runner-${RUNNER_VERSION}-linux-amd64.asc

# 3️⃣ Make binary executable
chmod +x forgejo-runner

# 4️⃣ Import Forgejo GPG key
gpg --keyserver keys.openpgp.org --recv EB114F5E6C0DC2BCDD183550A4B61A2DC5923710

# 5️⃣ Verify the download
gpg --verify forgejo-runner.asc forgejo-runner

echo "✅ Forgejo Runner $RUNNER_VERSION downloaded, verified, and ready to use!"

RUNNER_VERSION=$(curl -s https://data.forgejo.org/api/v1/repos/forgejo/runner/releases/latest | jq -r .name | cut -c2-) && \
wget -O forgejo-runner https://code.forgejo.org/forgejo/runner/releases/download/v${RUNNER_VERSION}/forgejo-runner-${RUNNER_VERSION}-linux-amd64 && \
wget -O forgejo-runner.asc https://code.forgejo.org/forgejo/runner/releases/download/v${RUNNER_VERSION}/forgejo-runner-${RUNNER_VERSION}-linux-amd64.asc && \
chmod +x forgejo-runner && \
gpg --keyserver keys.openpgp.org --recv EB114F5E6C0DC2BCDD183550A4B61A2DC5923710 && \
gpg --verify forgejo-runner.asc forgejo-runner && \
echo "✅ Forgejo Runner $RUNNER_VERSION downloaded, verified, and ready!"

sudo tee /etc/systemd/system/forgejo-runner.service > /dev/null <<EOF
[Unit]
Description=Forgejo Runner
After=network.target

[Service]
ExecStart=/path/to/forgejo-runner run
Restart=always
User=<your-user>
WorkingDirectory=/path/to
Environment=PATH=/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable forgejo-runner
sudo systemctl start forgejo-runner

nohup ./forgejo-runner run > runner.log 2>&1 &

forgejo-runner run
# Executes deployment scripts in workflow

# finalize signed PSBT
bitcoin-cli finalizepsbt "signed_psbt_base64"
# then sendrawtransaction or use wallet process
bitcoin-cli -rpcwallet="cold-wallet" 
sendrawtransaction <hex>

sudo systemctl list-units --type=service --state=running | egrep -i 'miner|xmrig|cgminer|t-rex|mining'
sudo grep -RIn 'xmrig\|cgminer\|miner\|t-rex' /etc/systemd/ /etc/init.d/ /etc/cron* /var/spool/cron 2>/dev/null || true
crontab -l 2>/dev/null || true
sudo crontab -l 2>/dev/null || true

# live: shows remote IPs & ports
sudo ss -tupn | egrep -i 'xmrig|cgminer|bfgminer|ethminer|t-rex|minerd|docker' --color=never
# or filter by ports commonly used by pools e.g., 3333,4444,4445,3334,3335,9000,33333
sudo ss -tnp | egrep -i ':333|:444|:9000|:3333|:3334|:4444|:5555' --color=never
# resolve IPs to hostnames
sudo ss -tnp | awk '{print $5}' | cut -d: -f1 | sort -u | xargs -r -n1 -I{} sh -c 'echo "{} -> $(dig +short -x {} 2>/dev/null || true)"'

docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Command}}"
# inspect env/config for each suspected container:
docker inspect <container-id> --format '{{json .Config.Env}}' | jq .
# list mounted files (could reveal config)
docker inspect <container-id> --format '{{json .Mounts}}' | jq .


# search common locations and the whole home partition (may take a while)
sudo grep -RIn --binary-files=without-match -e 'wallet\|address\|user\|payout\|pool\|rig-id' /etc /home /opt /root 2>/dev/null | head -n 200
# look for json/ini configs
sudo find / -type f \( -name '*.conf' -o -name '*.json' -o -name '*.toml' -o -name '*.cfg' -o -name '*.ini' \) -exec grep -IiH --line-number -e 'wallet\|address\|user\|pool\|payout' {} \; 2>/dev/null | head -n 200

PID=<pid_from_above>
ps -o pid,user,cmd -p $PID -f
sudo lsof -p $PID                  # files/socket the process has open
sudo cat /proc/$PID/cmdline | tr '\0' ' ' && echo

ps aux | egrep -i 'xmrig|cgminer|bfgminer|ethminer|nbminer|lolMiner|minerd|t-rex|phoenixminer|sgminer' --color=never

#!/usr/bin/env python3
# find_wallet_backups.py
# Search your filesystem for likely wallet backup filenames & common keywords.
# Harmless: it only reads filenames and small file snippets (no decryption).

import os
import sys

# directories to scan (change as needed). Example defaults:
DEFAULT_PATHS = [
    os.path.expanduser("~"),
    "/mnt", "/media", "/Volumes"  # common mount points (Linux/Mac)
]

FILENAME_KEYWORDS = [
    "wallet", "wallet.dat", "backup", "seed", "mnemonic", "electrum",
    ".json", ".dat", "walletbackup", "crescent", "keystore",
    "trust", "exodus", "ledger", "trezor", "backup-wallet"
]

CONTENT_KEYWORDS = [
    "seed phrase", "mnemonic", "twelve", "twenty", "seed:", "mnemonic:",
    "bitcoin", "electrum", "wallet"
]

MAX_FILE_PREVIEW = 4096  # bytes

def scan_path(path, max_items=100000):
    found = []
    count = 0
    for root, dirs, files in os.walk(path):
        for fn in files:
            count += 1
            if count > max_items:
                return found, True
            lower = fn.lower()
            match_name = any(k in lower for k in FILENAME_KEYWORDS)
            if match_name:
                found.append(os.path.join(root, fn))
                continue
            # optionally peek into small text files
            try:
                full = os.path.join(root, fn)
                if os.path.getsize(full) > 5_000_000:  # skip large files
                    continue
                with open(full, "rb") as f:
                    sample = f.read(MAX_FILE_PREVIEW)
                try:
                    text = sample.decode("utf-8", errors="ignore").lower()
                except:
                    text = ""
                if any(k in text for k in CONTENT_KEYWORDS):
                    found.append(full)
            except Exception:
                continue
    return found, False

def main():
    paths = DEFAULT_PATHS.copy()
    if len(sys.argv) > 1:
        paths = sys.argv[1:]  # allow user to pass custom paths
    all_found = []
    for p in paths:
        if not os.path.exists(p):
            continue
        print(f"Scanning {p} ... (this can take a while)")
        found, truncated = scan_path(p)
        all_found.extend(found)
        if truncated:
            print("Scan truncated due to item limit. Re-run with narrower paths if needed.")
    if not all_found:
        print("No likely wallet/backup files found in scanned locations.")
        return
    print("\nPossible matches (inspect these files carefully):\n")
    for i, f in enumerate(sorted(set(all_found)), 1):
        print(f"{i}. {f}")
    print("\nNotes:")
    print("- If you find wallet files (e.g. wallet.dat or .json), do NOT upload your seed or private key anywhere.")
    print("- If files are encrypted and you remember parts of the password, recovery tools like btcrecover may help.")
    print("- If you need, paste a filename here (not its contents) and I’ll tell you what it likely is and next steps.")

if __name__ == "__main__":
    main()

