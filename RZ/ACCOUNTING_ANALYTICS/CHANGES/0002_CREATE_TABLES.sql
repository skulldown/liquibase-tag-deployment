--liquibase formatted sql

--changeset 12:empp382dsstudent_119911gh

use database DEV_RZ;
use schema ACCOUNTING_ANALYTICS;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;

CREATE TABLE IF NOT EXISTS DEV_RZ.ACCOUNTING_ANALYTICS.student_119911(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

