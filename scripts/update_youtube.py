"""Refresh data/videos.json from the public Stellar Science Club YouTube channel."""
import json, os, subprocess
from datetime import datetime, timezone

CHANNEL = "https://www.youtube.com/@StellarScienceClub/videos"
OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "videos.json"))

cmd = [
    "yt-dlp",
    "--flat-playlist",
    "--dump-json",
    "--playlist-end", "12",
    "--no-warnings",
    "--ignore-errors",
    CHANNEL,
]

result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=240)
entries = []
for line in result.stdout.splitlines():
    try:
        item = json.loads(line)
    except json.JSONDecodeError:
        continue
    if item.get("id"):
        entries.append(item)
if not entries:
    if result.stderr.strip():
        print("yt-dlp reported an error:")
        print(result.stderr.strip()[-2000:])
    print("YouTube returned no videos; keeping existing data/videos.json")
    raise SystemExit(0)

videos=[]
for item in entries:
    vid=item["id"]
    upload_date=item.get("upload_date") or ""
    published=f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}" if len(upload_date)==8 else ""
    videos.append({
        "id":vid,
        "title":item.get("title") or "Untitled video",
        "url":f"https://www.youtube.com/watch?v={vid}",
        "thumbnail":f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        "published":published,
        "duration":item.get("duration_string") or (f"{int(item['duration']) // 60}:{int(item['duration']) % 60:02d}" if isinstance(item.get("duration"), (int, float)) else ""),
    })

payload={
    "updated":datetime.now(timezone.utc).isoformat(),
    "channel":"https://www.youtube.com/@StellarScienceClub",
    "videos":videos,
}
os.makedirs(os.path.dirname(OUTPUT),exist_ok=True)
with open(OUTPUT,"w",encoding="utf-8") as f:
    json.dump(payload,f,ensure_ascii=False,indent=2)
    f.write("\n")
print(f"Updated {OUTPUT} with {len(videos)} videos.")
