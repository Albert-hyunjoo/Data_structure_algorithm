def merge_sort_sep(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq)//2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)

def merge(left, right):
    if not left and not right:
        return left or right # 정렬이 없으면 not
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # i와 j가 안에 있는한
        if left[i] <= right[j]: # 만약 left에서의 i번쨰와 right의 j번째에서 right가 큰 경우
            result.append(left[i]) # 더 작은 걸 합하고
            i += 1
        else:
            result.append(right[j]) # 더 작은 걸 합하고
            j += 1 # j의 인덱스를 증가
    if left[i:]: # 한쪽이 먼저 끝나버리면 다른 한 쪽에서 진행된 인덱스부터 끝까지의 배열을 합한다
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    print(result)
    return result

print(merge_sort_sep([5,2,7,9,1,3,10,4]))

