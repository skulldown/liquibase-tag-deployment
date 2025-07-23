import sys
import json
import os
import snowflake.connector




# === Main Script ===
if len(sys.argv) < 4:
    print("Usage: a.py <CHANGED_FILES> <NEWER_TAG> <DEPLOYMENT_JSON>")
    sys.exit(1)

changed_files_raw = sys.argv[1]
newer_tag = sys.argv[2]
deployment_json_raw = sys.argv[3]

# print("== Received Parameters ==")
# print(f"CHANGED_FILES: {changed_files_raw}")
# print(f"NEWER_TAG: {newer_tag}")
# print(f"DEPLOYMENT_JSON: {deployment_json_raw}\n")

# changed_files_list = changed_files_raw.split('|')

# allowed_folders = {
#     "QUALITY", "AUDIT", "RZ", "RCZ", "TZ", "CZ", 
#     "SECURITY", "MULESOFT", "DATA_SHARE", "WORK_FLOW_TEST"
# }

# filtered_files = []
# for file_path in changed_files_list:
#     file_path = file_path.strip()
#     if not file_path:
#         continue
#     first_folder = file_path.split('/')[0].upper()
#     if first_folder in allowed_folders:
#         filtered_files.append(file_path)

# print("== Filtered Changed Files ==")
# for f in filtered_files:
#     print(f"- {f}")

# try:
#     deployment_data = json.loads(deployment_json_raw)
# except json.JSONDecodeError as e:
#     print(f"\n❌ Failed to parse DEPLOYMENT_JSON: {e}")
#     sys.exit(1)

# filtered_deployments = {}
# for f in filtered_files:
#     if f in deployment_data:
#         filtered_deployments[f] = deployment_data[f]

# print("\n== Final Deployment Mapping (Filtered) ==")
# print(json.dumps(filtered_deployments, indent=2))


# def get_snowflake_connection():
#     """
#     Establish a Snowflake connection using environment variables with default fallbacks.
#     """
#     conn = snowflake.connector.connect(
#         user=os.getenv("SNOWFLAKE_USER", "yogeshmakwana"),
#         password=os.getenv("SNOWFLAKE_PASSWORD", "myz3YHnLdqbx8YW"),
#         account=os.getenv("SNOWFLAKE_ACCOUNT", "HFEHAXR-WI86289"),
#         warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
#         role=os.getenv("SNOWFLAKE_ROLE", "FULL_ACCESS_ROLE")  # Optional: Add default role
#     )
#     return conn


# def update_changelog(conn, database, schema, deployment_id, tag):
#     """
#     Update DATABASECHANGELOG where DEPLOYMENT_ID matches.
#     Set TAG value.
#     """
#     try:
#         cursor = conn.cursor()
#         cursor.execute(f"USE DATABASE {database}")
#         cursor.execute(f"USE SCHEMA {schema}")

#         print(f"\n🔄 Updating DATABASECHANGELOG in {database}.{schema}...")

#         update_sql = """
#             UPDATE DATABASECHANGELOG
#             SET TAG = %s
#             WHERE DEPLOYMENT_ID = %s
#         """
#         print(f"📄 Executing SQL: {update_sql.strip()}")
#         print(f"📌 Params: TAG = '{tag}', DEPLOYMENT_ID = '{deployment_id}'")

#         cursor.execute(update_sql, (tag, deployment_id))
#         print(f"✅ Update complete. DEPLOYMENT_ID='{deployment_id}', TAG='{tag}'")

#         cursor.close()
#     except Exception as e:
#         print(f"❌ Error while updating changelog: {e}")


# conn = get_snowflake_connection()
# update_changelog(conn, database, schema, deployment_id, tag)
# conn.close()