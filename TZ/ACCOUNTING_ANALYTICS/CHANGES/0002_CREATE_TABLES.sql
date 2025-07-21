--liquibase formatted sql

--changeset 12:empp38

use database DEV_TZ;
use schema ACCOUNTING_ANALYTICS;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;

CREATE TABLE IF NOT EXISTS DEV_TZ.ACCOUNTING_ANALYTICS.empp38(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);


