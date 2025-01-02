class Grant:
    def __init__(self, id=None, projectId=None, userId=None, createdAt=None):
        self.id = id
        self.projectId = projectId
        self.userId = userId
        self.createdAt = createdAt

    def __repr__(self):
        return f"Grant(id={self.id}, projectId={self.projectId}, userId={self.userId}, createdAt={self.createdAt})"