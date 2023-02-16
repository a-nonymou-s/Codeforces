n, k = map(int, input().split())
scores = list(map(int, input().split()))

k_score = scores[k-1]
num_advancing = 0

if k_score == 0:
    print(num_advancing)
else:
    for score in scores:
        if score >= k_score and score > 0:
            num_advancing += 1
        else:
            break

    print(num_advancing)