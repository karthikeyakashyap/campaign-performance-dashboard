-- Create the database
CREATE DATABASE campaigndb;

-- Switch to the new DB (you'll run this manually in psql)
\c campaigndb;

-- Create a table for campaign data
CREATE TABLE campaign_metrics (
    timestamp TIMESTAMP PRIMARY KEY,
    impressions INT,
    clicks INT,
    conversions INT,
    cost FLOAT
);
