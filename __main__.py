from modules.classe_pessoa import pessoa
from modules.classe_funcionario import funcionario
from modules.classe_aluno import aluno
from modules.classe_aluno_portugues import aluno_portugues
from modules.classe_aluno_matematica import aluno_matematica

if __name__ == "__main__":
    
    try:
        
        while True:
                
            print("Escolha a opção de cadastro: \n")
            selecao =input(" \n1- Cadastrar pessoas? " 
                            "\n2- Cadastrar funcionarios? "
                            "\n3- Cadastrar aluno? "
                            "\n4- Cadastrar nota de português? "
                            "\n5- Cadastrar nota de matematica? "
                            "\n0- sair do sistema? \n"
                                )
            
            if selecao == "1":
                cad_pessoa = pessoa ("nome" , "rg", "contato" ,"endereco")
                cadastrados_pessoas = []
                nome = input("Nome: ")
                rg = input("RG: ")
                contato = input("Contato: ")
                endereco = input("Endereco: ")
                cadastrados_pessoas.append(pessoa.get_pessoa(cad_pessoa, nome, rg, contato, endereco))
                print(cadastrados_pessoas)
        
            elif selecao == "2":
                
                cad_funcionario = funcionario("id" , "cargo")
                cadastrados_func = []
                id = input("id: ")
                cargo = input("cargo: ")
                cadastrados_func.append(funcionario.get_funcionario(cad_funcionario, id, cargo))
                print(cadastrados_func)
                
            elif selecao == "3":
                cad_aluno = aluno ("matricula")
                cadastro_aluno =[]
                matricula = input("Matricula: ")
                cadastro_aluno.append(aluno.get_aluno(cad_aluno, matricula))
                print(cadastro_aluno)

            elif selecao == "4":
                cad_portugues = aluno_portugues ("nota_portugues")
                cadastro_aluno_portugues =[]
                nota_portugues = input("Nota português: ")
                cadastro_aluno_portugues.append(aluno_portugues.get_aluno_portugues(cad_portugues, nota_portugues))
                print(cadastro_aluno_portugues)
            
            elif selecao == "5":
                
                cad_matematica = aluno_matematica("nota matematica") 
                cadastro_aluno_matematica =[]
                nota_matematica = input("Nota matematica: ")
                cadastro_aluno_matematica.append(aluno_matematica.get_aluno_matematica(cad_matematica, nota_matematica))
                print(cadastro_aluno_matematica)
        
            elif selecao == "0": 
                break
    except Exception as e:
        print(str(e))     
    