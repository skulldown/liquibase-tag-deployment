--liquibase formatted sql

--changeset 12:teacher_11empp1234567845454

use database DEV_RZ;
use schema ACCOUNTING_ANALYTICS;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;

CREATE TABLE IF NOT EXISTS DEV_TZ.ACCOUNTING_ANALYTICS.teacher112(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS DEV_TZ.ACCOUNTING_ANALYTICS.teacher100012sdsd(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS DEV_TZ.ACCOUNTING_ANALYTICS.student_12(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS DEV_TZ.ACCOUNTING_ANALYTICS.emmp12(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);
