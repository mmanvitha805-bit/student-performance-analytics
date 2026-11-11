import cProfile
import pstats
import time

def run_analysis():
    import pandas as pd

    df = pd.read_csv("students.csv")

    subjects = [
        "math_marks",
        "physics_marks",
        "programming_marks"
    ]

    df["average_marks"] = df[subjects].mean(axis=1)

    print("Total students:", len(df))
    print("Average marks by subject:")
    print(df[subjects].mean())

    print("Performance analysis completed.")

if __name__ == "__main__":
    start_time = time.perf_counter()

    profiler = cProfile.Profile()
    profiler.enable()

    run_analysis()

    profiler.disable()

    end_time = time.perf_counter()

    print("\n===== PERFORMANCE REPORT =====")
    print("Execution time:", round(end_time - start_time, 4), "seconds")

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    stats.print_stats(10)

    stats.dump_stats("profile_results.prof")
    print("\nProfile saved to profile_results.prof")