# # Three 1's => 1000 points
# # Three 6's =>  600 points
# # Three 5's =>  500 points
# # Three 4's =>  400 points
# # Three 3's =>  300 points
# # Three 2's =>  200 points
# # One 1 = > 100 points
# # One 5 = > 50 point
#
# Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

# test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
# test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
# test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)

# dice = [2, 3, 4, 6, 2]
# dice = [4, 4, 4, 3, 3]
# dice = [2, 4, 4, 5, 4]
dice = [1, 1, 1, 1, 1]
# dice = [4, 4, 4, 3, 3]
# dice = [1, 3, 3, 3, 6]
# dice = [3, 3, 3, 3, 3]


def score(dice):
    return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
           + dice.count(2)//3 * 200 \
           + dice.count(3)//3 * 300 \
           + dice.count(4)//3 * 400 \
           + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
           + dice.count(6)//3 * 600 \

print(score(dice))