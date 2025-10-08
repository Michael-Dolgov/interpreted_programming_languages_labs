#1
def max_prime_divisor(num: int) -> int:
    max_prime = 1
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            max_prime = divisor
            num //= divisor
        divisor += 1
    if num > 1:
        max_prime = num
    return max_prime


#2
def product_of_digits_not_divisible_by_5(num: int) -> int:
    product = 1
    has_valid_digit = False
    while num != 0:
        digit = num % 10
        num //= 10
        if digit != 0 and digit % 5 != 0:
            product *= digit
            has_valid_digit = True
    return product if has_valid_digit else 0


def max_odd_nonprime_divisor(num: int) -> int:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    max_divisor = 1
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 1 and not is_prime(i):
            max_divisor = i
    return max_divisor


#3
def gcd_of_max_odd_nonprime_and_product_of_digits(num: int) -> int:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    max_odd_nonprime = max_odd_nonprime_divisor(num)
    product = 1
    tmp = num
    while tmp != 0:
        digit = tmp % 10
        tmp //= 10
        product *= digit if digit != 0 else 1
    return gcd(max_odd_nonprime, product)


print(max_prime_divisor(60))                    
print(product_of_digits_not_divisible_by_5(753)) 
print(gcd_of_max_odd_nonprime_and_product_of_digits(90)) 
