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
CREATE TABLE User (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, username TEXT, password TEXT, adminStatus BOOLEAN);

CREATE TABLE Room (id INTEGER PRIMARY KEY AUTOINCREMENT, roomName TEXT);

CREATE TABLE Room_User_Table (idRoom INTEGER, idUser INTEGER);

CREATE TABLE Message (sendingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, idRoom INTEGER, idUser INTEGER, content TEXT);

-- Insertion de données
INSERT INTO User (firstName, lastName, username, password) VALUES ("Admin","Admin","admin","test_admin");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Enzo","Calvino","enzo_log","test_enzo");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Aziz","Idomar","aziz_log","test_aziz");
INSERT INTO User (firstName, lastName, username, password) VALUES ("John","Doe","Dr.JD","0000AAAA");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Jane","Doe","MsJD","1234AzEr");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Philippe","Durand","Durandil","Df1598Rl");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Karine","Tour","Kami","659DB8g7");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Theo","Porose","Ostheoporose","147F258F");
INSERT INTO User (firstName, lastName, username, password) VALUES ("Emma","Misamal","MissEmma","jhLO7649");

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
