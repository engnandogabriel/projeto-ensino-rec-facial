# from models.Aluno import Aluno
# from services.FacesService import FacesService
from services.AlunoService import AlunoService
# # Corrigido: vírgula adicionada entre os argumentos
# aluno = Aluno(
#     2,
#     "Fábio da Silva Eloi Jr",
#     "628.031.203-80",
#     "Engenharia de Computação 2022",
#     "20221ENG.SIN0004",
#     "/home/nando/Desktop/reconhecimento-facial/20221ENG.SIN0004.jpg",
#     "2024-11-07 14:08:35.073003",
#     "2024-11-07 14:08:35.073015"
# )

# # Instanciando o serviço
# service = FacesService(aluno)

# # Chamando o método para criar o usuário
# service.createUser()

alunoService = AlunoService()

re = alunoService.getAlunos()
print(re[1].name)

res = alunoService.getAlunoById(2)
print(res.name)