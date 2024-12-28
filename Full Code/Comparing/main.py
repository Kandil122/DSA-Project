import random
import csv
import matplotlib.pyplot as plt
import time

# Sorting Algorithms (ensure these are correctly imported)
from selectionSort import selectionSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort

# Utility Functions
def generate_array(size, case="random"):
    if case == "best":
        return [i + 1 for i in range(size)]
    elif case == "worst":
        return [size - i for i in range(size)]
    else:
        return [random.randint(1, (size + 1) * 10) for _ in range(size)]

def write_results_to_csv(filename, results):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["InputSize", "Operations", "Time (microseconds)"])
            writer.writerows(results)
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"Failed to write to file: {filename}\nError: {e}")

# Performance Analysis and Visualization
def analyze_sorting_algorithm(algorithm, max_size, step, case="random", arr=None):
    results = []

    if arr is None:
        arr = generate_array(max_size, case)

    for n in range(step, max_size + 1, step):
        arr = generate_array(n, case)  # Re-generate for each case
        start_time = time.time()

        # Assuming the algorithm returns a tuple (sorted_array, comparisons)
        _, comparisons = algorithm(arr)

        elapsed_time = (time.time() - start_time) * 1e6  # Time in microseconds
        print(f"Sorting {case} case of size {n}: Time taken = {elapsed_time:.2f} microseconds")
        results.append((n, comparisons, elapsed_time))

    # Auto-save results to a CSV file
    csv_filename = f"{algorithm.__name__}_{case}_case_results.csv"
    write_results_to_csv(csv_filename, results)

    return results

def plot_comparison_results(results, algorithm_name, case_name):
    if results is None:
        print("Error: The results are None. Cannot plot.")
        return

    plt.figure(figsize=(10, 6))

    n = [x[0] for x in results]
    cmp = [x[1] for x in results]

    # Set the appropriate case label for the graph
    case_label = f"{case_name} Case"

    plt.plot(n, cmp, label=f"{algorithm_name} Comparisons ({case_label})", marker='o')
    plt.xlabel("Input Size")
    plt.ylabel("Comparisons")
    plt.title(f"{algorithm_name} - {case_label}")
    plt.legend()
    plt.grid()
    plt.show()

# User Menu
def print_menu():
    print("\nMENU")
    print("1. Test an individual sorting algorithm")
    print("2. Compare two sorting algorithms")
    print("3. Experimental studies with all algorithms")
    print("4. Exit")

def pick_algorithm():
    algorithms = ["selectionSort", "insertionSort", "mergeSort", "quickSort", "heapSort"]
    print("Available Algorithms:")
    for i, algo in enumerate(algorithms, 1):
        print(f"{i}. {algo}")
    while True:
        try:
            choice = int(input("Select an algorithm (1-5): "))
            if 1 <= choice <= 5:
                return algorithms[choice - 1]
            else:
                print("Invalid choice, please select a valid number.")
        except ValueError:
            print("Invalid input, enter a digit.")

# User Input for Array Type
def input_array_choice():
    print("Choose input method:")
    print("1. Generate array (random / best / worst cases)")
    print("2. Load array from CSV/Excel file")
    choice = int(input("Select an option (1 or 2): "))

    if choice == 1:
        return None
    elif choice == 2:
        filename = input("Enter the CSV/Excel filename (with extension): ")
        return load_array_from_file(filename)
    else:
        print("Invalid choice. Defaulting to array generation.")
        return None

def load_array_from_file(filename):
    try:
        import pandas as pd
        df = pd.read_csv(filename)
        return df.values.flatten()  # Assuming one-column CSV/Excel for simplicity
    except Exception as e:
        print(f"Failed to load array from file: {e}")
        return None

# Main
if __name__ == '__main__':
    while True:
        print_menu()
        try:
            option = int(input("Select an option (1-4): "))

            if option == 1:
                algorithm_name = pick_algorithm()
                array_choice = input_array_choice()
                case = input("Enter the case type (best, average, worst) or leave empty for random: ")
                if not case:
                    case = "random"

                max_size = int(input("Enter the maximum size for analysis: "))
                step = int(input("Enter the step size: "))

                algorithm = globals()[algorithm_name]
                results = analyze_sorting_algorithm(algorithm, max_size, step, case=case, arr=array_choice)
                if results:
                    plot_comparison_results(results, algorithm_name, case)

            elif option == 2:
                algo1_name = pick_algorithm()
                algo2_name = pick_algorithm()

                max_size = int(input("Enter the maximum size for analysis: "))
                step = int(input("Enter step size: "))

                algo1 = globals()[algo1_name]
                algo2 = globals()[algo2_name]

                results1 = analyze_sorting_algorithm(algo1, max_size, step, case="best")
                results2 = analyze_sorting_algorithm(algo2, max_size, step, case="worst")

                plot_comparison_results(results1, algo1_name, "best")
                plot_comparison_results(results2, algo2_name, "worst")

            elif option == 3:
                print("Experimental studies with all algorithms.")
                for algo in [selectionSort, insertionSort, mergeSort, quickSort, heapSort]:
                    for case in ["best", "average", "worst"]:
                        max_size = int(input(f"Enter max size for {algo.__name__} ({case} case): "))
                        step = int(input("Enter step size: "))
                        analyze_sorting_algorithm(algo, max_size, step, case=case)

            elif option == 4:
                print("Exiting program...")
                break

            else:
                print("Invalid option, try again.")

        except ValueError:
            print("Invalid input, enter a digit.")
