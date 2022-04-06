package programmers;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution12978 {
	public int solution(int N, int[][] road, int K) {

		int[][] cost = new int[N + 1][N + 1];
		for (int i = 1; i < N + 1; i++) {
			Arrays.fill(cost[i], Integer.MAX_VALUE);
			cost[i][i] = 0;
		}

		for (int[] edge : road) {
			cost[edge[0]][edge[1]] = Math.min(cost[edge[0]][edge[1]], edge[2]);
			cost[edge[1]][edge[0]] = Math.min(cost[edge[1]][edge[0]], edge[2]);
		}

		for (int k = 1; k < N + 1; k++) {
			for (int a = 1; a < N + 1; a++) {
				if (cost[a][k] == Integer.MAX_VALUE || a == k) continue;
				for (int b = 1; b < N + 1; b++) {
					if (cost[k][b] == Integer.MAX_VALUE) continue;
					cost[a][b] = Math.min(cost[a][b], cost[a][k] + cost[k][b]);
				}
			}
		}
		int answer = 0;
		for (int i = 1; i < N + 1; i++) {
			if (cost[1][i] <= K) {
				++answer;
			}
		}
		return answer;
	}

	static class Solution2 {
		public int solution(int N, int[][] road, int K) {

			Queue<Node> heap = new PriorityQueue<>(((o1, o2) -> o1.weight - o2.weight));
			Map<Integer, Integer>[] path = new Map[N + 1];

			for (int i = 1; i < N + 1; i++) {
				path[i] = new HashMap<>();
			}

			for (int[] edge : road) {
				path[edge[0]].put(edge[1], Math.min(path[edge[0]].getOrDefault(edge[1], edge[2]), edge[2]));
				path[edge[1]].put(edge[0], Math.min(path[edge[1]].getOrDefault(edge[0], edge[2]), edge[2]));
			}

			int[] visited = new int[N + 1];
			Arrays.fill(visited, Integer.MAX_VALUE);
			heap.add(new Node(1, 0));
			visited[1] = 0;
			while (!heap.isEmpty()) {
				Node poll = heap.poll();
				if (visited[poll.number] < poll.weight)
					continue;

				for (Map.Entry<Integer, Integer> entry : path[poll.number].entrySet()) {
					if (visited[entry.getKey()] <= visited[poll.number] + entry.getValue()) continue;

					visited[entry.getKey()] = visited[poll.number] + entry.getValue();
					heap.add(new Node(entry.getKey(), visited[poll.number] + entry.getValue()));
				}
			}
			int answer = 0;
			for (int i = 1; i < N + 1; i++) {
				if (visited[i] <= K)
					++answer;
			}
			return answer;
		}

		static class Node {
			int number;
			int weight;

			public Node(int number, int weight) {
				this.number = number;
				this.weight = weight;
			}
		}
	}

}
