MAX, MIN = 1000, -1000
nodeIndex = 0
Depth = 3         
Children = 2  
def minimax(depth, nodeIndex, maximizingPlayer,values): 
 
    if depth == Depth:                       
        return values[nodeIndex] 

    if maximizingPlayer: 
        best = MIN
        for i in range(0, Children):    
            val = minimax(depth + 1, nodeIndex * Children + i,False, values) 
            best = max(best, val)   
            print(depth+1,nodeIndex * Children + i,best,val)
        return best 

    else: 
        best = MAX
        
        for i in range(0, Children):        
            val = minimax(depth + 1, nodeIndex * Children + i,True, values) 
            best = min(best, val)  
            print(depth+1,nodeIndex * Children + i ,best,val)
        return best 


if __name__ == "__main__": 

    values = [3, 5, 6, 9, 1, 2, 0, -1] #depth 3, child 2
    #values = [3,12,8,2,4,6,14,5,2] #depth 2, child 3
    #values = [2,7,6,8] #depth 2, child 2
    print(values)
    print("The optimal value is :", minimax(0, nodeIndex, True, values)) 
