## 10부터 1까지 곱하는 예

# def multiple(num):
#     if num <= 1:
#         return 1
#     return num * multiple(num-1)
#
# print(multiple(10))

## 5! 을 재귀 호출로 구현

# def factorial(num):
#     if num <= 1:
#         print('1 반환')
#         return 1
#     print(f'{num}*{num-1}! 호출')
#     mul = factorial(num-1)
#
#     print(f'{num}*{num-1}!(={mul}) 반환')
#     return num * mul
#
# print('\n5! =', factorial(5))

##
