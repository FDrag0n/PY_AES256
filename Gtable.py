def GF(a,b):
    bw = [0,0,0,0]
    res = 0
    bw[0] = b
    for i in range(1,4):
        bw[i] = bw[i-1] << 1
        if(bw[i-1] & 0x80):
            bw[i] ^= 0x1b
        bw[i] = bw[i]  & 0xff
    
    for i in range(0,4):
        if((a >> i) & 0x01):
            res ^= bw[i]
    return res


def G_box(n):
    table=[]
    for i in range(0,256):
        i = GF(n,i)
        table.append(i)
    table = tuple(table)
    print(table)

for i in [2,3,9,11,13,14]:
    print(i)
    G_box(i)
    print("-------------------------")
