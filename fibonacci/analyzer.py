import time

def measure_execution_time(func, n):
    """
    Mengukur waktu eksekusi fungsi untuk input tertentu.
    
    Args:
        func: Fungsi yang akan dieksekusi.
        n: Input untuk fungsi.
        
    Returns:
        Waktu eksekusi dalam milidetik.
    """
    start_time = time.time()
    func(n)
    end_time = time.time()
    return (end_time - start_time) * 1000