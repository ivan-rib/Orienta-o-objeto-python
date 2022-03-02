from modules.classe_aluno import aluno

class aluno_portugues(aluno):
    
    
    def __init__(self, nome = "", rg = "", contato = "", endereco = "", matricula = "",nota_portugues =""):
        
        try:
            self.portugues = nota_portugues
            super(). __init__(nome, rg, contato, endereco, matricula)
        except Exception as e:
            print(str(e)) 
            
    def get_aluno_portugues(self, nota_portugues):
        try:
            self.nota_portugues = nota_portugues
            return print("\n Nota do aluno em portugês: ", nota_portugues)                        
                
        except Exception as e:
            print(str(e))    
    
    def set_aluno_portugues(self, nota_portugues): 
        self.matricula = nota_portugues