
print("==="*20)
# NAMA : BAYU PURNAMA AJI
# NIM  : 2209116050
# POST 1 ASD MENGENAI SORTING

# SORTING TERDIRI 3, YAITU:
#     1. MERGER SORT
#     2. QUICK SORT
#     3. SHELL SHORT

# =================================================================================
# 1. SOURCE CODE MERGER SORT
import random
import os

os.system("cls")
def mergesort(data):
    if len(data)>1:
        tengah=len(data)//2
        kiri=data[:tengah]
        kanan=data[tengah:]
        
        
        mergesort(kiri)
        mergesort(kanan)
        
        
        i=j=k=0
        
        while i<len(kiri) and j<len(kanan):
            if kiri[i]<kanan[j]:
                data[k]=kiri[i]
                i+=1
                
            else:
                data[k]=kanan[j]
                j+=1
            k+=1
            
        while i<len(kiri):
            data[k]=kiri[i]
            i+=1
            k+=1
        while j<len(kanan):
            data[k]=kanan[j]
            j+=1
            k+=1


data=[12,10,22,30,40,18,17,50,66,6,2]

print("==="*20)
print("==="*20)

print("SORTING MERGER SORT")
print( )
print("Angka awal sebelum diacak dan disorting:")
print(data)
print( )

random.shuffle(data)
print("Pengacakan angka satu kali:")
print(data)
print( )

random.shuffle(data)
print("Pengacakan angka dua kali:")
print(data)
print( )

mergesort(data)
print("Setelah melakukan sorting:")
print(data)
print( )


print("==="*20)
print("==="*20)

# =================================================================================
# 2. SOURCE CODE QUICK SORT
def quickSort(arr):
    if len (arr) <= 1:
        return arr
    else:

        pivot = arr[0]

        left = [x for x in arr [1:] if x <= pivot]

        right = [x for x in arr [1:] if x >= pivot]

        return quickSort(left) + [pivot] + quickSort(right)
    
    
sample_list =[10,8,6,16,26,20,30,50,44,88]
    
arr = sample_list

print("SORTING QUICK SORT")
print()
print("Sebelum diacak:")
print(sample_list)
print( )

random.shuffle(sample_list)
print("Sampel diacak satu kali:")
print(sample_list)
print( )

random.shuffle(sample_list)
print(f"sampel diacak kedua kali:")
print(sample_list)
print( )

print("list sebelum di sort:")
print(arr)
print( )

result = quickSort(arr)

print("list setelah di sort :")
print(result)
print( )

print("==="*20)
print("==="*20)

# =================================================================================
# 3. SOURCE CODE SHELL SORT
def shell(list):
    n = len (list)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = list[i]
            j=i
            while j >= gap and list [j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap

            list [j] = temp
        gap //= 2

    return list

shill=[random.randint(1,50) for i in range(10)]
print("SORTING SHELL SORT")
print()
print("angka sebelum disorting:")
print(shill)
print( )

print("Angka setelah disorting:")
print (shell(shill))
print( )

print("==="*20)
print("==="*20)


# =================================================================================



