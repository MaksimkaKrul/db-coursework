from dao.base_dao import BaseDAO
from beans.project import Project
from datetime import datetime
import mysql.connector

class ProjectDAO(BaseDAO):
    def create(self, project):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_project = "INSERT INTO Project (name, description, ownerId, teamId) VALUES (%s, %s, %s, %s)"
            cursor.execute(add_project, (project.name, project.description, project.ownerId, project.teamId))
            cnx.commit()
            project.id = cursor.lastrowid
            return project
        except mysql.connector.Error as err:
            print(f"Error creating project: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, project_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Project WHERE id = %s", (project_id,))
            row = cursor.fetchone()
            if row:
                return Project(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting project by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_name(self, name):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Project WHERE name = %s", (name,))
            row = cursor.fetchone()
            if row:
                return Project(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting project by name: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()