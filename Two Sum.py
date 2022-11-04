# test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
# test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])




def two_sum(numbers, target):
    for i in numbers:
        try:
            if numbers.index(target - i) != numbers.index(i):
                return [numbers.index(i), numbers.index(target - i)]
            else:
                pos = []
                for j in range(len(numbers)):
                    if numbers[j] == i:
                        pos.append(j)
                return pos
        except ValueError:
            pass

nums, summ = [1, 2, 3], 4
nums1, summ1 = [1234,5678,9012], 14690
nums2, summ2 = [2,2,3], 4

print(two_sum(nums, summ))
print(two_sum(nums1, summ1))
print(two_sum(nums2, summ2))