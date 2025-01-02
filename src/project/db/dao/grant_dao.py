from dao.base_dao import BaseDAO
from beans.grant import Grant
from datetime import datetime
import mysql.connector

class GrantDAO(BaseDAO):
    def create(self, grant):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_grant = "INSERT INTO Grant (projectId, userId) VALUES (%s, %s)"
            cursor.execute(add_grant, (grant.projectId, grant.userId))
            cnx.commit()
            grant.id = cursor.lastrowid
            return grant
        except mysql.connector.Error as err:
            print(f"Error creating grant: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, grant_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Grant WHERE id = %s", (grant_id,))
            row = cursor.fetchone()
            if row:
                return Grant(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting grant by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()