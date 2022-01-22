import numpy as np
import copy

def RowReduce(mtrx, showSteps = True):
    """
    Row reduces a matrix in the form of a 2d numpy array and return resulting array
    can also shows steps
    """
    
    if showSteps: print(mtrx, "\n")
    
    rowNum = mtrx.shape[0]
    colNum = mtrx.shape[1]

    row = 0

    for col in range(colNum - 1):
        if row >= rowNum: continue#stop if all rows solved
            
        nonZero = True
        if a[row][col] == 0:
            nonZero = False
            for rIdx in range(row, rowNum):
                if mtrx[rIdx][col] != 0:
                    #tries to swap rows if col is 0
                    temp = copy.deepcopy(mtrx[row])
                    mtrx[row] = mtrx[rIdx]
                    mtrx[rIdx] = temp                 
                    nonZero = True
                    if showSteps: print(f"R{row} <-> R{rIdx}")
                    if showSteps: print(mtrx, "\n")
                    break

        if nonZero:
            if mtrx[row][col] != 1:
                if showSteps: print(f"R{row}/{mtrx[row][col]} -> R{row}")
                mtrx[row] *= 1/mtrx[row][col] # normalize to 1
                if showSteps: print(mtrx, "\n")
            for rIdx in range(rowNum):
                if row == rIdx: continue
                if mtrx[rIdx][col] == 0: continue
                if showSteps: print(f"R{rIdx} + ({(-mtrx[rIdx][col])} * R{row}) -> R{rIdx}")
                mtrx[rIdx] += (-mtrx[rIdx][col]) * a[row]#subtract or add until zero
                if showSteps: print(mtrx, "\n")
            row += 1
        
    return mtrx

#a = np.array([[1, 3, -3, -16], [-3, -8, 12, 51], [12, 33, -44, -199]], dtype = np.longdouble)
#a = np.array([[0, 0, 0, 0], [0, 2, 2, 10], [0, 3, 2, 13]], dtype = np.longdouble)
#a = np.array([[2,1,-9,3], [10,4,-42,14]], dtype = np.longdouble)
a = np.array([[-.85, .10, .20, 0],[.75, -.80, .50, 0],[.1, .7, -.7, 0], [1,1,1,1]], dtype = np.longdouble)
#a = np.array([[3, 0, -1, 0, 0],[8, 0, 0, -2, 0],[0, 2, -2, -1, 0]], dtype = np.longdouble)
#a = np.array([[3, 6, 15],[-3, -2, -19],[-2, 2, 0]], dtype = np.longdouble)
RowReduce(a)