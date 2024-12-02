with open('day1/in') as f:
    lines = f.readlines()
    nums1,nums2=[],[]
    for line in lines:
        l = line.split(' ')
        nums1.append(int(l[0]))
        nums2.append(int(l[-1]))

nums1.sort()
nums2.sort()

ans = 0
for i, j in zip(nums1, nums2):
    ans += abs(i-j)

print(ans)