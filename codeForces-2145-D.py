import math
import sys
input = sys.stdin.readline

def choose_max_x(S, cap):
    # max x such that C(x,2) <= S and x <= cap
    if S <= 0:
        return 1  # choose singletons when no sum left
    # solve x*(x-1)/2 <= S  => x^2 - x - 2S <= 0
    # positive root = (1 + sqrt(1 + 8S)) / 2
    x = int((1 + math.isqrt(1 + 8*S)) // 2)
    if x < 1:
        x = 1
    if x > cap:
        x = cap
    return x

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    total = n * (n - 1) // 2
    if k < 0 or k > total:
        print(0)
        continue

    S = total - k  # we need sum C(Li,2) = S
    blocks = []
    rem = n
    # Greedily pick block sizes
    while rem > 0:
        x = choose_max_x(S, rem)
        # ensure we don't pick a block that contributes more than S (choose_max_x does that)
        blocks.append(x)
        S -= x * (x - 1) // 2
        rem -= x

    if S != 0:
        # impossible to represent S with block sizes summing to n
        print(0)
        continue

    # Build permutation: take numbers from n downwards, for each block output
    # the block's numbers in increasing order (so each block is increasing,
    # but blocks are in decreasing value order).
    perm = []
    cur = n
    for L in blocks:
        start = cur - L + 1
        perm.extend(range(start, cur + 1))
        cur -= L

    print(*perm)
