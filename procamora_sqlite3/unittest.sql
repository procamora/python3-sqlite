BEGIN TRANSACTION;
DROP TABLE IF EXISTS "table1";
CREATE TABLE IF NOT EXISTS "table1" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "value"	TEXT NOT NULL
);
DROP TABLE IF EXISTS "table2";
CREATE TABLE IF NOT EXISTS "table2" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "value2"	INTEGER NOT NULL
);
INSERT INTO "table1" VALUES (1,'Python');
INSERT INTO "table1" VALUES (2,'Java');
INSERT INTO "table1" VALUES (3,'C++');
INSERT INTO "table1" VALUES (4,'Bash');
INSERT INTO "table2" VALUES (1,2.7);
INSERT INTO "table2" VALUES (2,3.5);
INSERT INTO "table2" VALUES (3,3.6);
INSERT INTO "table2" VALUES (4,3.7);
INSERT INTO "table2" VALUES (5,3.8);
COMMIT;
