#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse -- make.fun entry.

Writes one line (at most 140 characters) to /output/entry.txt: the
robot vacuum's own excuse for missing a spot, in its own voice.
"""

import os

EXCUSE = "My lidar mapped that crumb as a load-bearing wall, so I circled it twice, saluted, and filed a formal complaint with the dustbin."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
