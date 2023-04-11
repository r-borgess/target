def fibonacci(n):
    """lista dos n primeiros numeros da sequencia de fibonacci"""
    seq = [0, 1]
    while len(seq) < n:
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return seq

def is_fibonacci(num):
    """verifica se um numero pertence à sequência de fibonacci"""
    seq = fibonacci(100)
    return num in seq

num = int(input("Digite um numero: "))

if is_fibonacci(num):
    print(f"{num} pertence à sequência")
else:
    print(f"{num} NÃO pertence à sequência")
