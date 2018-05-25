#-*-coding: utf-8 -*-

def RLEncoding(vec):
    """
        Appliquer le codage RLE
    """
    RLE_c = [] # represente la valeur
    RLE_p = [] # represente le nbr derepetition de la valeur
    rep = 0
    for i in range(1,len(vec)):
        if(vec[i-1]==vec[i]):
            rep=rep+1
        else:
            RLE_p.append(rep+1)
            RLE_c.append(vec[i-1])
            rep=0
    RLE_p.append(rep + 1)
    RLE_c.append(vec[len(vec)-1])
    return RLE_c, RLE_p
    
def RLEncoding_time(vec, timeVec):
    """
        Appliquer le codage RLE
    """
    RLE_c = []  # represente la valeur
    RLE_p = []  # represente le nbr derepetition de la valeur
    RLE_t = []  # represente le nbr de jour que le pixel ne change pas
    rep = 0
    t = 0
    t_1 = 0

    for i in range(1, len(vec)):
        if abs(vec[i - 1] - vec[i]) <= 30:
            rep = rep + 1
            t_1 = i
        else:
            RLE_p.append(rep + 1)
            RLE_c.append(vec[i - 1])
            RLE_t.append(timeVec[t_1]-timeVec[t])
            t = i
            t_1 = i
            rep = 0
            if timeVec[t_1]-timeVec[t] < 0:
                print "val negatif => ", timeVec[t_1]-timeVec[t]

    RLE_p.append(rep + 1)
    RLE_c.append(vec[len(vec) - 1])
    RLE_t.append(timeVec[t_1] - timeVec[t])

    return RLE_c, RLE_p, RLE_t
