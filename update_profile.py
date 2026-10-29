#!/usr/bin/env python3
"""
Dynamic GitHub Profile README Updater
Periodically rotates daily architectural insights and engineering principles
in NURJAKS/NURJAKS while maintaining a clean, high-signal profile.
"""

import re
from datetime import datetime, timezone

PRINCIPLES = [
    "Simplicity is prerequisite for reliability. (Edsger W. Dijkstra)",
    "Make it work, make it right, make it fast — strictly in that order. (Kent Beck)",
    "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable. (Leslie Lamport)",
    "In distributed systems, expect everything to fail all the time. Design idempotent retries and resilient fallbacks.",
    "Premature optimization is the root of all evil, but premature distribution is the architect's nightmare. Keep boundaries clean.",
    "Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. (Linus Torvalds)",
    "Event-driven architecture decouples producers from consumers in time, space, and synchronization.",
    "Cache invalidation and naming things are the two hardest problems in computer science. Choose cache TTLs wisely.",
    "First, solve the problem. Then, write the code. (John Johnson)",
    "Good architecture is about making decisions easy to change later as requirements evolve."
]

def main():
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")
        return

    now_utc = datetime.now(timezone.utc)
    day_of_year = now_utc.timetuple().tm_yday
    quote = PRINCIPLES[day_of_year % len(PRINCIPLES)]

    dynamic_block = f"""<!-- DYNAMIC_PROFILE:START -->
<div align="center">
  <sub>💭 Architectural Principle: <i>"{quote}"</i></sub>
</div>
<!-- DYNAMIC_PROFILE:END -->"""

    if "<!-- DYNAMIC_PROFILE:START -->" in content and "<!-- DYNAMIC_PROFILE:END -->" in content:
        pattern = r"<!-- DYNAMIC_PROFILE:START -->.*?<!-- DYNAMIC_PROFILE:END -->"
        new_content = re.sub(pattern, dynamic_block, content, flags=re.DOTALL)
    else:
        new_content = content.rstrip() + "\n\n" + dynamic_block + "\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully updated README.md with daily architectural principle.")

if __name__ == "__main__":
    main()
