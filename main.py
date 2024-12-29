from fibonacci.iterative import fibonacci_iterative
from fibonacci.recursive import fibonacci_recursive
from fibonacci.analyzer import measure_execution_time
from fibonacci.plotter import plot_execution_times

def main():
    inputs = [5, 10, 15, 20, 25, 30]
    
    iterative_times = []
    recursive_times = []
    
    for n in inputs:
        print(f"Processing n = {n}...")
        iterative_time = measure_execution_time(fibonacci_iterative, n)
        recursive_time = measure_execution_time(fibonacci_recursive, n)
        
        iterative_times.append(iterative_time)
        recursive_times.append(recursive_time)
    
    plot_execution_times(inputs, iterative_times, recursive_times)

if __name__ == "__main__":
    main()