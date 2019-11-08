def selection_sort(data):
    n=len(data)
    i=0

    for i in range(n):
        min=data[i]
        for j in range(i+1,n):
            if min>data[j]:
                temp=min
                min=data[j]
                data[j]=temp
                j+=1
            else:
                j+=1
        data[i]=min
        
    return data
    
