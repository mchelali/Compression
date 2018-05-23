# -*- coding : utf-8 -*-

def encodeRZW(vector):
    symbole = [chr(i) for i in range(97, 97+26)]
    code = []
    p='' #p is the previus symbole
    for i in vector:
        if (p+i) in symbole:
            p=p+i
        else:
            symbole.append(p+i)
            code.append(symbole.index(p))
            p=i
    code.append(symbole.index(p))
    #print symbole
    return code

def decodeRZW(code):
    symbole = [chr(i) for i in range(97, 97+26)]
    decode = symbole[code[0]]
    pw=code[0]
    for i in code[1:]:
        if (symbole[i]):
            decode=decode+symbole[i]
            symbole.append(symbole[pw]+symbole[i][0])
            pw=i
    #print symbole
    return decode


if __name__=="__main__":
    #T = "wabbawabba"
    T= "tobeornottobeortobeornot"

    code = encodeRZW(T)

    print T, len(T)
    print code, len(code)

    #print "size of file = ", T.__len__()*8
    #print "size of code = ", code.__len__()*8
    #print "the diffrent is ", T.__len__()*8-code.__len__()*8

    print decodeRZW(code)
