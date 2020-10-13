import time
import os
from random import randint

class InsertionSort: 
    def __init__(self, arr):
        self.OverTime = False
        tStart = time.perf_counter() # 計時開始
        for i in range(1, len(arr)): 
            key = arr[i] 
            j = i-1
            while j >=0 and key < arr[j] and not self.OverTime : 
                arr[j+1] = arr[j] 
                j -= 1
                tEnd = time.perf_counter() # 計時檢查
                if tEnd - tStart >= 3600: 
                    self.OverTime = True
            arr[j+1] = key 
            if self.OverTime :
                break
        



class MergeSort:
    def __init__(self, arr):
        self.OverTime = False
        self.tStart = time.perf_counter() # 計時開始
        self.Merge_Sort(arr)

    def Merge_Sort(self, array):
        tEnd = time.perf_counter() # 計時檢查
        if tEnd - self.tStart >= 3600:
            self.OverTime = True
            return
        if len(array) > 1:
            mid = len(array) // 2
            left_array = array[:mid]
            right_array = array[mid:]

            self.Merge_Sort(left_array)
            self.Merge_Sort(right_array)

            right_index = 0;
            left_index = 0;
            merged_index = 0;
            while right_index < len(right_array) and left_index < len(left_array):
                if(right_array[right_index] < left_array[left_index]):
                    array[merged_index] = right_array[right_index]
                    right_index = right_index + 1
                else:
                    array[merged_index] = left_array[left_index]
                    left_index = left_index + 1

                merged_index = merged_index + 1

            while right_index < len(right_array):
                array[merged_index] = right_array[right_index]
                right_index = right_index + 1
                merged_index = merged_index + 1

            while left_index < len(left_array):
                array[merged_index] = left_array[left_index]
                left_index = left_index + 1
                merged_index = merged_index + 1


class RandomizedQuickSort:
    def __init__(self, arr):
        self.OverTime = False
        self.tStart = time.perf_counter() # 計時開始
        self.quicksort(arr, 0, len(arr)-1)

    def quicksort(self, arr, start , stop):
        tEnd = time.perf_counter() # 計時檢查
        if tEnd - self.tStart >= 3600:
            self.OverTime = True
            return
        if(start < stop):
            pivotindex = self.partitionrand(arr,start, stop)
            self.quicksort(arr , start , pivotindex-1)
            self.quicksort(arr, pivotindex + 1, stop)


    def partitionrand(self, arr , start, stop):
        randpivot = randint(start, stop)
        arr[start], arr[randpivot] = arr[randpivot], arr[start]
        return self.partition(arr, start, stop)

    def partition(self, arr,start,stop):
        pivot = start # pivot
        
        i = start + 1
        
        # partition in the array starts from.
        for j in range(start + 1, stop + 1):
            if arr[j] <= arr[pivot]:
                arr[i] , arr[j] = arr[j] , arr[i]
                i = i + 1
        arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
        pivot = i - 1
        return (pivot)


'''
class RandomizedQuickSort:
    def __init__(self, arr):
        self.OverTime = False
        self.tStart = time.perf_counter() # 計時開始
        self.quicksort(arr, 0, len(arr)-1)
        
    def quicksort(self, arr, start, end):
        tEnd = time.perf_counter() # 計時檢查
        if tEnd - self.tStart >= 3600:
            self.OverTime = True
            return arr
        if start < end:
            pIndex = self.partition(arr, start, end)
            self.quicksort(arr, start, pIndex-1)
            self.quicksort(arr, pIndex+1, end)
        return arr

    def partition(self, arr, start, end):
        pivot = randint(start, end)
        temp = arr[end]
        arr[end] = arr[pivot]
        arr[pivot] = temp
        pIndex = start
        
        for i in range(start, end):
            if arr[i] <= arr[end]:
                temp = arr[i]
                arr[i] = arr[pIndex]
                arr[pIndex] = temp
                pIndex += 1
        temp1 = arr[end]
        arr[end] = arr[pIndex]
        arr[pIndex] = temp1
        
        return pIndex
'''

class CountingSort:
    def __init__(self, arr, size = 0):
        self.OverTime = False
        self.tStart = time.perf_counter() # 計時開始
        rec = [0]*max(1001,size+1)
        for i in range(len(arr)):
            rec[arr[i]] += 1
            tEnd = time.perf_counter() # 計時檢查
            if tEnd - self.tStart >= 3600:
                self.OverTime = True
                break
        index = 0
        for i in range(1001):
            if rec[i] >= 0 :
                for j in range(index, index + rec[i]) :
                    arr[j] = i
                    tEnd = time.perf_counter() # 計時檢查
                    if tEnd - self.tStart >= 3600:
                        self.OverTime = True
                        break
                index = index + rec[i]
            if self.OverTime :
                break

        