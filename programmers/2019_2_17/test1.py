# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 유지된 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [498,501,470,489]	[2,1,1,0]
# 입출력 예 설명
# 1초 시점의 ₩498은 2초간 가격을 유지하고, 3초 시점에 ₩470으로 떨어졌습니다.
# 2초 시점의 ₩501은 1초간 가격을 유지하고, 3초 시점에 ₩470으로 떨어졌습니다.
# 3초 시점의 ₩470은 최종 시점까지 총 1초간 가격이 떨어지지 않았습니다.
# 4초 시점의 ₩489은 최종 시점까지 총 0초간 가격이 떨어지지 않았습니다.

def solution(prices):
    answer = []
    price_queue = []

    for p in prices:
        price_queue.append(p)
        while True:
            if price_queue[0] > p:
                price_queue.remove(price_queue[0])
                answer.append(len(price_queue))
            else:
                break
    for _ in range(len(price_queue)):
        price_queue.remove(price_queue[0])
        answer.append(len(price_queue))
    return answer

    # answer = []
    # for i, price in enumerate(prices):
    #     count = 0
    #     pos = i
    #     while pos < len(prices) and price <= prices[pos]:
    #         pos += 1
    #         if pos < len(prices):
    #             count += 1
    #
    #     answer.append(count)
    #
    # return answer


arr1 = [[498,501,470,489,300], [498,501,470,489,300,350],[1,2,3,4], [1,1,1,1]]
return_list = [[2,1,2,1,0], [2,1,2,1,1,0], [3,2,1,0], [3,2,1,0]]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 50 min