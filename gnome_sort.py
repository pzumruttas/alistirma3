def gnome_sort(data):
    n=len(data)
    i=0
    while i<(n-1):
        if data[i]>data[i+1]:
            data[i],data[i+1]=data[i+1],data[i]
            if i==0:
                i+=1
            else:
                i+=-1
        else:
            i+=1
            
    return data
