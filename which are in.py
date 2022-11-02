# a1 = ["live", "arp", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp', 'live', 'strong']
# testing(a1, a2, r)
# a1 = ["arp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp']

# Example 1:
# a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# Example 2:
# a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []


array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]


def in_array(array1, array2):
    array3 = set()
    for i in array1:
        for j in array2:
            if i in j:
                array3.add(i)
    return sorted(array3)

