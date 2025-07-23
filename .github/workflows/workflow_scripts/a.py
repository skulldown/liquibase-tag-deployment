import sys

# Ensure we have both arguments
if len(sys.argv) < 3:
    print("Usage: a.py <CHANGED_FILES> <NEWER_TAG>")
    sys.exit(1)

changed_files_raw = sys.argv[1]
newer_tag = sys.argv[2]

print("== Received Parameters ==")
print(f"CHANGED_FILES: {changed_files_raw}")
print(f"Type of CHANGED_FILES: {type(changed_files_raw)}")

print(f"NEWER_TAG: {newer_tag}")
print(f"Type of NEWER_TAG: {type(newer_tag)}")

# Split the changed files using the | delimiter
changed_files_list = changed_files_raw.split('|')

# List of allowed top-level folders
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
    if not file_path.strip():
        continue
    first_folder = file_path.strip().split('/')[0]
    if first_folder.upper() in allowed_folders:
        filtered_files.append(file_path)

# Print filtered results
print("\nFiltered Changed Files:")
for f in filtered_files:
    print(f"- {f}")
