import mysql.connector
from dao.base_dao import BaseDAO
from beans.artefact import Artefact
from datetime import datetime

class ArtefactDAO(BaseDAO):
    def create(self, artefact):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_artefact = "INSERT INTO Artefact (title, description, filePath, fileType, uploadedBy, projectId) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(add_artefact, (artefact.title, artefact.description, artefact.filePath, artefact.fileType, artefact.uploadedBy, artefact.projectId))
            cnx.commit()
            artefact.id = cursor.lastrowid
            return artefact
        except mysql.connector.Error as err:
            print(f"Error creating artefact: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, artefact_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Artefact WHERE id = %s", (artefact_id,))
            row = cursor.fetchone()
            if row:
                return Artefact(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting artefact by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()