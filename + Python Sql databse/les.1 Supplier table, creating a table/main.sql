CREATE TABLE supplier2(
    SNO TEXT PRIMARY KEY, 
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT);

INSERT INTO supplier2 (SNO, SNAME, STATUS, CITY) VALUES 
   ('S1','Smith', 20, 'London'),
   ('S2', 'Jones', 10, 'Paris'),
   ('S3','Jones', 20,'London'),
   ('S4', 'Adams', 30, 'Athens'),
   ('S5', 'Clarke', 30, 'Athens');


SELECT * FROM supplier2;