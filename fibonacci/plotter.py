import matplotlib.pyplot as plt

def plot_execution_times(inputs, iterative_times, recursive_times):
    """
    Membuat grafik perbandingan waktu eksekusi.
    
    Args:
        inputs: Daftar ukuran input.
        iterative_times: Waktu eksekusi algoritma iteratif.
        recursive_times: Waktu eksekusi algoritma rekursif.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(inputs, iterative_times, label="Iterative", marker="o")
    plt.plot(inputs, recursive_times, label="Recursive", marker="x", linestyle="--")
    
    plt.title("Execution Time Comparison")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid()
    plt.show()