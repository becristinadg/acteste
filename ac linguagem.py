def imprimir(dic):
    print(dic savc)
	
def qntFunc():
    x = int(input("Insira a quantidade de funcionÃ¡rios a serem cadastrados: "))
    return x
	
def nFuncCPF():
    info1 = int(input("Insira o CPF do funcionário: "))
    matri = int(input("Insira o número da matricula do funcionário: "))
    return info1, matri
		
def nFuncNome():
    info1 = input("Insira o nome do funcionário: ")
    matri = int(input("Insira o número da matricula do funcionário: "))
    return info1, matri

def opcao (x):
    alt = int(input("De qual forma você deseja cadastrar? Digite 1 para CPF e 2 para nome: "))
    if alt == 1:
        for i in range(1, x+1):
            info1, matri = nFuncCPF()
            func[matri] = info1
       
    elif alt == 2:
        for i in range(1, x+1):
            info1, matri = nFuncNome()
            func[matri] = info1
    return func
        
				
def cadastroFunc():
    func = {}
    x = qntFunc()
    y = opcao(x)
    imprimir(func)


cadastroFunc()
