



CREATE TABLE   tv_view_players  (
 player  integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 first_name  varchar(30) NOT NULL,
 last_name  varchar(30) NOT NULL,
 contact_info  varchar(30) NOT NULL,
 way  integer NOT NULL,
 throw_count  integer NOT NULL,
 avarege_score  real NOT NULL,
 comand_id_id  integer NOT NULL REFERENCES  tv_view_command  ( command )
 );
CREATE TABLE   tv_view_game  (
game  integer NOT NULL PRIMARY KEY AUTOINCREMENT,
game_name  varchar(30) NOT NULL,
game_date  datetime NOT NULL
);
CREATE TABLE   tv_view_ligue  ( 
ligue  integer NOT NULL PRIMARY KEY AUTOINCREMENT,
ligue_name  varchar(30) NOT NULL,
club_id_id  integer NOT NULL REFERENCES  tv_view_clubmeta  ( club ) DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE   tv_view_command  (
command  integer NOT NULL PRIMARY KEY AUTOINCREMENT,
comand_name  varchar(50) NOT NULL,
score  real NOT NULL,
game_id_id  integer NOT NULL REFERENCES  tv_view_game  ( game ) DEFERRABLE INITIALLY DEFERRED,
lugue_id_id  integer NOT NULL REFERENCES  tv_view_ligue  ( ligue ) DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE   tv_view_clubmeta  (
club  integer NOT NULL PRIMARY KEY AUTOINCREMENT,
address  varchar(30) NOT NULL,
way_count  integer NOT NULL,
club_name  varchar(30) NOT NULL UNIQUE
);

