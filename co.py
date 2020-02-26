import glob
import shutil
import os
import random 
import numpy as np 

# Estes sao os diretorios onde vou buscar as imagens todas e as respectivas mascaras
src_dir = "C:\\Users\\Bruno\\Desktop\\images\\img"
src_dir_mask = "C:\\Users\\Bruno\\Desktop\\images\\masks"


# Eu pretendo meter 70% das imagens originais na parta images e as mascaras 
# dessas mesmas imagens na pasta label
# Na pasta teste meter os restantes 30% de imagens

dst_dir = "C:\\Users\\Bruno\\Desktop\\images\\result\\images"
dst_dir_mask = "C:\\Users\\Bruno\\Desktop\\images\\result\\label"
dst_dir_test = "C:\\Users\\Bruno\\Desktop\\images\\result\\test"


# for jpgfile in glob.iglob(os.path.join(src_dir, "%s.png"%fig)):
#     shutil.copy(jpgfile, dst_dir)


# função que gera valores random dentro de uma determinada gama
def Rand(start, end, num): 
    res = [] 
    res=np.array(random.sample(range(start, end), num))
    return res 
  
# Driver Code 
num = int(input("Indique a quantidade de imagens que pretende usar para treinos:"))
start = int(input("Indique o numero da primeira imagem do seu repertorio:"))
end = int(input("Indique o numero da ultima imagem do seu repertorio:"))+1
res=Rand(start, end, num)
print(res) 

# Imagens para teste
for i in range(start, end):
    if i not in res:
        if i<10:
            fig=('00%s' %i)
        elif i>9 and i<100:
            fig=('0%s' %i)
        else:
            fig=('%s'%i)
        jpgfile = src_dir + "\\%s.png"%fig
        shutil.copy(jpgfile, dst_dir_test)
        print(fig)
        

# Imagens para treino
for i in res:
    if i<10:
        fig=('00%s' %i)
        # fig_mask=('masks_00000%s' %i)
        fig_mask=('00%s' %i)
    elif i>9 and i<100:
        fig=('0%s' %i)
        # fig_mask=('masks_0000%s' %i)
        fig_mask=('0%s' %i)
    else:
        fig=('%s' %i)
        # fig_mask=('masks_000%s'%i)
        fig_mask=('%s'%i)
    jpgfile = src_dir + "\\%s.png"%fig
    shutil.copy(jpgfile, dst_dir)
    jpgfile_mask = src_dir_mask + "\\%s.png"%fig_mask
    shutil.copy(jpgfile_mask, dst_dir_mask)