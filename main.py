from flask import Flask, request, jsonify
import os

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

@app.route('/')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Sailing Club API is running'})

@app.route('/sailing-club', methods=['POST'])
def sailing_club():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        test_cases = data.get('testCases', [])
        if not isinstance(test_cases, list):
            return jsonify({'error': 'testCases must be a list'}), 400
            
        solutions = []
        for test_case in test_cases:
            if not isinstance(test_case, dict) or 'id' not in test_case or 'input' not in test_case:
                return jsonify({'error': 'Invalid test case format'}), 400
                
            id_ = test_case['id']
            input_ = test_case['input']
            
            if not isinstance(input_, list):
                return jsonify({'error': 'input must be a list of intervals'}), 400
                
            merged = merge_intervals(input_)
            min_boats_needed = min_boats(input_)
            solution = {
                'id': id_,
                'sortedMergedSlots': merged,
                'minBoatsNeeded': min_boats_needed
            }
            solutions.append(solution)
        return jsonify({'solutions': solutions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)
