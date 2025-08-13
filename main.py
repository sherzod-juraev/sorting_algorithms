import tartiblash_algoritmlari as tartib
import random,time

arr=[]
while len(arr)!=100:
    arr.append(random.randint(1, 100))
boshlash=time.time()
tartib.BubbleSort(arr)
tugash=time.time()
print(f"BubbleSort: {tugash-boshlash}")
print()

arr=[]
while len(arr)!=100:
    arr.append(random.randint(1, 100))
boshlash=time.time()
tartib.SelectionSort(arr)
tugash=time.time()
print(f"SelectionSort: {tugash-boshlash}")
print()

arr=[]
while len(arr)!=100:
    arr.append(random.randint(1, 100))
boshlash=time.time()
tartib.InsertionSort(arr)
tugash=time.time()
print(f"InsertionSort: {tugash-boshlash}")
print()

arr=[]
while len(arr)!=100:
    arr.append(random.randint(1, 100))
boshlash=time.time()
tartib.ShellSort(arr)
tugash=time.time()
print(f"ShellnSort:  {tugash-boshlash}")
print()

arr=[]
while len(arr)!=1_000_000:
    arr.append(random.randint(1, 100))
boshlash=time.time()
tartib.MergeSort(arr)
tugash=time.time()
print(f"MergeSort: {tugash-boshlash}")
print()

arr=[]
while len(arr)!=1_000_000:
    arr.append(random.randint(1, 100))
boshlash=time.time()
tartib.QuickSortHead(arr)
tugash=time.time()
print(f"QuickSort: {tugash-boshlash}")