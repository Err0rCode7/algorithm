package programmers;

import java.util.*;

public class Solution43162 {
	public static boolean[] visited;
	public int solution(int n, int[][] computers) {
		visited = new boolean[n];

		int answer = 0;
		Queue<Integer> que = new LinkedList<>();
		for (int i = 0; i < n; i++) {
			if (visited[i])
				continue;
			answer += 1;
			que.add(i);
			bfs(n, computers, que);
		}

		return answer;
	}

	public void bfs(int n, int[][] computer, Queue<Integer> que) {
		while (!que.isEmpty()) {
			Integer cur = que.poll();

			for (int i = 0; i < n; i++) {
				if (computer[cur][i] == 0 || visited[i])
					continue;

				visited[i] = true;
				que.add(i);
			}
		}
	}
}