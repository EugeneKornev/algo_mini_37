from itertools import permutations

def count_top_sort(edges):
    N = len(edges) + 1
    parents = [[] for _ in range(N)]

    for u, v in edges:
        parents[v].append(u)

    top_sorts = [0] * (1 << N)
    top_sorts[0] = 1

    for mask in range(1 << N):
        for v in range(N):
            if mask & 1 << v:
                continue
            if all(mask & 1 << p for p in parents[v]):
                top_sorts[mask | 1 << v] += top_sorts[mask]

    return top_sorts[-1]

def check_sort(order, edges):
    pos = {node: index for index, node in enumerate(order)}

    for u, v in edges:
        if pos[u] > pos[v]:
            return False
    return True


def naive_count_top_sort(edges):
    N = len(edges) + 1
    count = 0
    vertices = list(range(N))

    for p in permutations(vertices):
        if check_sort(p, edges):
            count += 1

    return count
        
    
def test1():
    edges = []
    assert count_top_sort(edges) == naive_count_top_sort(edges)

def test2():
    edges = [(0, 1)]
    assert count_top_sort(edges) == naive_count_top_sort(edges)

def test3():
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    assert count_top_sort(edges) == naive_count_top_sort(edges)

def test4():
    edges = [(0, 1), (0, 2)]
    assert count_top_sort(edges) == naive_count_top_sort(edges)

def test5():
    edges = [(0, 1), (0, 2), (0, 3)]
    assert count_top_sort(edges) == naive_count_top_sort(edges)

def test6():
    edges = [(0, 1), (0, 4), (0, 7), (1, 2), (1, 3), (4, 5), (4, 6)]
    assert count_top_sort(edges) == naive_count_top_sort(edges)

def test7():
    edges = [(0, 1), (0, 2), (0, 6), (2, 3), (3, 4), (3, 5), (6, 7), (7, 8), (7, 9), (8, 10)]
    assert count_top_sort(edges) == naive_count_top_sort(edges)


if __name__ == "__main__":
    test1()
    print("Test 1: \u2713")
    test2()
    print("Test 2: \u2713")
    test3()
    print("Test 3: \u2713")
    test4()
    print("Test 4: \u2713")
    test5()
    print('Test 5: \u2713')
    test6()
    print("Test 6: \u2713")
    test7()
    print("Test 7: \u2713")
    print("All tests passed")