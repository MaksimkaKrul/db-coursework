from dao.base_dao import BaseDAO
from beans.user import User
import mysql.connector

class UserDAO(BaseDAO):
    def create(self, user):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_user = "INSERT INTO User (username, email, password, roleId, status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(add_user, (user.username, user.email, user.password, user.roleId, user.status))
            cnx.commit()
            user.id = cursor.lastrowid
            return user
        except mysql.connector.Error as err:
            print(f"Error creating user: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, user_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
            row = cursor.fetchone()
            if row:
                return User(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting user by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_email(self, email):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
            row = cursor.fetchone()
            if row:
                return User(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting user by email: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()