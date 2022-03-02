from modules.classe_aluno import aluno

class aluno_matematica(aluno):
    
    def __init__(self, nome = "", rg = "", contato = "", endereco = "", matricula = "", nota_matematica =""):
        
        try:
            self.nota_matematica = nota_matematica
            super(). __init__(nome, rg, contato, endereco, matricula)
        except Exception as e:
            print(str(e)) 
        
    def get_aluno_matematica(self, nota_matematica):
        try:
            self.nnota_matematica = nota_matematica
            return print("\n Nota do aluno em matematica: ", nota_matematica)                        
                
        except Exception as e:
            print(str(e))    
    
    def set_aluno_matematica(self, nota_matematica): 
        self.nota_matematica = nota_matematica