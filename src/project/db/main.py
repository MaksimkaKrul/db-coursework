# main.py
from config import db_config
from beans.role import Role
from beans.user import User
from beans.project import Project
from beans.team import Team
from beans.member import Member
from beans.task import Task
from beans.artefact import Artefact
from beans.grant import Grant
from dao.role_dao import RoleDAO
from dao.user_dao import UserDAO
from dao.project_dao import ProjectDAO
from dao.team_dao import TeamDAO
from dao.member_dao import MemberDAO
from dao.task_dao import TaskDAO
from dao.artefact_dao import ArtefactDAO
from dao.grant_dao import GrantDAO
from datetime import datetime

def main():
    role_dao = RoleDAO(db_config)
    user_dao = UserDAO(db_config)
    project_dao = ProjectDAO(db_config)
    team_dao = TeamDAO(db_config)
    member_dao = MemberDAO(db_config)
    task_dao = TaskDAO(db_config)
    artefact_dao = ArtefactDAO(db_config)
    grant_dao = GrantDAO(db_config)

    # Create some objects
    admin_role_name = 'Admin'
    admin_role = role_dao.get_by_name(admin_role_name)
    if not admin_role:
        admin_role = Role(name=admin_role_name)
        admin_role = role_dao.create(admin_role)
        print(f"Created Role: {admin_role}")
    else:
        print(f"Role '{admin_role_name}' already exists: {admin_role}")

    new_user = User(username='test_user', email='test@example.com', password='testpass', roleId=admin_role.id)
    new_user = user_dao.create(new_user)
    print(f"Created User: {new_user}")

    new_team = Team()
    new_team = team_dao.create(new_team)
    print(f"Created Team: {new_team}")

    new_project = Project(name='Test Project', description='A test project', ownerId=new_user.id, teamId=new_team.id)
    new_project = project_dao.create(new_project)
    print(f"Created Project: {new_project}")

    new_member = Member(userId=new_user.id, teamId=new_team.id, teamRole='Developer')
    new_member = member_dao.create(new_member)
    print(f"Created Member: {new_member}")

    due_date = datetime(2024, 12, 31, 12, 0, 0)
    new_task = Task(title='Test Task', projectId=new_project.id, dueDate=due_date)
    new_task = task_dao.create(new_task)
    print(f"Created Task: {new_task}")

    new_artefact = Artefact(title='Test Artefact', filePath='/tmp/test.txt', fileType='TXT', uploadedBy=new_user.id, projectId=new_project.id)
    new_artefact = artefact_dao.create(new_artefact)
    print(f"Created Artefact: {new_artefact}")

    new_grant = Grant(projectId=new_project.id, userId=new_user.id)
    new_grant = grant_dao.create(new_grant)
    print(f"Created Grant: {new_grant}")

    # Search for existing objects
    found_user = user_dao.get_by_email('test@example.com')
    print(f"\nFound User by Email: {found_user}")

    found_project = project_dao.get_by_name('Test Project')
    print(f"Found Project by Name: {found_project}")

if __name__ == "__main__":
    main()