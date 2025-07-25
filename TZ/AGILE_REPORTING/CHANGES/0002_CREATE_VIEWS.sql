--liquibase formatted sql

--changeset DEMO:student_invalid_role
use database DEV_RZ;
use schema AGILE_REPORTING;
use role NON_EXISTENT_ROLE;  -- ❌ Will fail if the role does not exist or Liquibase user has no permission to switch

CREATE TABLE IF NOT EXISTS student_broken(
    id NUMBER PRIMARY KEY,
    name STRING
);