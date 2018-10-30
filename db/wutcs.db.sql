BEGIN TRANSACTION;
DROP TABLE IF EXISTS `news`;
CREATE TABLE IF NOT EXISTS `news` (
	`title`	TEXT,
	`date`	TEXT,
	`content`	TEXT,
	`link`	TEXT UNIQUE,
	PRIMARY KEY(`link`)
);
DROP TABLE IF EXISTS `act`;
CREATE TABLE IF NOT EXISTS `act` (
	`title`	TEXT,
	`date`	TEXT,
	`content`	TEXT,
	`index`	TEXT UNIQUE,
	PRIMARY KEY(`index`)
);
COMMIT;
