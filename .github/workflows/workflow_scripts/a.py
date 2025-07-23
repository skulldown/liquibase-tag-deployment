import sys
import json

# Ensure we have all arguments
if len(sys.argv) < 4:
    print("Usage: a.py <CHANGED_FILES> <NEWER_TAG> <DEPLOYMENT_JSON>")
    sys.exit(1)

changed_files_raw = sys.argv[1]
newer_tag = sys.argv[2]
deployment_json_raw = sys.argv[3]

print("== Received Parameters ==")
print(f"CHANGED_FILES: {changed_files_raw}")
print(f"NEWER_TAG: {newer_tag}")
print(f"DEPLOYMENT_JSON: {deployment_json_raw}\n")

# Split the changed files using the | delimiter
changed_files_list = changed_files_raw.split('|')

# Allowed top-level folders
allowed_folders = {
    "QUALITY",
    "AUDIT",
    "RZ",
    "RCZ",
    "TZ",
    "CZ",
    "SECURITY",
    "MULESOFT",
    "DATA_SHARE",
    "WORK_FLOW_TEST"
}

# Filter files based on first folder name
filtered_files = []
for file_path in changed_files_list:
    file_path = file_path.strip()
    if not file_path:
        continue
    first_folder = file_path.split('/')[0].upper()
    if first_folder in allowed_folders:
        filtered_files.append(file_path)

# Print filtered results
print("== Filtered Changed Files ==")
for f in filtered_files:
    print(f"- {f}")

# Parse deployment JSON
try:
    deployment_data = json.loads(deployment_json_raw)
except json.JSONDecodeError as e:
    print(f"\n❌ Failed to parse DEPLOYMENT_JSON: {e}")
    sys.exit(1)

# Filter deployment info for changed files
filtered_deployments = {}
for f in filtered_files:
    if f in deployment_data:
        filtered_deployments[f] = deployment_data[f]

# Final output
print("\n== Final Deployment Mapping (Filtered) ==")
print(json.dumps(filtered_deployments, indent=2))
