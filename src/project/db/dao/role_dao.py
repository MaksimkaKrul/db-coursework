from dao.base_dao import BaseDAO
from beans.role import Role
import mysql.connector

class RoleDAO(BaseDAO):
    def create(self, role):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_role = "INSERT INTO Role (name) VALUES (%s)"
            cursor.execute(add_role, (role.name,))
            cnx.commit()
            role.id = cursor.lastrowid
            return role
        except mysql.connector.Error as err:
            print(f"Error creating role: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, role_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Role WHERE id = %s", (role_id,))
            row = cursor.fetchone()
            if row:
                return Role(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting role by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_name(self, name):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Role WHERE name = %s", (name,))
            row = cursor.fetchone()
            if row:
                return Role(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting role by name: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()