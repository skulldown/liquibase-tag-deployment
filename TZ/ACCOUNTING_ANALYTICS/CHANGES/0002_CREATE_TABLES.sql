--liquibase formatted sql

--changeset 12:Student_21

use database DEV_TZ;
use schema ACCOUNTING_ANALYTICS;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;

CREATE  DEV_TZ.ACCOUNTING_ANALYTICS.Student_20(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);



CREATE  DEV_TZ.ACCOUNTING_ANALYTICS.Student_21(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);