def fibonacci_iterative(n):
    """Menghitung bilangan Fibonacci menggunakan algoritma iteratif."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b