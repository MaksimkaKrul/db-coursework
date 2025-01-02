class Member:
    def __init__(self, id=None, userId=None, teamId=None, teamRole='Developer', joinedAt=None):
        self.id = id
        self.userId = userId
        self.teamId = teamId
        self.teamRole = teamRole
        self.joinedAt = joinedAt

    def __repr__(self):
        return f"Member(id={self.id}, userId={self.userId}, teamId={self.teamId}, teamRole='{self.teamRole}', joinedAt={self.joinedAt})"