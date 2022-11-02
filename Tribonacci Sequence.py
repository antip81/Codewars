# test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
# test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
# test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
# test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
# test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
# # test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])


def tribonacci(signature, n):
    if n > 2:
        for i in range(3, n, 1):
            signature.append(sum(signature[-3:]))
        return signature
    else:
        for j in range(3 - n):
            signature.pop()
        return signature


signature = [1, 1, 1]
n = 10
print(tribonacci(signature, n))
