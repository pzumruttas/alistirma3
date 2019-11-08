def insertion_sort(data):
    i=1
    n=len(data)
    while i<n:
        for x in range(i):
            if data[i]<data[x]:
                data[i],data[x]=data[x],data[i]
            else:
                data[i]=data[i]
        i+=1
    return data
