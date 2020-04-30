from collections import Counter

cnt = Counter()

list = [1,2,3,4,1,2,6,7,3,8,1]

cnt = Counter(list)
print(cnt.most_common(1))