class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        max_prob = [0.0] * n 
        max_prob[start_node]=1.0

        heap = [(-1.0, start_node)]

        while heap:
            cur_prob, cur_node = heapq.heappop(heap)

            if cur_node == end_node:
                return -cur_prob
            
            for child_node, child_node_prob in graph[cur_node]:
                if -cur_prob * child_node_prob > max_prob[child_node]:
                    max_prob[child_node] = -cur_prob * child_node_prob
                    heapq.heappush(heap, (-max_prob[child_node], child_node))

        return 0.0