# snwoflake_add_tag_to_chagnelog.py

import sys

if len(sys.argv) < 2:
    print("No changed files provided.")
    sys.exit(1)

# Changed files string passed as: file1.sql|file2.sql|folder/file3.sql
changed_files_arg = sys.argv[1]
changed_files = changed_files_arg.split('|')

print("Changed files:")
for f in changed_files:
    print(f"Type of f: {type(f)} : {f}")
