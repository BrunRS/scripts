import os
path_image = 'C:\\Users\\Bruno\\Desktop\\images\\result\\images'
path_masks = 'C:\\Users\\Bruno\\Desktop\\images\\result\\label'
path_test = 'C:\\Users\\Bruno\\Desktop\\images\\result\\test'
# path_image = 'C:\\Users\\Bruno\\Desktop\\BRUNO\\image'
# path_masks = 'C:\\Users\\Bruno\\Desktop\\BRUNO\\label'
# path_test = 'C:\\Users\\Bruno\\Desktop\\BRUNO\\test'
files_image = os.listdir(path_image)
files_masks = os.listdir(path_masks)
files_test = os.listdir(path_test)
i=1
for file in files_image:
    name='%s'%i
    os.rename(os.path.join(path_image, file), os.path.join(path_image, name + '.png'))
    i+=1
i=1
for file in files_masks:
    name='%s'%i
    os.rename(os.path.join(path_masks, file), os.path.join(path_masks, name + '.png'))
    i+=1
i=1
for file in files_test:
    name='%s'%i
    os.rename(os.path.join(path_test, file), os.path.join(path_test, name + '.png'))
    i+=1