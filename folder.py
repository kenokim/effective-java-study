import os
for i in range (1, 91):
    path_dir = 'item' + str(i)
    os.makedirs(path_dir)
    open (path_dir + '/' + 'README.md', 'w')
    
