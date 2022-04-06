package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

public class Solution49189 {
	private static List<Integer>[] graph;
	private static int max;
	private static Set<Integer> selectedNodes;

	public int solution(int n, int[][] edge) {
		graph = new List[n + 1];
		for (int i = 0; i < graph.length; i++) {
			graph[i] = new ArrayList<>();
		}
		for (int i = 0; i < edge.length; i++) {
			int a = edge[i][0];
			int b = edge[i][1];
			graph[a].add(b);
			graph[b].add(a);
		}

		int[] cost = new int[n + 1];
		max = 0;
		selectedNodes = new HashSet<>();
		Arrays.fill(cost, Integer.MAX_VALUE);
		dfs(1, 0, cost);

		int max = 0;
		int count = 0;
		for (int i = 2; i < n + 1; i++) {
			if (cost[i] == Integer.MAX_VALUE)
				continue;
			if (max < cost[i]) {
				count = 1;
				max = cost[i];
			} else if (max == cost[i]) {
				count += 1;
			}
		}
		return count;
	}
	public void dfs(int start, int costSum, int[] cost) {

		for (Integer next : graph[start]) {
			if (costSum + 1 >= cost[next])
				continue;

			cost[next] = costSum + 1;
			dfs(next, costSum + 1, cost);
		}
	}

	/**
	 * que with depth
	 */

	static class Solution_2 {
		private static List<Integer>[] graph;
		private static int max;
		private static Set<Integer> selectedNodes;

		public int solution(int n, int[][] edge) {

			boolean[] visited = new boolean[n + 1];
			Queue<Integer> que = new LinkedList<>();

			List<Integer>[] graph = new List[n + 1];
			for (int i = 1; i < n + 1; i++) {
				graph[i] = new ArrayList<>();
			}

			for (int[] e : edge) {
				graph[e[0]].add(e[1]);
				graph[e[1]].add(e[0]);
			}

			que.add(1);
			visited[1] = true;
			int answer = 0;
			while (!que.isEmpty()) {
				int count = 0;
				int size = que.size();
				for (int i = 0; i < size; i++) {
					Integer cur = que.poll();
					for (Integer next : graph[cur]) {
						if (visited[next]) continue;

						count += 1;
						visited[next] = true;
						que.add(next);
					}
					System.out.println();
				}
				if (count > 0)
					answer = count;
			}

			return answer;
		}
	}
}