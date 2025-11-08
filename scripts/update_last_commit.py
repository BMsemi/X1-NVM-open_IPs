#!/usr/bin/env python3
import os, re, sys, json
from datetime import datetime, timezone
from urllib.request import Request, urlopen

REPOS = [
    "final3blindside/HE-PSMRC",
    "DhruvBDixit/Caravel-based_ReRAM-Accelerated_Safe-State_Logger_for_Edge_Devices",
    "Juan-AquinoH/secure_logger_controller",
    "ebatzolis/ReRAM-Based-Ultra-Low-Power-ECG-Anomaly-Detector-with-Patient-Adaptive-Learning",
    "mthudaa/har_reram",
    "ha-jer-9/smart_pwm",
    "partcleda/caravel_user_neuromorphic_comp",
    "Lefteris-B/ReRAM-Accelerated-Edge-Intelligence-Processor",
    "schizoneko/EDABK_SNN_CIM",
]

TOKEN = os.environ.get("GITHUB_TOKEN", "")
HEADERS = {
    "User-Agent": "bm-labs-readme-updater",
    "Accept": "application/vnd.github+json",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

def gh_get(url):
    req = Request(url, headers=HEADERS)
    with urlopen(req) as r:
        return json.loads(r.read().decode("utf-8"))

def fmt_date_ago(iso):
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(timezone.utc)
    now = datetime.now(timezone.utc)
    days = (now - dt).days
    # e.g., "Oct 24, 2025 · 16 days ago"
    return f"{dt.strftime('%b %d, %Y')} · {days} day{'s' if days != 1 else ''} ago"

def replace_marker(text, repo, val):
    pattern = rf"<!--LAST_COMMIT:{re.escape(repo)}-->.*?<!--/LAST_COMMIT-->"
    repl = f"<!--LAST_COMMIT:{repo}--><strong>{val}</strong><!--/LAST_COMMIT-->"
    return re.sub(pattern, repl, text, flags=re.DOTALL)

def main():
    readme_path = os.path.join(os.getcwd(), "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        md = f.read()

    for repo in REPOS:
        api = f"https://api.github.com/repos/{repo}"
        data = gh_get(api)
        # Prefer pushed_at; fallback to updated_at
        iso = data.get("pushed_at") or data.get("updated_at")
        if not iso:
            iso = datetime.now(timezone.utc).isoformat()
        human = fmt_date_ago(iso)
        md = replace_marker(md, repo, human)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)

if __name__ == "__main__":
    sys.exit(main())
