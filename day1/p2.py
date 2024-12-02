with open('day1/in') as f:
    lines = f.readlines()
    nums1,nums2=[],[]
    for line in lines:
        l = line.split(' ')
        nums1.append(int(l[0]))
        nums2.append(int(l[-1]))

from collections import Counter
nums2 = Counter(nums2)

ans = 0
for i in nums1:
    ans += i * nums2[i]

print(ans)