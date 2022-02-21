package programmers;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class Main76503 {
	public void main(String[] args) {
		Solution solution = new Solution();
		long result;
		result = solution.solution(new int[] {-5, 0, 2, 1, 2}, new int[][] {{0, 1}, {3, 4}, {2, 3}, {0, 3}});
		System.out.println(result);
		result = solution.solution(new int[] {0, 1, 0}, new int[][] {{0, 1}, {1, 2}});
		System.out.println(result);
	}
	class Solution {
		public long solution(int[] a, int[][] edges) {

			Set<Integer>[] graph = new HashSet[a.length];
			for (int i = 0; i < a.length; i++) {
				graph[i] = new HashSet<>();
			}
			for (int i = 0; i < edges.length; i++) {
				int s = edges[i][0];
				int e = edges[i][1];
				graph[s].add(e);
				graph[e].add(s);
			}
			Queue<Integer> que = new LinkedList<>();
			long[] longA = new long[a.length];
			for (int i = 0; i < a.length; i++) {
				if (graph[i].size() == 1) {
					que.add(i);
				}
				longA[i] = a[i];
			}
			long answer = 0;
			while (!que.isEmpty()) {
				Integer cur = que.poll();
				if (graph[cur].size() == 0)
					continue;
				Integer removed = graph[cur].iterator().next();
				graph[cur].remove(removed);
				graph[removed].remove(cur);

				long weight = Math.abs(longA[cur]);
				if (longA[cur] > 0) {
					longA[removed] += weight;
				} else {
					longA[removed] -= weight;
				}
				longA[cur] = 0;
				answer += weight;

				if (graph[removed].size() == 1) {
					que.add(removed);
				}
			}

			for (int i = 0; i < longA.length; i++) {
				if (longA[i] != 0) {
					return -1;
				}
			}

			return answer;
		}
	}
}
