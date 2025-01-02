class Artefact:
    def __init__(self, id=None, title=None, description=None, filePath=None, fileType=None, uploadedBy=None, projectId=None, createdAt=None):
        self.id = id
        self.title = title
        self.description = description
        self.filePath = filePath
        self.fileType = fileType
        self.uploadedBy = uploadedBy
        self.projectId = projectId
        self.createdAt = createdAt

    def __repr__(self):
        return f"Artefact(id={self.id}, title='{self.title}', projectId={self.projectId}, fileType='{self.fileType}', uploadedBy={self.uploadedBy}, createdAt={self.createdAt})"
