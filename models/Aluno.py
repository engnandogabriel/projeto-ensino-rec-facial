class Aluno:
    def __init__(self, user_id, name, document, course, registration_code, photo, created_at, updated_at):
        self.user_id = user_id
        self.name = name
        self.document = document
        self.course = course
        self.registration_code = registration_code
        self.photo = photo
        self.created_at = created_at
        self.updated_at = updated_at

    def verificaPresenca(self):
        tamanhoFrequencia = len(self.frequencia)
        # 2023-03-02T14:01:17.402+00:00
        if len(self.frequencia) != 0:
            ultimaFrequenica = self.frequencia[tamanhoFrequencia - 1]
            ultimaFrequenica = ultimaFrequenica.split("T")[0]
        else:
            ultimaFrequenica = "0000-00-00"

        if tamanhoFrequencia == 0:
            print("Cadastro de frequencia nescessário")
            self.controleFrequencia = 0
            return 0

        elif self.atualizedAt == self.dados.get_data():
            print("Cadastro de frequência ja realizado")
            self.controleFrequencia = 1
            return 1

        elif ultimaFrequenica == self.dados.get_data():
            print("Cadastro de frequência ja realizado")
            self.controleFrequencia = 1
            return 1
        else:
            print("Cadastro nescessário")
            self.controleFrequencia = 0
            return 0

