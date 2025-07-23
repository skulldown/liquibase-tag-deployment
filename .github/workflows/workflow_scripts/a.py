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

# Optional: Split changed files into a list
changed_files_list = changed_files_raw.split('|')
print("\nParsed CHANGED_FILES as list:")
for file in changed_files_list:
    print(f"- {file}")
