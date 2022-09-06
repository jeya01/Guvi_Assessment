"""
1.Given 2 numbers N and K and followed by an array of N integers.The given element K is removed from the array and new array is printed.If after removing every occurance of K the array becomes empty, print 'empty' without quotes.
input1:{10,10,20,30,76}, K=10output: {20,20,76}input size : N<=100000

example

INPUT

5 10

10 10 20 30 76

OUTPUT

20 20 76

"""
lst = [10, 10, 20, 20, 76]
k = 10



def remove_ele(lst,k):
    for i in range(0,len(lst)):
        if k in lst:
            lst.remove(k)
    return lst



result = remove_ele(lst, k)
if len(result) > 0:
    print(result)
else:
    print("Empty")














