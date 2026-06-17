import os

BASE = os.path.join(os.getcwd(), "apps")
apps = [d for d in sorted(os.listdir(BASE)) if os.path.isdir(os.path.join(BASE, d))]
apps_with_models = []
apps_with_migrations = {}
apps_with_numeric = []

for app in apps:
    models_dir = os.path.join(BASE, app, "models")
    migrations_dir = os.path.join(BASE, app, "migrations")
    if os.path.isdir(models_dir):
        apps_with_models.append(app)
    if os.path.isdir(migrations_dir):
        files = [f for f in sorted(os.listdir(migrations_dir)) if f.endswith(".py")]
        apps_with_migrations[app] = files
        for f in files:
            if f.startswith("000") and f.endswith(".py"):
                apps_with_numeric.append(app)
                break

print("apps_with_models:", apps_with_models)
print("apps_with_migrations (files):")
for k, v in sorted(apps_with_migrations.items()):
    print("  ", k, v)

print("\napps_with_numeric_migrations:", sorted(set(apps_with_numeric)))
missing = [a for a in apps_with_models if a not in set(apps_with_numeric)]
print("\napps_with_models_but_no_numeric_migrations:", sorted(missing))
