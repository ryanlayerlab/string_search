import tracemalloc
import time
import numpy as np

def naive_search(text, pattern):
    occurrences = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences

def test_harness(f, n, text, pattern):

    run_times = []
    mem_usages = []


    for i in range(n):
        start = time.monotonic_ns()
        r = f(text, pattern)
        stop = time.monotonic_ns()

        run_times.append(stop - start)

        tracemalloc.start()
        r = f(text, pattern)
        mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        mem_usages.append( mem[1] - mem[0])

    return (run_times, mem_usages)

def main():
    text = 'abcabc'
    pattern = 'abc'

    n = 10

    (run_times, mem_usages) = test_harness(naive_search, n, text, pattern)

    print(f'run_times: {np.mean(run_times)}')
    print(f'mem_usages: {np.mean(mem_usages)}')

if __name__ == '__main__':
    main()
