#!/usr/bin/env python3
"""
Dynamic GitHub Profile README Updater
Periodically refreshes live telemetry, daily architectural insights,
weather, and real-time status in NURJAKS/NURJAKS.
"""

import re
import urllib.request
import urllib.parse
from datetime import datetime, timezone

QUOTES = [
    "Premature optimization is the root of all evil, but premature distribution is the architect's nightmare. Keep boundaries clean before splitting.",
    "Make it work, make it right, make it fast — strictly in that order. (Kent Beck)",
    "Simplicity is prerequisite for reliability. (Edsger W. Dijkstra)",
    "In distributed systems, expect everything to fail, all the time. Design idempotent retries and resilient fallbacks.",
    "Good code is its own best documentation. As you're about to add a comment, ask yourself, 'How can I improve the code so that this comment isn't needed?'",
    "First, solve the problem. Then, write the code. (John Johnson)",
    "Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. (Linus Torvalds)",
    "Event-driven architecture decouples producers from consumers in time, space, and synchronization.",
    "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable. (Leslie Lamport)",
    "Cache invalidation and naming things are the two hardest problems in computer science. Choose cache TTLs wisely.",
]

def get_weather() -> str:
    cities = ["Almaty", "Kyzylorda", "Astana"]
    for city in cities:
        try:
            url = f"https://wttr.in/{city}?format=%t+(%C)&m"
            req = urllib.request.Request(url, headers={"User-Agent": "curl/7.88.1"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                text = resp.read().decode("utf-8").strip()
                if text and not text.startswith("<") and "Unknown" not in text:
                    return f"{city}: {text}"
        except Exception:
            continue
    return "Almaty: +12°C (Clear)"

def main():
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    now_utc = datetime.now(timezone.utc)
    day_of_year = now_utc.timetuple().tm_yday
    quote = QUOTES[day_of_year % len(QUOTES)]
    weather = get_weather()
    date_str = now_utc.strftime("%d %b %Y, %H:%M UTC")

    dynamic_block = f"""<!-- DYNAMIC_PROFILE:START -->
<div align="center">
  <kbd>📍 {weather}</kbd> • <kbd>⚡ Status: Engineering Scalable Systems</kbd> • <kbd>🔄 Synced: {date_str}</kbd>
</div>

<br/>

> 💡 **Architectural Thought of the Day:**  
> *" {quote} "*

<br/>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=NURJAKS&show_icons=true&theme=radical&hide_border=true&count_private=true" height="150" alt="GitHub Stats"/>
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=NURJAKS&layout=compact&theme=radical&hide_border=true" height="150" alt="Top Languages"/>
</p>
<!-- DYNAMIC_PROFILE:END -->"""

    # Check if markers exist
    if "<!-- DYNAMIC_PROFILE:START -->" in content and "<!-- DYNAMIC_PROFILE:END -->" in content:
        pattern = r"<!-- DYNAMIC_PROFILE:START -->.*?<!-- DYNAMIC_PROFILE:END -->"
        new_content = re.sub(pattern, dynamic_block, content, flags=re.DOTALL)
    else:
        # Insert right after the header block (after the intro blockquote)
        marker = "measurable business impact.\n\n---"
        if marker in content:
            new_content = content.replace(marker, f"measurable business impact.\n\n---\n\n{dynamic_block}\n\n---")
        else:
            # Fallback append
            new_content = dynamic_block + "\n\n" + content

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully updated README.md with dynamic profile telemetry!")

if __name__ == "__main__":
    main()
