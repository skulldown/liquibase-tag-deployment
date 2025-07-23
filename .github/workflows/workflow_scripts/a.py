import sys
import json
import snowflake.connector
import os

# Set of allowed folders
ALLOWED_FOLDERS = {
    "QUALITY", "AUDIT", "RZ", "RCZ", "TZ", "CZ",
    "SECURITY", "MULESOFT", "DATA_SHARE", "WORK_FLOW_TEST"
}

def parse_and_filter_inputs(changed_files_raw, newer_tag, deployment_json_raw, env):
    """Parse CLI inputs, filter changed files, and enrich deployment data with database/schema."""
    print("\n== Received Parameters ==")
    print(f"Changed Files: {changed_files_raw}")
    print(f"Latest Release Tag: {newer_tag}")
    print(f"Liquibase Deployment JSON: {deployment_json_raw}\n")

    # Step 1: Filter changed files
    changed_files = changed_files_raw.split('|')
    filtered_files = []
    for path in changed_files:
        path = path.strip()
        if not path:
            continue
        first_folder = path.split('/')[0].upper()
        if first_folder in ALLOWED_FOLDERS:
            filtered_files.append(path)

    print("== Changed Files Between Previous and Current Release ==")
    for f in filtered_files:
        print(f"- {f}")

    # Step 2: Parse and enrich deployment data
    try:
        deployment_data = json.loads(deployment_json_raw)
    except json.JSONDecodeError as e:
        print(f"\n❌ Failed to parse deployment JSON: {e}")
        sys.exit(1)

    print("\n== Enriched Deployment Data with Database and Schema ==")
    enriched_data = {}

    for key, deployments in deployment_data.items():
        parts = key.split('/')
        if len(parts) < 3:
            print(f"⚠️ Skipping invalid key: {key}")
            continue

        database = f"{env}_{parts[1]}"
        schema = parts[2]

        enriched_list = []
        for item in deployments:
            item["database"] = database
            item["schema"] = schema
            enriched_list.append(item)

        enriched_data[key] = enriched_list

    print(json.dumps(enriched_data, indent=2))
    print("\n✅ Done: Enriched deployment entries are ready for use.")

    return enriched_data, filtered_files


def validate_deployment_scope_against_changed_files(enriched_data, filtered_files):
    """
    Validate that each changed file is listed in deployment data and has a deploymentId.
    Returns a list of valid matched deployment records.
    """
    deployment_lookup = {}

    # Build deployment lookup: RZ/SCHEMA -> deployments
    for full_key, deployments in enriched_data.items():
        if full_key.startswith("liquibase-tag-deployment/"):
            trimmed_key = full_key.replace("liquibase-tag-deployment/", "")
            deployment_lookup[trimmed_key] = deployments

    matched_results = []

    for path in filtered_files:
        parts = path.split('/')
        if len(parts) < 3:
            continue  # Invalid file path

        dir_key = '/'.join(parts[:2])       # e.g., RZ/AGILE_REPORTING
        relative_file = '/'.join(parts[2:]) # e.g., CHANGES/0002_CREATE_TABLES.sql

        deployments = deployment_lookup.get(dir_key, [])
        for record in deployments:
            if record["file"] == relative_file and record.get("deploymentId"):
                matched_results.append(record)
                break

    return matched_results


def get_snowflake_connection():
    """
    Establish a Snowflake connection using environment variables with default fallbacks.
    """
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER", "yogeshmakwana"),
        password=os.getenv("SNOWFLAKE_PASSWORD", "myz3YHnLdqbx8YW"),
        account=os.getenv("SNOWFLAKE_ACCOUNT", "HFEHAXR-WI86289"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        role=os.getenv("SNOWFLAKE_ROLE", "FULL_ACCESS_ROLE")
    )
    return conn


def update_changelog(conn, config, tag):
    """
    Update DATABASECHANGELOG where DEPLOYMENT_ID matches.
    Set TAG value.
    """
    try:
        for item in config:
            database = item['database']
            schema = item['schema']
            deployment_id = item['deploymentId']

            cursor = conn.cursor()
            cursor.execute(f"USE DATABASE {database}")
            cursor.execute(f"USE SCHEMA {schema}")

            print(f"\n🔄 Updating DATABASECHANGELOG in {database}.{schema}...")

            update_sql = """
                UPDATE DATABASECHANGELOG
                SET TAG = %s
                WHERE DEPLOYMENT_ID = %s
            """
            print(f"📄 Executing SQL: {update_sql.strip()}")
            print(f"📌 Params: TAG = '{tag}', DEPLOYMENT_ID = '{deployment_id}'")

            cursor.execute(update_sql, (tag, deployment_id))
            print(f"✅ Update complete. DEPLOYMENT_ID='{deployment_id}', TAG='{tag}'")

            cursor.close()
    except Exception as e:
        print(f"❌ Error while updating changelog: {e}")



if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python a.py <CHANGED_FILES> <NEWER_TAG> <DEPLOYMENT_JSON> [ENV]")
        sys.exit(1)

    changed_files_raw = sys.argv[1]
    newer_tag = sys.argv[2]
    deployment_json_raw = sys.argv[3]
    env = sys.argv[4] if len(sys.argv) > 4 else "dev"

    enriched_data, filtered_files = parse_and_filter_inputs(
        changed_files_raw,
        newer_tag,
        deployment_json_raw,
        env
    )

    extract_latest_file_deployment_results = validate_deployment_scope_against_changed_files(
        enriched_data,
        filtered_files
    )

    print(json.dumps(extract_latest_file_deployment_results, indent=2))

    conn = get_snowflake_connection()
    update_changelog(conn, extract_latest_file_deployment_results, newer_tag)
    conn.close()
