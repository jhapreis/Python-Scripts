import os

path = '.' #você pode mudar o diretório aqui; 
#se deixar assim, ele busca os que estão no mesmo local

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(file))

files.sort() #ordenar do menor dia para o maior
for i in files:
    print (i, end = ' ')
    
