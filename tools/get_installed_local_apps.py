import re

p = "config/settings/base.py"
s = open(p).read()
# naive parse INSTALLED_APPS list
m = re.search(r"INSTALLED_APPS\s*=\s*\[([\s\S]*?)\]", s)
apps = []
if m:
    body = m.group(1)
    for line in body.splitlines():
        line = line.strip()
        if line.startswith(('"apps.', "'\"apps.")):
            app = line.strip().strip(",").strip('"').strip("'")
            apps.append(app)
print("\n".join(apps))
