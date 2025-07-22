--liquibase formatted sql

--changeset DEMO:0010-student_14 labels:${liquibase.label}

use database DEV_RZ;
use schema AGILE_REPORTING;
use role FULL_ACCESS_ROLE;
use warehouse SNOWFLAKE_LEARNING_WH;




CREATE TABLE IF NOT EXISTS DEV_RZ.AGILE_REPORTING.student_14(
    ID             NUMBER       PRIMARY KEY,
    NAME           STRING       NOT NULL,
    STATUS         STRING,
    CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);




-- CREATE TABLE IF NOT EXISTS DEV_RZ.AGILE_REPORTING.empp382asasdsgh(
--     ID             NUMBER       PRIMARY KEY,
--     NAME           STRING       NOT NULL,
--     STATUS         STRING,
--     CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
-- );


-- CREATE TABLE IF NOT EXISTS DEV_RZ.AGILE_REPORTING.empp382dsghasas(
--     ID             NUMBER       PRIMARY KEY,
--     NAME           STRING       NOT NULL,
--     STATUS         STRING,
--     CREATED_AT     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
-- );


