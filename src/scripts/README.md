# Реалізація доступу до бази даних

PS D:\asdasdas\DB> python -u "d:\asdasdas\DB\project\db\main.py"
Role 'Admin' already exists: Role(id=1, name='Admin')
Created User: User(id=5, username='test_user', email='test@example.com', roleId=1, status='ACTIVE', createdAt=None)
Created Team: Team(id=5, createdAt=None)
Created Project: Project(id=4, name='Test Project', ownerId=5, teamId=5, createdAt=None)
Created Member: Member(id=5, userId=5, teamId=5, teamRole='Developer', joinedAt=None)
Created Task: Task(id=5, title='Test Task', projectId=4, status='PENDING', priority='MEDIUM', dueDate=2024-12-31 12:00:00, createdAt=None)
Created Artefact: Artefact(id=4, title='Test Artefact', projectId=4, fileType='TXT', uploadedBy=5, createdAt=None)
Found User by Email: User(id=5, username='test_user', email='test@example.com', roleId=1, status='ACTIVE', createdAt=2024-12-30 23:25:08)
Found Project by Name: Project(id=4, name='Test Project', ownerId=5, teamId=5, createdAt=2024-12-30 23:25:08)

# Зображення результату
![chrome_Os2RMbnJrA](https://github.com/user-attachments/assets/69c90c6f-8309-4fc5-9ea3-3303c7cf2e36)

