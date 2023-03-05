import sys
import threading



def compute_height(n, parents):
    
    skautnes = [[]for i in range(n)]
    sakne = -1
    for i in range (n):
        if parents[i] == -1:
            sakne = i
        else:
            skautnes[parents[i]].append(i)

    max_height = 0
    daudzums = [(sakne, 0)]

    while daudzums:
        node, height = daudzums.pop(0)
        max_height = max(max_height, height)

        for berns in skautnes[node]:
            daudzums.append((berns, height+1))

    return max_height


def main():
    ievade = input()
    if ievade == "F":
        failaNosaukums = input()
    
        with open ("/test" + failaNosaukums, "r") as file:
            n = int(file.readline())
            vecaki = list(map(int, file.readline().split()))
            print(compute_height(n,vecaki)+1)
                
        
    elif ievade == "I":
        n = int(input())
        vecaki = list(map(int,input().split()))
        
    print(compute_height(n,vecaki)+1)



sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)   
threading.Thread(target=main).start()
#print(numpy.array([1,2,3]))