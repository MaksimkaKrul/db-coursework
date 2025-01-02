class User:
    def __init__(self, id=None, username=None, email=None, password=None, roleId=None, status='ACTIVE', createdAt=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.roleId = roleId
        self.status = status
        self.createdAt = createdAt

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', roleId={self.roleId}, status='{self.status}', createdAt={self.createdAt})"