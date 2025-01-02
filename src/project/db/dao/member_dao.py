from dao.base_dao import BaseDAO
from beans.member import Member
import mysql.connector

class MemberDAO(BaseDAO):
    def create(self, member):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_member = "INSERT INTO Member (userId, teamId, teamRole) VALUES (%s, %s, %s)"
            cursor.execute(add_member, (member.userId, member.teamId, member.teamRole))
            cnx.commit()
            member.id = cursor.lastrowid
            return member
        except mysql.connector.Error as err:
            print(f"Error creating member: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, member_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Member WHERE id = %s", (member_id,))
            row = cursor.fetchone()
            if row:
                return Member(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting member by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()