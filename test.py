def find(x, secondString, pre, suff):
    n = len(secondString)
    if x == n:
        return True
    if suff[x] != -1:
        return True
    for i in range(n):
        st = i
        end = i + x + 1
        if end >= n:
            if pre[st] != -1:
                return True
            else:
                return False
        if pre[st] != -1 and suff[end] != -1 and pre[st] < suff[end]:
            # If removing the substring from secondString[i.....i+x-1] makes it a subsequence, then pre[i] ≤ suff[i+x-1] holds.
            return True
    return False


def findDifferenceValue(firstString, secondString):
    n = len(secondString)
    pre = [-1] * n
    suff = [-1] * n
    i = 0
    for k in range(len(firstString)):
        # Creating a prefix array such that pre[i] will denote the minimum index such that secondString[0......i] is a subsequence of firstString[0.....pre[i]].
        if firstString[k] == secondString[i]:
            pre[i] = k
            i += 1
            if i == len(secondString):
                break
    i = len(secondString) - 1
    for k in range(len(firstString) - 1, -1, -1):
        # Creating a suffix array such that suff[i] will denote the maximum index such that secondString[i.......m] is a subsequence of firstString[suff[i].......n].
        if firstString[k] == secondString[i]:
            suff[i] = k
            i -= 1
            if i == -1:
                break
    st = 0
    end = n
    ans = n
    while st <= end:
        # Binary Searching the minimum numbers to be removed to make secondString a subsequence of firstString.
        mid = (st + end) // 2
        fi = find(mid, secondString, pre, suff)
        if fi == True:
            ans = mid
            end = mid - 1
        else:
            st = mid + 1
    return ans