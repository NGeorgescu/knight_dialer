

knight_moves = [[4,6],[6,8],[9,7],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]

def KD_pure_recursion(todo, total_length=7):
    """
    
    """
    def KD_rec(the_list_of_lists):
        return_val = []
        for the_list in the_list_of_lists:    
            if len(the_list) == total_length-1:
                for i in knight_moves[the_list[-1]]:
                    return_val += [the_list + [i]]
            else:
                for i in knight_moves[the_list[-1]]:
                    return_val += KD_rec([the_list + [i]]) 
        return return_val
        
    return KD_rec(todo).sort()



def KD_recursive_addition(todo,total_length=7):
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
    [dial(i) for i in todo]
    return done.sort()





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
    return done.sort()


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    import time

    trad = []
    tpur = []
    tbac = []
    for j in range(2,15):
        t = time.time()
        rad = KD_recursive_addition([[1],[2],[3],[4],[6],[7],[8],[9]],total_length=j)
        t = time.time()-t
        trad.append(t)  
        del t

        t = time.time()
        pur = KD_pure_recursion([[1],[2],[3],[4],[6],[7],[8],[9]],total_length=j)
        t = time.time()-t
        tpur.append(t)  
        del t
        
        t = time.time()        
        bac = KD_backtrack([[1],[2],[3],[4],[6],[7],[8],[9]],total_length=j)
        t = time.time()-t
        tbac.append(t)
        del t
        
        assert rad == bac
        assert pur == rad
    
    plt.figure()
    plt.plot(np.log(trad[2:]),label='recursive addition')
    plt.plot(np.log(tpur[2:]),label='pure recursion')
    plt.plot(np.log(tbac[2:]),label='backtrack')
    plt.legend()
    plt.xlabel('length of dial'); plt.ylabel('ln(time)')
    plt.show()

#%%
    
    
    