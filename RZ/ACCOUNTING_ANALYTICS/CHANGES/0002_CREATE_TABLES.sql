--liquibase formatted sql

--changeset 12:student9

use database DEV_RZ;
use schema ACCOUNTING_ANALYTICS;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;

CREATE TABLE IF NOT EXISTS DEV_RZ.ACCOUNTING_ANALYTICS.student_8(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);





-- CREATE TABLE IF NOT EXISTS DEV_RZ.ACCOUNTING_ANALYTICS.student_11948sd9112(
--     ID             NUMBER       PRIMARY KEY,
--     NAME           STRING       NOT NULL,
--     STATUS         STRING,
--     CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
-- );


--tag: liquibase-dev-deploy-123