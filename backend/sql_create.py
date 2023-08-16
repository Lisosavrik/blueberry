import sqlite3

db = sqlite3.connect("blueberry.db")

c = db.cursor()

c.execute("""
        CREATE TABLE Users (
                user_id varchar(255) PRIMARY KEY,
                name varchar(255),
                log_in varchar(255),
                password varchar(255)
        );
""");

c.execute("""
        CREATE TABLE Workspaces (
                workspace_id varchar(255) PRIMARY KEY,
                name varchar(255),
                user_id varchar(255) NOT NULL,
                CONSTRAINT user_fk
                FOREIGN KEY (user_id)
                REFERENCES Users(user_id) ON DELETE CASCADE
        );
""");

c.execute("""
        CREATE TABLE Tables (
                table_id varchar(255) PRIMARY KEY,
                name varchar(255),
                workspace_id varchar(255) NOT NULL,
                CONSTRAINT workspace_fk
                FOREIGN KEY (workspace_id)
                REFERENCES Workspaces(workspace_id) ON DELETE CASCADE
        );
""");

c.execute("""
        CREATE TABLE Cards (
                card_id varchar(255) PRIMARY KEY,
                key text,
                value text,
                training_date varchar(255),
                color varchar(255),
                next_well INTEGER,
                next_very_well INTEGER,
                table_id varchar(255) NOT NULL,
                CONSTRAINT table_fk
                FOREIGN KEY (table_id)
                REFERENCES Tables(table_id) ON DELETE CASCADE
        );
""");



if __name__ == "__main__":
        db.commit()

db.close()
