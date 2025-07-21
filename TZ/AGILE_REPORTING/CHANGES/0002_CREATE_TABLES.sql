--liquibase formatted sql

--changeset DEMO:0010-empp382dsgh
use database DEV_TZ;
use schema AGILE_REPORTING;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;



CREATE TABLE IF NOT EXISTS DEV_TZ.AGILE_REPORTING.empp382dsgh(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);


