from modules.classe_pessoa import pessoa
                    
class funcionario(pessoa):
    
    def __init__(self, id = "", nome = "", rg = "", contato = "", endereco = "", cargo = ""):
        try:    
            self.id = id
            self.cargo = cargo
            super().__init__(nome, rg, contato, endereco)
        except Exception as e:
            print(str(e))
            
    def get_funcionario(self, id, cargo):
        try:
            self.id = id
            self.cargo = cargo
            return print("\n O codigo do id foi: ", id, 
                         "\n O cargo cadastrado foi: ", cargo )
                
        except Exception as e:
            print(str(e))    
    
    def set_funcionario(self,id, cargo):        
        self.id = id
        self.cargo = cargo
        