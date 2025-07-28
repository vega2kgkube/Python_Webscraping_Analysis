# prime_checker.py
num = int(input("숫자를 입력하세요: "))

if num < 2:
    print(f"{num}은 소수가 아닙니다.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num}은 소수입니다.")
    else:
        print(f"{num}은 소수가 아닙니다.")