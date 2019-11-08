def cocktail_sort(data):
    n=len(data)
    basla=0
    bitir=n-1
    for x in range(n):
        yon=True
        if yon:
            for i in range(basla,bitir):
                j=i+1
                if data[i]>data[i+1]:
                    data[i],data[i+1]=data[i+1],data[i]
            bitir+=-1
            yon=False
        
        #x çift sayı ise çevrim sol yönlü
        else:
            for i in range(bitir,basla,-1):
                j=i-1
                if data[i]>data[i-1]:
                    data[i],data[i-1]=data[i-1],data[i]
            basla+=1
            yon=True
        

    return data
