package programmers;

import java.util.Arrays;

class Solution42861 {
	private static int[] root;
	public int solution(int n, int[][] costs) {
		root = new int[n];

		for (int i = 0; i < n; i++) {
			root[i] = i;
		}

		Arrays.sort(costs, ((o1, o2) -> o1[2] - o2[2]));
		int answer = 0;
		for (int i = 0; i < costs.length; i++) {
			int a = costs[i][0];
			int b = costs[i][1];
			int cost = costs[i][2];

			if (union(a, b)) {
				answer += cost;
			}
		}
		return answer;
	}

	public boolean union(int a, int b) {
		int rootA = findRoot(a);
		int rootB = findRoot(b);
		if (rootA == rootB)
			return false;

		if (rootA < rootB) {
			root[rootB] = rootA;
		} else {
			root[rootA] = rootB;
		}
		return true;
	}

	public int findRoot(int n) {
		if (root[n] == n)
			return n;
		return root[n] = findRoot(root[n]);
	}
}
