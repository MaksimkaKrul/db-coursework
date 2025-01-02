class Team:
    def __init__(self, id=None, createdAt=None):
        self.id = id
        self.createdAt = createdAt

    def __repr__(self):
        return f"Team(id={self.id}, createdAt={self.createdAt})"