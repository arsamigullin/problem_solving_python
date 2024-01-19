import collections
import os

import json

VISITED, VISITING, UNVISITED = 0, 1, 2


def has_cycle(graph, node, state):
    state.setdefault(node, UNVISITED)
    if state[node] == UNVISITED:
        state[node] = VISITING
        for child in graph[node]:
            if has_cycle(graph, child, state):
                return True
        state[node] = VISITED
        return False
    else:
        return state[node] != VISITED


def load_json_with_comments(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Removing lines that start with //
    cleaned_lines = [line for line in lines if not line.strip().startswith('//')]
    cleaned_content = ''.join(cleaned_lines)

    data = None
    try:
        data = json.loads(cleaned_content)
    except Exception as e:
        print("An error occurred:", e)
        print(filename)

    return data


def dfs(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            dfs(file_path)
        else:
            _, ext = os.path.splitext(file_path)
            if ext == '.json':
                data = load_json_with_comments(file_path)
                if data is None:
                    continue
                # content = file.read()
                graph = collections.defaultdict(list)
                if "Scenarios" not in data:
                    continue
                vals = data["Scenarios"].values()
                for val in vals:
                    if "PrerequisiteScenarioReportingId" in val and "ScenarioReportingId" in val:
                        u = val["PrerequisiteScenarioReportingId"]
                        v = val["ScenarioReportingId"]
                        graph.setdefault(v, [])
                        graph[u].append(v)
                state = collections.defaultdict(int)
                for node in graph:
                    state.setdefault(node, UNVISITED)
                    if state[node] == UNVISITED:
                        cycle_exist = has_cycle(graph, node, state)
                        if cycle_exist == True:
                            print(f"file {file_path} has cycle")


if __name__ == '__main__':
    dfs("D:\projects\Aurora-Base\src\Tests\Manifests\Manifests")
