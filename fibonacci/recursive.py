def fibonacci_recursive(n):
    """Menghitung bilangan Fibonacci menggunakan algoritma rekursif."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)