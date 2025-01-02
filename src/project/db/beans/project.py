from datetime import datetime

class Project:
    def __init__(self, id=None, name=None, description=None, ownerId=None, teamId=None, createdAt=None):
        self.id = id
        self.name = name
        self.description = description
        self.ownerId = ownerId
        self.teamId = teamId
        self.createdAt = createdAt

    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}', ownerId={self.ownerId}, teamId={self.teamId}, createdAt={self.createdAt})"