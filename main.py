from flask import Flask, request, jsonify

app = Flask(__name__)

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

def min_boats(intervals):
    if not intervals:
        return 0
    events = []
    for start, end in intervals:
        events.append((start, 1))  # start
        events.append((end, -1))  # end
    events.sort()
    current = 0
    max_boats = 0
    for time, event in events:
        current += event
        max_boats = max(max_boats, current)
    return max_boats

@app.route('/sailing-club', methods=['POST'])
def sailing_club():
    data = request.get_json()
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
    return jsonify({'solutions': solutions})

if __name__ == '__main__':
    app.run(debug=True)
