import time


def time_check(n_operations: int) -> float:
    resultat = 1
    start_time = time.time()
    for i in range(n_operations):  # 1 addition (i increment) + 1 comparison (i < n_op)
        resultat *= 2  # 1 multiplication + 1 assignation
    end_time = time.time()
    return end_time-start_time


for i in range(1, 11):
    print(f"{i*100000} opérations : {time_check(i*100000)} s")
