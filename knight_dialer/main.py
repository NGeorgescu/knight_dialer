

knight_moves = [[4,6],[6,8],[9,7],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]


def KD_recursive(todo,total_length=7):
    """
    
    """
    done=[]
    def dial(the_list):
        ret_list = []
        for i in knight_moves[the_list[-1]]:
            if len(the_list) == total_length:
                done.append(the_list + [i])
            else:
                ret_list.append(dial(the_list + [i]))
        return ret_list
            
    return [dial(i) for i in todo]


def KD_backtrack(todo,total_length=7):
    """
    
    """
    done=[]
    while len(todo)>0:
        workon = todo.pop()
        for move in knight_moves[workon[-1]]:
            if len(workon)==total_length:
                done.append(workon + [move])
            else:
                todo.append(workon + [move])
    return done


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    import time

    trec = []
    tbac = []
    for j in range(2,15):
        t = time.time()
        KD_recursive([[1],[2],[3],[4],[6],[7],[8],[9]],total_length=j)
        t = time.time()-t
        trec.append(t)  
        del t
        
        t = time.time()        
        KD_backtrack([[1],[2],[3],[4],[6],[7],[8],[9]],total_length=j)
        t = time.time()-t
        tbac.append(t)
        del t
    
    plt.figure()
    plt.plot(np.log(trec[2:]),label='recursive')
    plt.plot(np.log(tbac[2:]),label='backtrack')
    plt.legend()
    plt.xlabel('length of dial'); plt.ylabel('ln(time)')
    plt.show()

#%%
    
    
    