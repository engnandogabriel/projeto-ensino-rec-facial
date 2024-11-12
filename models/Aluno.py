import datetime
class Aluno:
    def __init__(self, user_id, name, document, course, registration_code, photo, created_at, updated_at):
        self.user_id = user_id
        self.name = name
        self.document = document
        self.course = course
        self.registration_code = registration_code
        self.photo = photo
        self.recognized = False
        self.recognition_time = None
        self.created_at = created_at
        self.updated_at = updated_at

    def recognation(self) -> None:
        self.recognation = True
        self.recognition_time = datetime.datetime

