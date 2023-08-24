def test_sorting_algorithms():
    test_cases = [
        [],
        [1],
        [3, 2, 1],
        [5, 9, 3, 6, 2],
        [10, 8, 6, 4, 2, 0],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [9, 1, 8, 2, 7, 3, 6, 4, 5],
    ]

    for test in test_cases:
        insertion_sorted = test.copy()
        merge_sorted = test.copy()

        insertion_sort(insertion_sorted)
        merge_sort(merge_sorted)

        print(f"Original: {test}")
        print(f"Insertion Sorted: {insertion_sorted}")
        print(f"Merge Sorted: {merge_sorted}")
        print("=" * 30)

if __name__ == "__main__":
    test_sorting_algorithms()
