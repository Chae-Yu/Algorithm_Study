# 문제
# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.
# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
# 입력
# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 출력
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

# 1. 오름차순으로 정렬
# 2. 같은 수끼리 나누기
# 3. 길이 비교해서 그 중 작은 수 출력
# 딕셔너리를 통해 키값에 카드번호(고유함), 벨류에 카드 개수 

cardDic={}
N=int(input())

for _ in range(N):
    card = int(input())
    if card in cardDic:
        cardDic[card] += 1
    else:
        cardDic[card] = 1

ans = sorted(cardDic.items(), key=lambda x: (-x[1],x[0]))
print(ans[0][0])