def bubble_sort(data):
    n=len(data)
    for x in range(n):
        for i in range(1,n-x):
            j=i-1
            if data[j]>data[i]:
                data[j],data[i]=data[i],data[j]
            else:
                data[i]=data[i]

    return data
   
