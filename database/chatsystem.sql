/***********************************************
     Authors : Emmanuel COLLIN, Théo PAILLIER
************************************************/

-- sqlite3 chatsystem.db
-- .read chatsystem.sql

-- commandes de destruction des tables
DROP TABLE IF EXISTS User;             -- Table de utilisateurs
DROP TABLE IF EXISTS Room;             -- Table des salles de discussion
DROP TABLE IF EXISTS Room_User_Table;  -- Table des accès accordées aux utilisateurs
DROP TABLE IF EXISTS Message;          -- Tables contenant les messages (historique)

-- commandes de création des tables
CREATE TABLE User (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, username TEXT, password TEXT, adminStatus INTEGER);

CREATE TABLE Room (id INTEGER PRIMARY KEY AUTOINCREMENT, roomName TEXT);

CREATE TABLE Room_User_Table (idRoom INTEGER, idUser INTEGER);

CREATE TABLE Message (sendingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, idRoom INTEGER, idUser INTEGER, content TEXT);

-- Insertion de données
INSERT INTO User (firstName, lastName, username, password, adminStatus) VALUES ("Admin","Admin","admin","test_admin", 1);
INSERT INTO User (firstName, lastName, username, password, adminStatus) VALUES ("Enzo","Calvino","enzo_log","test_enzo", 0);
INSERT INTO User (firstName, lastName, username, password, adminStatus) VALUES ("Aziz","Idomar","aziz_log","test_aziz", 0);
INSERT INTO User (firstName, lastName, username, password, adminStatus) VALUES ("Theo","Paillier","theo_log","test_theo", 0);
INSERT INTO User (firstName, lastName, username, password, adminStatus) VALUES ("Emmanuel","Collin","emmanuel_log","test_emmanuel", 0);

INSERT INTO Room (roomName) VALUES ("Emergency meeting");
INSERT INTO Room (roomName) VALUES ("Daily news");
INSERT INTO Room (roomName) VALUES ("Weekly report");

INSERT INTO Room_User_Table (idRoom,idUser) VALUES (1,1);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (1,2);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (2,1);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (2,2);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (2,3);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (2,4);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (2,5);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (2,6);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (3,1);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (3,2);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (3,3);
INSERT INTO Room_User_Table (idRoom,idUser) VALUES (3,4);

INSERT INTO Message (idRoom,idUser,content) VALUES (1,1,"Philippe, you must call the IT department");
INSERT INTO Message (idRoom,idUser,content) VALUES (2,4,"We should focus on TDD dev right now !");
INSERT INTO Message (idRoom,idUser,content) VALUES (3,2,"In addition to that, sells are skyrocketing");
