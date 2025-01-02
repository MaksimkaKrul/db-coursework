class Task:
    def __init__(self, id=None, title=None, description=None, assignedTo=None, projectId=None, status='PENDING', priority='MEDIUM', dueDate=None, createdAt=None):
        self.id = id
        self.title = title
        self.description = description
        self.assignedTo = assignedTo
        self.projectId = projectId
        self.status = status
        self.priority = priority
        self.dueDate = dueDate
        self.createdAt = createdAt

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', projectId={self.projectId}, status='{self.status}', priority='{self.priority}', dueDate={self.dueDate}, createdAt={self.createdAt})"
