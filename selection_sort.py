import time 


A = list(range(3000))

#A = [64,25,12,22,11 ]

def selection_sort(A):
    for i in range (len(A)):
        min_idx = i

        for j in range(i+1,len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i],A[min_idx] = A[min_idx],A[i]

    return A



start_time = time.time()
print(selection_sort(A))
print("...%s seconds..."%(time.time()- start_time))