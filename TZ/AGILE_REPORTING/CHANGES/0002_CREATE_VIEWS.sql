--liquibase formatted sql

--changeset DEMO:student_9
use database DEV_TZ;
use schema AGILE_REPORTING;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;


CREATE TABLE IF NOT EXISTS DEV_TZ.AGILE_REPORTING.student_9(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

