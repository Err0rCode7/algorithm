package programmers;

import java.util.*;

public class Solution86971 {
	private Set<Integer>[] graph;
	private int answer = Integer.MAX_VALUE;
	public int solution(int n, int[][] wires) {
		graph = new Set[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new HashSet<>();
		}
		for (int[] wire : wires) {
			int a = wire[0];
			int b = wire[1];

			graph[a].add(b);
			graph[b].add(a);
		}

		for (int[] wire : wires) {
			int a = wire[0];
			int b = wire[1];
			boolean[] visited = new boolean[n + 1];
			graph[a].remove(b);
			graph[b].remove(a);
			int A = dive(a, visited);
			int B = dive(b, visited);
			// System.out.println(a + " " + b);
			// System.out.println(A + " " + B + "\n");
			graph[a].add(b);
			graph[b].add(a);
			answer = Math.min(answer, Math.abs(A - B));
		}

		return answer;
	}

	private int dive(int start, boolean[] visited) {
		int result = 1; // 자신을 포함
		visited[start] = true;
		for (int next : graph[start]) {
			if (visited[next]) continue;
			result += dive(next, visited);
		}
		return result;
	}
}