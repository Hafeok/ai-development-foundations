#!/usr/bin/env python3
"""Validate registry/frameworks.yaml against the entry schema."""
import sys, yaml, pathlib

REQUIRED = {"name", "repository", "pillars", "coverage",
            "conformance", "foundation_ref", "maintainer", "license"}
VALID_PILLARS = {"specification", "execution"}

def main() -> int:
    path = pathlib.Path(__file__).with_name("frameworks.yaml")
    data = yaml.safe_load(path.read_text()) or {}
    entries = data.get("frameworks") or []
    errors = []
    seen = set()
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            errors.append(f"entry {i}: not a mapping"); continue
        missing = REQUIRED - e.keys()
        if missing:
            errors.append(f"{e.get('name', f'entry {i}')}: missing {sorted(missing)}")
        pillars = e.get("pillars") or []
        if not pillars or set(pillars) - VALID_PILLARS:
            errors.append(f"{e.get('name', f'entry {i}')}: pillars must be subset of {VALID_PILLARS}")
        for key in ("repository", "conformance"):
            v = e.get(key, "")
            if v and not str(v).startswith("http"):
                errors.append(f"{e.get('name', f'entry {i}')}: {key} should be a URL")
        name = e.get("name")
        if name in seen:
            errors.append(f"duplicate framework name: {name}")
        seen.add(name)
    if errors:
        print("Registry validation FAILED:")
        for x in errors: print("  -", x)
        return 1
    print(f"Registry OK — {len(entries)} framework(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
