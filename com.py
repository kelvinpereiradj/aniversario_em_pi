"""mensagem='pi_reformulado.txt'
frase=""
with open(mensagem) as me:
	linhas=me.readlines()
for linha in linhas:
	frase+=linha"""



from txt_p_string import endereço_p_string
#transforma um arquivo txt para string

endereço="pi_reformulado.txt"
if endereço:
	endereço=endereço
else :
	endereço=input("\tDigite o endereço do arquivo txt:\n\n\t")

#entre as aspas, digite o txt em que está contido o valor de PI
#exemplo  endereço="pi_reformulado.txt"

frase=endereço_p_string(endereço)


aqui= input("   \n\n\tSUA DATA DE ANIVERSÁRIO ESTÁ CONTIDA\n \tNO PRIMEIRO MILHÃO DAS CASAS DE PI?\n\n\n   \tDigite sua data de aniversário:\n\t")

frase_numero=len(frase)
frase_lista=list(frase)
novo_um=-1
novo_dois=0
novo_tres=1
novo_quatro=2
novo_cinco=3
novo_seis=4
contador=-1

for conta in range(frase_numero):
	contador+=1
	novo_um+=1
	novo_dois+=1
	novo_tres+=1
	novo_quatro+=1
	novo_cinco+=1
	novo_seis+=1
	if novo_seis<frase_numero:
		posi_um=frase_lista[novo_um]
		posi_dois=frase_lista[novo_dois]
		posi_tres=frase_lista[novo_tres]
		posi_quatro=frase_lista[novo_quatro]
		posi_cinco=frase_lista[novo_cinco]
		posi_seis=frase_lista[novo_seis]
		um_a_seis=posi_um+posi_dois+posi_tres+posi_quatro+posi_cinco+posi_seis
#		print(um_a_seis)
	if um_a_seis==aqui:
		print("\n\n\tSIM, na casa:   "+str(contador)+"\n\n\t   "+str(novo_um)+"   "+str(novo_dois)+"   "+str(novo_tres)+"   "+str(novo_quatro)+"   "+str(novo_cinco)+"   "+str(novo_seis))

