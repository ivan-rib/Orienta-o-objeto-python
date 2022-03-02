class pessoa:
    
    def __init__(self, nome = "", rg = "", contato = "", endereco = ""):
        try:    
            self.nome = nome
            self.rg = rg
            self.contato = contato
            self.endereco = endereco
                            
        except Exception as e:
                    print(str(e))
    
    def get_pessoa(self, nome, rg, contato, endereco):
        try:
            self.nome = nome
            self.rg = rg
            self.contato = contato
            self.endereco = endereco
            return print("\n O Nome cadastrado do foi: ", nome, 
                         "\n O RG cadastrado foi: ", rg,
                         "\n O contato cadastrado foi: ", contato, 
                         "\n Endereço: ", endereco )
                
        except Exception as e:
            print(str(e))    
    
    def set_pessoa(self, nome, rg, contato, endereco):        
        self.nome = nome
        self.rg = rg
        self.contato = contato
        self.endereco = endereco            
        
                        

    
    
            
        
            
