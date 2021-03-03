#pede um endereço de txt e retorna uma string

def endereço_p_string(endereço):
	
	mensagem=endereço
	frase=""
	with open(mensagem) as me:
		linhas=me.readlines()
	for linha in linhas:
		frase+=linha
	return frase
	
