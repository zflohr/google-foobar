def solution(s: str) -> int:
    """Find the maximum number of equal partitions of a string.

    Compute the number of non-overlapping matches of the smallest 
    substring in s such that the product of the length of the 
    substring and the number of matches is the length of s.

    Args:
        s: A non-empty string less than 200 characters in length.

    Returns:
        The maximum number of partitions of s such that all 
        partitions have the same sequence of characters. For example, 
        the maximum number of partitions of "abcabcabcabc" such that 
        all partitions have the same sequence of characters is 4.
    """
    if len(s) >= 200 or len(s) == 0:
        raise Exception("Parameter must be a non-empty string less than 200 "
                        "characters in length!")
    
    # Loop through indices from 1 to half the length of s, disregarding
    # indices that aren't factors of the length of s. Each index is a stop
    # index for creating the substring sub_seq from s. Thus, the length of
    # sub_seq increases by one character in each iteration of the outer loop. 
    # In an inner loop, compare sub_seq with non-overlapping, adjacent 
    # sequences of s whose lengths are equal to the length of sub_seq.
    # Extrapolate the maximum number of equal partitions of s based on these
    # comparisons.
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0:
            sub_seq = s[:i]
            for j in range(i, len(s), i):
                if sub_seq != s[j:j + i]:
                    break
                if j + i == len(s):
                    return len(s) // i
    return 1
