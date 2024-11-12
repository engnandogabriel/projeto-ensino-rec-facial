from models.Aluno import Aluno
from services.FacesService import FacesService
from services.AlunoService import AlunoService
# # Corrigido: vírgula adicionada entre os argumentos
aluno = Aluno(
    "acde070d-8c4c-4f0d-9d8a-162843c10333",
    "Nando Gabriel",
    "628.031.203-80",
    "Engenharia de Computação 2022",
    "20221ENG.SIN0003",
    "/home/nando/Desktop/reconhecimento-facial/20221ENG.SIN0003.jpg",
    "2024-11-07 14:08:35.073003",
    "2024-11-07 14:08:35.073015"
)

# Instanciando o serviço
service = FacesService(aluno)

#  Chamando o método para criar o usuário e armazenar face
service.storeFaces(aluno.user_id)
alunoService = AlunoService()
alunoService.createAluno(aluno)

re = alunoService.getAlunos()
# print(re[1].name)

res = alunoService.getAlunoById("550e8400-e29b-41d4-a716-446655440000")
print(res)

# import numpy as np

# def remove_primeiro_elemento_faces(npz_file_path):
#     try:
#         # Carregar o arquivo .npz
#         data = np.load(npz_file_path, allow_pickle=True)
        
#         # Verificar se o arquivo contém dados
#         if not data.files:
#             print("O arquivo .npz está vazio.")
#             return
        
#         # Carregar o dicionário de faces (onde as chaves são os user_id e os valores são as face matrices)
#         faces_dict = dict(data.items())
        
#         # Verificar se há pelo menos um item para remover
#         if len(faces_dict) > 0:
#             # Remover o primeiro par chave-valor
#             first_key = next(iter(faces_dict))  # Pega a primeira chave
#             faces_dict.pop(first_key)  # Remove o primeiro item

#             # Re-salvar o arquivo .npz sem o primeiro elemento
#             np.savez(npz_file_path, **faces_dict)
#             print(f"Primeiro elemento removido e arquivo atualizado com {len(faces_dict)} faces.")
#         else:
#             print("Não há elementos para remover.")
    
#     except Exception as e:
#         print(f"Ocorreu um erro ao processar o arquivo .npz: {e}")

# # Exemplo de uso
# remove_primeiro_elemento_faces("data/backup/faces.npz")
