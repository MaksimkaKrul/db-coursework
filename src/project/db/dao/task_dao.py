from dao.base_dao import BaseDAO
from beans.task import Task
from datetime import datetime
import mysql.connector

class TaskDAO(BaseDAO):
    def create(self, task):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor()
            add_task = "INSERT INTO Task (title, description, assignedTo, projectId, status, priority, dueDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(add_task, (task.title, task.description, task.assignedTo, task.projectId, task.status, task.priority, task.dueDate))
            cnx.commit()
            task.id = cursor.lastrowid
            return task
        except mysql.connector.Error as err:
            print(f"Error creating task: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()

    def get_by_id(self, task_id):
        try:
            cnx = self.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Task WHERE id = %s", (task_id,))
            row = cursor.fetchone()
            if row:
                return Task(**row)
            return None
        except mysql.connector.Error as err:
            print(f"Error getting task by ID: {err}")
            return None
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()