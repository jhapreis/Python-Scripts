import time

time_value = time.localtime() #Obtem a data local
time_string = time.strftime("%Y,%m,%d, %H:%M:%S", time_value) #String formatada como dito
print (time_string)

file_name = time_string + '.txt' #Nome para o arquivo
file = open ( file_name , 'w') #Cria o arquivo e dá o nome anterior a ele

loop = True #Condição para dar início ao loop

while (loop == True) : #Loop infinito, ou até precisar parar
        
    time_variable = time.localtime() #Obtem o novo horário a cada laço do loop
    time_string = time.strftime("%Y,%m,%d, %H:%M:%S", time_variable)
    
    file.write (time_string) #Escreve esta informação (a data) a cada novo laço
    
    #Possível solução para múltiplas inscrições ao mesmo tempo:
    #delay de um segundo
    
    time.sleep(1)
                   
#Se o tempo que ele gerou o arquivo for diferente do tempo do útlimo laço
#do loop (eu coloquei em min. só pra testar), ele para o loop e fecha o arquivo
    if (time_value.tm_min != time_variable.tm_min) :
        loop = False
        file.close() 

file = open (file_name , 'r') 
print ( file.read() )