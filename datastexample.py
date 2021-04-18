## bubble sort

def bubble_sort(seq):
    length = len(seq)-1 # 바깥 루프는 3번
    for num in range(length, 0, -1):
        print("--{0}--".format(num))
        for i in range(num):
            print(i)
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq

print(bubble_sort([2,3,1,4]))

# 삽입 정렬 알고리즘의 원리
# 먼저 key = 1부터 시작하고,
# 맨 첫번째 요소와 크기를 비교한다
# 그 다음 차근차근 바꾸어 나가는 것
# 끝나면 그 다음 키로...
# key = outer comparing = inner

def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i # j는 i다. 반대로 i = j는 성립이 X -> J는 결정나지도 않았느데 어떻게 정의에 쓰나?
        while j > 0 and seq[j-1] > seq[j]:
            print("현재 루프:", j)
            print("현재 시퀀스", seq)
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
            print(seq)
    return seq

print(insertion_sort([6,3,2,4,1]))

def gnorm_sort(seq):
    i = 0 # 인덱스 사전 설정
    while i < len(seq): # 인덱스가 배열의 끝까지 가면 종료
        if i==0 or seq[i-1] <= seq[i]: # 만약 현재 첫 인덱스를 훑고 있거나 올바르게 배열된 경우
            i += 1
            print(seq)
        else: # 두쥡고, 그 이전 인덱스의 값과 다시 비교 (인덱스 옮기기)
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
            print(seq)
    return seq

print(gnorm_sort([4,8,1,2,3,6]))

from collections import defaultdict
def count_sort_dict(a):
    b, c = [], defaultdict(list)
    for x in a:
        c[x].append(x)
        print(c)
    for k in range(min(c), max(c)+1):
        b.extend(c[k])
        print(b)
    return b

print(count_sort_dict([3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]))