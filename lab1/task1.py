def sum_of_prime_divisors(num: int) -> int:
    divisors = set()
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            divisors.add(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        divisors.add(num)
    return sum(divisors)


def odd_digits_bigger_than_3_count(num: int) -> int:
    biggerThan3Cnt = 0
    while num != 0:
        tmp = num%10
        num //= 10
        if tmp>3 and tmp&1==1:
            biggerThan3Cnt += 1
    return biggerThan3Cnt


def divisors_product(num: int) -> int:
    product = 1
    def digits_sum(num: int) -> int:
        sum = 0
        while num != 0:
            sum += num%10
            num //= 10 
        return sum

    for i in range(1, num):
        if(num%i==0 and digits_sum(i) < digits_sum(num)):
            product *= i
    return product


print(sum_of_prime_divisors(10))
print(odd_digits_bigger_than_3_count(10))
print(divisors_product(10))
