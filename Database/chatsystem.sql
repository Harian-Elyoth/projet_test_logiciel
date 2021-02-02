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
INSERT INTO User (firstName, lastName, username, password) VALUES
     ("John","Doe","Dr.JD","0000AAAA"),
     ("Jane","Doe","MsJD","1234AzEr"),
     ("Philippe","Durand","Durandil","Df1598Rl"),
     ("Karine","Tour","Kami","659DB8g7")
     ("Theo","Porose","Ostheoporose","147F258F"),
     ("Emma","Misamal","MissEmma","jhLO7649");

INSERT INTO Room (roomName) VALUES
     ("Emergency meeting"),
     ("Daily news"),
     ("Weekly report");

INSERT INTO Room_User_Table (idRoom,idUser) VALUES
     (1,1),
     (1,2),
     (2,1),
     (2,2),
     (2,3),
     (2,4),
     (2,5),
     (2,6),
     (3,1),
     (3,2),
     (3,3),
     (3,4);

INSERT INTO Message (idRoom,idUser,content) VALUES
     (1,1,"Philippe, you must call the IT department"),
     (2,4,"We should focus on TDD dev right now !"),
     (3,2,"In addition to that, sells are skyrocketing");
