import json
from main import merge_intervals, min_boats

# Test data
test_cases = [
    {
        "id": "0001",
        "input": [[1, 8], [17, 28], [5, 8], [8, 10]],
        "expected_merged": [[1, 10], [17, 28]],
        "expected_boats": 2
    },
    {
        "id": "0000",
        "input": [[15, 28], [49, 57], [8, 13], [51, 62], [16, 28], [66, 73], [83, 94], [44, 62], [69, 70], [4, 6]],
        "expected_merged": [[4, 6], [8, 13], [15, 28], [44, 62], [66, 73], [83, 94]],
        "expected_boats": 3
    },
    {
        "id": "0004",
        "input": [[45, 62], [53, 62], [53, 62], [46, 48], [78, 86], [72, 73], [80, 90], [47, 54], [77, 90], [1, 5]],
        "expected_merged": [[1, 5], [45, 62], [72, 73], [77, 90]],
        "expected_boats": 4
    },
    {
        "id": "empty",
        "input": [],
        "expected_merged": [],
        "expected_boats": 0
    },
    {
        "id": "single",
        "input": [[10, 20]],
        "expected_merged": [[10, 20]],
        "expected_boats": 1
    }
]

for test in test_cases:
    merged = merge_intervals(test['input'])
    boats = min_boats(test['input'])
    print(f"ID: {test['id']}")
    print(f"Merged: {merged}")
    print(f"Expected: {test['expected_merged']}")
    print(f"Match: {merged == test['expected_merged']}")
    print(f"Boats: {boats}")
    print(f"Expected: {test['expected_boats']}")
    print(f"Match: {boats == test['expected_boats']}")
    print("---")
