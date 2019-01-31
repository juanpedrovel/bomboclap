def findMedianSortedArrays(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    total_len = len1 + len2
    if total_len == 1:
        result = nums1 + nums2
        return result[0]
    half = 0
    even = False
    if total_len % 2 == 0:
        half = int(total_len / 2) + 1
        even = True
    else:
        half = int((total_len // 2) + 1)
    i = 0
    j = 0
    k = []
    while i < len1 and j < len2:
        if nums1[i] <= nums2[j]:
            k.append(nums1[i])
            i += 1
        else:
            k.append(nums2[j])
            j += 1
        if len(k) == half:
            break
    if len(k) < half:
        x = half - len(k)
        if i == len1:
            k += nums2[j:j+x]
        else:
            k += nums1[i:i+x]
    if even:
        return (k[half-1] + k[half-2]) / 2.0
    else:
        return float(k[half-1])

nums1 = [1,2]
nums2 = [3,4,5]
print(findMedianSortedArrays(nums1, nums2))