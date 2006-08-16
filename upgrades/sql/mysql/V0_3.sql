ALTER TABLE preference ADD COLUMN email_limit INT UNSIGNED NOT NULL DEFAULT 0;
ALTER TABLE preference ADD COLUMN email_sent INT UNSIGNED NOT NULL DEFAULT 0;
ALTER TABLE preference ADD COLUMN email_sent_timestamp DATETIME;

ALTER TABLE developer ADD COLUMN guest BOOL NOT NULL DEFAULT 0;

ALTER TABLE smoke_report ADD COLUMN failed BOOLEAN NOT NULL DEFAULT 0;
UPDATE smoke_report SET failed = ( fail > 1);
