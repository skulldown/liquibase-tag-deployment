--liquibase formatted sql

--changeset DEMO:Student_21
use database DEV_TZ;
use schema AGILE_REPORTING;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;



CREATE TABLE IF NOT EXISTS DEV_TZ.AGILE_REPORTING.Student_113(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);


