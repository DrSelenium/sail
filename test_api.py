import json
from main import merge_intervals, min_boats

# Simulate the API logic
def simulate_api(data):
    test_cases = data.get('testCases', [])
    solutions = []
    for test_case in test_cases:
        id_ = test_case['id']
        input_ = test_case['input']
        merged = merge_intervals(input_)
        min_boats_needed = min_boats(input_)
        solution = {
            'id': id_,
            'sortedMergedSlots': merged,
            'minBoatsNeeded': min_boats_needed
        }
        solutions.append(solution)
    return {'solutions': solutions}

data = {
    "testCases": [
        {
            "id": "0001",
            "input": [[1, 8], [17, 28], [5, 8], [8, 10]],
        },
        {
            "id": "0000",
            "input": [[15, 28], [49, 57], [8, 13], [51, 62], [16, 28], [66, 73], [83, 94], [44, 62], [69, 70], [4, 6]],
        },
        {
            "id": "0004",
            "input": [[45, 62], [53, 62], [53, 62], [46, 48], [78, 86], [72, 73], [80, 90], [47, 54], [77, 90], [1, 5]],
        }
    ]
}

result = simulate_api(data)
print(json.dumps(result, indent=4))
