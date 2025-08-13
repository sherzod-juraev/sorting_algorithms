def BubbleSort(array):

    if isinstance(array, list):
        moslashuv=True
        for i in range(0,len(array),1):
            if moslashuv==False:
                break
            index=0
            moslashuv=False
            while len(array)-i>index+1:
                if array[index]>array[index+1]:
                    value=array[index]
                    array[index]=array[index+1]
                    array[index+1]=value
                    moslashuv=True
                index+=1

def SelectionSort(array):

    if isinstance(array, list):
        for i in range(len(array)-1,-1,-1):
            select_index=i
            for j in range(i,-1,-1):
                if array[j]>array[select_index]:
                    select_index=j
            value=array[select_index]
            array[select_index]=array[i]
            array[i]=value

def InsertionSort(array):

    if isinstance(array, list):
        for base in range(1,len(array),1):
            value=array[base]
            index=base
            while index>=1 and array[index-1]>value:
                array[index]=array[index-1]
                index-=1
            array[index]=value

def ShellSort(array):

    if isinstance(array, list):
        oraliq=1
        while (oraliq*3+1)<(len(array)/3):
            oraliq=oraliq*3+2
        while oraliq>0:
            for index in range(oraliq,len(array)):
                value=array[index]
                index1=index
                while index1>oraliq-1 and array[index1-oraliq]>=value:
                    if index1<0:
                        break
                    else:
                        array[index1]=array[index1-oraliq]
                        index1=index1-oraliq
                array[index1]=value
            oraliq=oraliq//3
        
def MergeSort(array):

    if isinstance(array, list):
        left=[]
        right=[]
        if len(array)>1:
            middle=len(array)//2
            left=array[0:middle]
            right=array[middle:]
            MergeSort(left)
            MergeSort(right)
        i, j, k = 0, 0, 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1

def ThreeIIndexes(array,left,middle,right):
    
    if isinstance(array,list):
        if array[left]>array[middle]:
            if array[left]>array[right]:
                array[right],array[left]=array[left],array[right]
        else:
            if array[middle]>array[right]:
                array[right],array[middle]=array[middle],array[right]
                
def QuickSortBody(array,left,right):

    if left<right and 0<=left<len(array) and right<len(array) and right-left>5:
        mid=(left+right)//2
        ThreeIIndexes(array, left, mid,right)
        base=array[right]
        i=left
        j=right-1
        while i<j:
            while base>array[i] and i<j:
                i+=1
            while base<array[j] and i<j:
                j-=1
            if i<j:
                array[j],array[i]=array[i],array[j]
                i+=1
                j-=1
        if j==i:
            array[right],array[i]=array[i],array[right]
        QuickSortBody(array, left, j-1)
        QuickSortBody(array, j+1,right)
        
def QuickSortHead(array):
    if isinstance(array,list):
        QuickSortBody(array, 0, (len(array)-1))
        InsertionSort(array)
    