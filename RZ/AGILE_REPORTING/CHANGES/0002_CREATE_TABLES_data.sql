--liquibase formatted sql

--changeset DEMO:student_158435438111
use database DEV_RZ;
use schema AGILE_REPORTING;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;



CREATE TABLE IF NOT EXISTS DEV_RZ.AGILE_REPORTING.student_1175475411(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);










