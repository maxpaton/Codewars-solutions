import numpy as np

def snail(snail_map):
    
    arr = np.array(snail_map)
    trail = []
    
    while arr.shape[0] > 0:
        # add first row to trail
        for j in range(len(arr[0,:])):
            trail.append(arr[0,j])
        # remove top row and rotate 90 degrees
        arr = np.rot90(arr[1:, :], 1, (0,1))        
    return trail
    
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)