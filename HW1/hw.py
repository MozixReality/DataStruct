import Sort
import time
import random
import csv

def gen_data_1(seed, k):
    random.seed(seed)
    Len = 2**k
    data = []
    for i in range(Len):
        data.append(random.randint(1,1000))
    return data

def gen_data_2(k):
    Len = 2**k + 1
    data = []
    for i in range(1,Len):
        data.append(i)
    for i in range(100):
        data[random.randint(0,Len-2)] = random.randint(1,1000)
    return data

OverTime = [False]*8
OverTime[0] = True
OverTime[4] = OverTime[5] = True
File = open("test.txt","w")
with open('ans.csv', "r+") as csvFile:
    csvFile.truncate()
    writer = csv.writer(csvFile)
    writer.writerow(['Sort', 'case', 'k', 'time(ms)'])
for k in range(27,31):
#for k in range(10,12):
    seed = []
    for i in range(10):
        seed.append(random.randint(0,1000))
    # sol 1 gen 1
    if not OverTime[0]:
        T = []
        for i in range(10):
            data = gen_data_1(seed[i], k)
            tStart = time.perf_counter() # 計時開始
            check = Sort.InsertionSort(data)
            if check.OverTime:
                OverTime[0] = True
                msg = "Insertion Sort        in case 1 k = " + str(k) + " Time : Over Time"
                ans_1_1 = ['Insertion Sort', 'case 1', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[0]:
            Tavg = sum(T) / len(T)
            msg = "Insertion Sort        in case 1 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_1_1 = ['Insertion Sort', 'case 1', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Insertion Sort        in case 1 k = " + str(k) + " Time : Over Time"
        ans_1_1 = ['Insertion Sort', 'case 1', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 1 gen 2
    if not OverTime[1] :
        T = []
        for i in range(10):
            data = gen_data_2(k)
            tStart = time.perf_counter() # 計時開始
            check = Sort.InsertionSort(data)
            if check.OverTime:
                OverTime[1] = True
                msg = "Insertion Sort        in case 2 k = " + str(k) + " Time : Over Time"
                ans_1_2 = ['Insertion Sort', 'case 2', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[1]:
            Tavg = sum(T) / len(T)
            msg = "Insertion Sort        in case 2 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_1_2 = ['Insertion Sort', 'case 2', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Insertion Sort        in case 2 k = " + str(k) + " Time : Over Time"
        ans_1_2 = ['Insertion Sort', 'case 2', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 2 gen 1
    if not OverTime[2] :
        T = []
        for i in range(10):
            data = gen_data_1(seed[i], k)
            tStart = time.perf_counter() # 計時開始
            check = Sort.MergeSort(data)
            if check.OverTime:
                OverTime[2] = True
                msg = "Merge Sort            in case 1 k = " + str(k) + " Time : Over Time"
                ans_2_1 = ['Merge Sort', 'case 1', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[2]:
            Tavg = sum(T) / len(T)
            msg = "Merge Sort            in case 1 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_2_1 = ['Merge Sort', 'case 1', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Merge Sort            in case 1 k = " + str(k) + " Time : Over Time"
        ans_2_1 = ['Merge Sort', 'case 1', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 2 gen 2
    if not OverTime[3] :
        T = []
        for i in range(10):
            data = gen_data_2(k)
            tStart = time.perf_counter() # 計時開始
            check = Sort.MergeSort(data)
            if check.OverTime:
                OverTime[3] = True
                msg = "Merge Sort            in case 2 k = " + str(k) + " Time : Over Time"
                ans_2_2 = ['Merge Sort', 'case 2', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[3]:
            Tavg = sum(T) / len(T)
            msg = "Merge Sort            in case 2 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_2_2 = ['Merge Sort', 'case 2', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Merge Sort            in case 2 k = " + str(k) + " Time : Over Time"
        ans_2_2 = ['Merge Sort', 'case 2', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 3 gen 1
    if not OverTime[4]:
        T = []
        for i in range(10):
            data = gen_data_1(seed[i], k)
            tStart = time.perf_counter() # 計時開始
            check = Sort.RandomizedQuickSort(data)
            if check.OverTime:
                OverTime[4] = True
                msg = "Randomized Quick Sort in case 1 k = " + str(k) + " Time : Over Time"
                ans_3_1 = ['Randomized Quick Sort', 'case 1', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[4]:
            Tavg = sum(T) / len(T)
            msg = "Randomized Quick Sort in case 1 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_3_1 = ['Randomized Quick Sort', 'case 1', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Randomized Quick Sort in case 1 k = " + str(k) + " Time : Over Time"
        ans_3_1 = ['Randomized Quick Sort', 'case 1', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 3 gen 2
    if not OverTime[5]:
        T = []
        for i in range(10):
            data = gen_data_2(k)
            tStart = time.perf_counter() # 計時開始
            check = Sort.RandomizedQuickSort(data)
            if check.OverTime:
                OverTime[5] = True
                msg = "Randomized Quick Sort in case 2 k = " + str(k) + " Time : Over Time"
                ans_3_2 = ['Randomized Quick Sort', 'case 2', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[5]:
            Tavg = sum(T) / len(T)
            msg = "Randomized Quick Sort in case 2 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_3_2 = ['Randomized Quick Sort', 'case 2', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Randomized Quick Sort in case 2 k = " + str(k) + " Time : Over Time"
        ans_3_2 = ['Randomized Quick Sort', 'case 2', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 4 gen 1
    if not OverTime[6]:
        T = []
        for i in range(10):
            data = gen_data_1(seed[i], k)
            tStart = time.perf_counter() # 計時開始        
            check = Sort.CountingSort(data)
            if check.OverTime:
                OverTime[6] = True
                msg = "Counting Sort         in case 1 k = " + str(k) + " Time : Over Time"
                ans_4_1 = ['Counting Sort', 'case 1', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[6]:
            Tavg = sum(T) / len(T)
            msg = "Counting Sort         in case 1 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_4_1 = ['Counting Sort', 'case 1', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        msg = "Counting Sort         in case 1 k = " + str(k) + " Time : Over Time"
        ans_4_1 = ['Counting Sort', 'case 1', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 4 gen 2
    if not OverTime[7]:
        T = []
        for i in range(10):
            data = gen_data_2(k)
            tStart = time.perf_counter() # 計時開始        
            check = Sort.CountingSort(data,2**k)
            if check.OverTime:
                OverTime[7] = True
                msg = "Counting Sort         in case 2 k = " + str(k) + " Time : Over Time"
                ans_4_2 = ['Counting Sort', 'case 2', k, "Over Time"]
                #print(msg)
                msg += "\n"
                File.write(msg)
                break
            tEnd = time.perf_counter() # 計時結束
            T.append(tEnd - tStart)
        if not OverTime[7]:
            Tavg = sum(T) / len(T)
            msg = "Counting Sort         in case 2 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
            ans_4_2 = ['Counting Sort', 'case 2', k, round(Tavg*1000, 5)]
            #print(msg)
            msg += "\n"
            File.write(msg)
    else:
        OverTime[7] = True
        msg = "Counting Sort         in case 2 k = " + str(k) + " Time : Over Time"
        ans_4_2 = ['Counting Sort', 'case 2', k, "Over Time"]
        #print(msg)
        msg += "\n"
        File.write(msg)
    # sol 5 gen 1
    T = []
    for i in range(10):
        data = gen_data_1(seed[i], k)
        tStart = time.perf_counter() # 計時開始
        data.sort()
        tEnd = time.perf_counter() # 計時結束
        T.append(tEnd - tStart)
    Tavg = sum(T) / len(T)
    msg = "Tim Sort              in case 1 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
    ans_5_1 = ['Tim Sort', 'case 1', k, round(Tavg*1000, 5)]
    #print(msg)
    msg += "\n"
    File.write(msg)
    # sol 5 gen 2
    T = []
    for i in range(10):
        data = gen_data_2(k)
        tStart = time.perf_counter() # 計時開始
        data.sort()
        tEnd = time.perf_counter() # 計時結束
        T.append(tEnd - tStart)
    Tavg = sum(T) / len(T)
    msg = "Tim Sort              in case 2 k = " + str(k) + " Time : " + str(round(Tavg*1000, 5)) + " (ms)"
    ans_5_2 = ['Tim Sort', 'case 2', k, round(Tavg*1000, 5)]
    #print(msg)
    msg += "\n\n"
    File.write(msg)

    # 結束換行
    #print("\n")
    with open('ans.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(ans_1_1)
        writer.writerow(ans_1_2)
        writer.writerow(ans_2_1)
        writer.writerow(ans_2_2)
        writer.writerow(ans_3_1)
        writer.writerow(ans_3_2)
        writer.writerow(ans_4_1)
        writer.writerow(ans_4_2)
        writer.writerow(ans_5_1)
        writer.writerow(ans_5_2)

# 迴圈結束
File.close()
    



