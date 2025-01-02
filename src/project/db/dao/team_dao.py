from dao.base_dao import BaseDAO
from beans.team import Team
import mysql.connector

class TeamDAO(BaseDAO):
    def create(self, team):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_team = "INSERT INTO Team () VALUES ()"
            cursor.execute(add_team)
            cnx.commit()
            team.id = cursor.lastrowid
            return team
        except mysql.connector.Error as err:
            print(f"Error creating team: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, team_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Team WHERE id = %s", (team_id,))
            row = cursor.fetchone()
            if row:
                return Team(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting team by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()