import os, re

base = "LotM Art"
for vol in os.listdir(base):
    vol_path = os.path.join(base, vol)
    if not os.path.isdir(vol_path): continue
    for fname in os.listdir(vol_path):
        fpath = os.path.join(vol_path, fname)
        if not os.path.isfile(fpath): continue
        match = re.match(r'^(\d{4})', fname)
        if not match: continue
        ext = fname.rsplit('.', 1)[-1]
        new_name = match.group(1) + '.' + ext
        new_path = os.path.join(vol_path, new_name)
        if fpath != new_path:
            os.rename(fpath, new_path)
            print(f"{fname[:50]}... -> {new_name}")

print("Done!")
