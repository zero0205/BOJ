# 문자열 길이와 문자열 입력
l = int(input())
input_str = input()

sum = 0
i = 0

for el in input_str:
    num = ord(el) - 96
    sum += num * pow(31, i)
    i += 1
    
print(sum % 1234567891)