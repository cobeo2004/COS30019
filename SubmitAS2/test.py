import time
from iengine import main
import sys

sys.setrecursionlimit(20000)


def run_horn_tt():
    total_time = 0
    for i in range(0, 50):
        start_time = time.perf_counter()
        t_case = f"Components/Datasets/HornTestCases/test{i}.txt"
        print(f"Test case {i}: ", main(t_case, "tt"))
        end_time = time.perf_counter()
        total_time += end_time - start_time
    print(f"--- {total_time * 1000} miliseconds ---")


def run_gen_tt():
    total = 0
    for i in range(0, 50):
        start_time = time.perf_counter()
        t_case = f"Components/Datasets/GeneralTestCases/test{i}.txt"
        print(f"Test case {i}: ", main(t_case, "tt"))
        end_time = time.perf_counter()
        total += end_time - start_time

    print(f"--- {total * 1000} miliseconds ---")


def run_horn_fc():
    total = 0
    for i in range(0, 50):
        start_time = time.perf_counter()
        t_case = f"Components/Datasets/HornTestCases/test{i}.txt"
        print(f"Test case {i}: ", main(t_case, "fc"))
        end_time = time.perf_counter()
        total += end_time - start_time
    print(f"--- {total * 1000} miliseconds ---")


def run_horn_bc():
    total = 0
    for i in range(0, 50):
        start_time = time.perf_counter()
        t_case = f"Components/Datasets/HornTestCases/test{i}.txt"
        print(f"Test case {i}: ", main(t_case, "bc"))
        end_time = time.perf_counter()
        total += end_time - start_time
    print(f"--- {total * 1000} miliseconds ---")


run_horn_tt()
run_gen_tt()
run_horn_fc()
run_horn_bc()
