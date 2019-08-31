import matplotlib.pyplot as plt
import numpy as np


knight_moves = [[4,6],[6,8],[9,7],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]

trec = []
tbac = []
for j in range(2,15):
    t = time.time()
    todo=[[1],[2],[3],[4],[6],[7],[8],[9]]
    done=[]
    def dial(the_list):
        ret_list = []
        for i in knight_moves[the_list[-1]]:
            if len(the_list) == j:
                done.append(the_list + [i])
            else:
                ret_list.append(dial(the_list + [i]))
        return ret_list
            
    [dial(i) for i in todo]
    
    t = time.time()-t
    trec.append(t)   
    print(len(done))
    del todo, done, t
    
    t = time.time()
    
    todo=[[1],[2],[3],[4],[6],[7],[8],[9]]
    done=[]
    while len(todo)>0:
        workon = todo.pop()
        for move in knight_moves[workon[-1]]:
            if len(workon)==j:
                done.append(workon + [move])
            else:
                todo.append(workon + [move])
    
    t = time.time()-t
    tbac.append(t)    
    print(len(done))    
    del todo, done, workon, t

plt.figure()
plt.plot(np.log(trec[2:]),label='recursive')
plt.plot(np.log(tbac[2:]),label='backtrack')
plt.legend()
plt.xlabel('length of dial'); plt.ylabel('ln(time)')
plt.show()

