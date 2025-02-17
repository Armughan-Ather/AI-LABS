#Task1 GoalBased DLS
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        return percept == self.goal

    def dls(self, graph, start, goal, depth_limit):
        visited = []

        def dfs(node, depth):
            if depth > depth_limit:
                return None

            visited.append(node)

            if node == goal:
                return visited

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    path = dfs(neighbor, depth + 1)
                    if path:
                        return path
            visited.pop()
            return None
        return dfs(start, 0)

    def act(self, percept, graph, depth_limit):
        if self.formulate_goal(percept):
            return f"Goal {self.goal} found at the start node!"

        path = self.dls(graph, percept, self.goal, depth_limit)
        if path:
            return f"Goal found with DLS. Path: {path}"
        else:
            return "Goal not found within depth limit."

def run_agent(agent, environment, start_node, depth_limit):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph, depth_limit)
    print(action)

start_node = 'A'
goal_node = 'I'
depth_limit = 3
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)
run_agent(agent, environment, start_node, depth_limit)