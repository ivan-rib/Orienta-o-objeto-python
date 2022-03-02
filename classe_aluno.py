from modules.classe_pessoa import pessoa

class aluno(pessoa):
    
    def __init__(self, nome = "", rg = "", contato = "", endereco = "", matricula = ""):
        try:
            self.matricula = matricula
            super(). __init__(nome, rg, contato, endereco)
        except Exception as e:
            print(str(e))
        
    def get_aluno(self, matricula):
        try:
            self.matricula = matricula
            return print("\n Aluno matriculado:", matricula)                        
                
        except Exception as e:
            print(str(e))    
    
    def set_aluno(self, matricula):        
        self.matricula = matricula
        