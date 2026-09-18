#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIFIED = ROOT / "unified"

FILES = [
    "protocol.map.json",
    "governance.map.json",
    "epoch.bindings.json",
    "sovereign.bindings.json",
    "deployment.bindings.json",
    "rootstone.bindings.json",
    "pptf.bindings.json",
    "multi_chain.map.json",
]


def main():
    ok = True
    for name in FILES:
        path = UNIFIED / name
        try:
            with path.open("r", encoding="utf-8") as f:
                json.load(f)
            print(f"[OK] {name}")
        except Exception as e:
            print(f"[ERR] {name}: {e}")
            ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
