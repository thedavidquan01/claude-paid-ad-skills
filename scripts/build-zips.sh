#!/usr/bin/env bash
# Rebuild dist/<skill>.zip for each skill. Each zip holds the skill folder at its root,
# which is the shape Claude.ai expects when you upload a skill. Needs python3.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/dist"
python3 - "$ROOT" <<'PY'
import os, sys, zipfile
root = sys.argv[1]
skills = os.path.join(root, "skills")
for name in sorted(os.listdir(skills)):
    src = os.path.join(skills, name)
    if not os.path.isfile(os.path.join(src, "SKILL.md")):
        continue
    out = os.path.join(root, "dist", name + ".zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for d, dirs, files in os.walk(src):
            dirs[:] = sorted(x for x in dirs if x != "__pycache__")
            for f in sorted(files):
                if f == ".DS_Store" or f.endswith(".pyc"):
                    continue
                full = os.path.join(d, f)
                arc = os.path.relpath(full, skills)
                info = zipfile.ZipInfo(arc, date_time=(2026, 1, 1, 0, 0, 0))
                info.external_attr = (os.stat(full).st_mode & 0o777) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                with open(full, "rb") as fh:
                    z.writestr(info, fh.read())
    print("dist/" + name + ".zip")
PY
