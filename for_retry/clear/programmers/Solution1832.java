package programmers;

import java.util.*;

public class Solution1832 {
	int MOD = 20170805;
	private int[] dx = new int[] {1, 0};
	private int[] dy = new int[] {0, 1};
	public int solution(int m, int n, int[][] cityMap) {

		if (m == 1 && n == 1)
			return 1;
		int[][][] visitCount = new int[m][n][2];
		Queue<Visit> que = new LinkedList<>();
		que.add(new Visit(0, 0, -1));

		while (!que.isEmpty()) {
			Visit poll = que.poll();

			if (poll.y == m - 1 && poll.x == n - 1)
				continue;

			int count = (poll.dir == -1) ? 1 : visitCount[poll.y][poll.x][poll.dir];

			for (int i = 0; i < 2; i++) {
				int nx = poll.x + dx[i];
				int ny = poll.y + dy[i];

				if (isNotSafeIdx(m, n, nx, ny) || cityMap[ny][nx] == 1) continue;
				if (cityMap[poll.y][poll.x] == 2 && poll.dir != i && poll.dir != -1) continue;
				if (visitCount[ny][nx][i] == 0) {
					que.add(new Visit(nx, ny, i));
				}

				visitCount[ny][nx][i] = (visitCount[ny][nx][i] + count) % MOD;
			}
		}
		int answer = 0;
		for (int i = 0; i < 2; i++) {
			answer = (answer + visitCount[m - 1][n - 1][i]) % MOD;
		}
		return answer;
	}

	private boolean isNotSafeIdx(int m, int n, int nx, int ny) {
		return nx < 0 || nx >= n || ny >= m || ny < 0;
	}

	private static class Visit {
		int x;
		int y;
		int dir;

		public Visit(int x, int y, int dir) {
			this.x = x;
			this.y = y;
			this.dir = dir;
		}
	}
}

// class Solution {
// 	public int solution(int m, int n, int[][] cityMap) {
// 		if (m == 1 && n == 1)
// 			return 1;
// 		int[][][] dp = new int[m + 1][n + 1][2];
//
// 		dp[1][1][0] = 1;
// 		dp[1][1][1] = 1;
//
// 		for (int y = 1; y < m + 1; y++) {
// 			for (int x = 1; x < n + 1; x++) {
// 				if (cityMap[y - 1][x - 1] == 1) continue;
// 				if (cityMap[y - 1][x - 1] == 2) {
// 					dp[y][x][0] = (dp[y][x][0] + dp[y][x - 1][0]) % 20170805;
// 					dp[y][x][1] = (dp[y][x][1] + dp[y - 1][x][1]) % 20170805;
// 				} else {
// 					dp[y][x][0] = (dp[y][x][0] + dp[y][x - 1][0]) % 20170805;
// 					dp[y][x][0] = (dp[y][x][0] + dp[y - 1][x][1]) % 20170805;
// 					dp[y][x][1] = (dp[y][x][1] + dp[y][x - 1][0]) % 20170805;
// 					dp[y][x][1] = (dp[y][x][1] + dp[y - 1][x][1]) % 20170805;
// 				}
//
// 			}
// 		}
// 		return (dp[m][n - 1][0] + dp[m - 1][n][1]) % 20170805;
// 	}
// }


// class Solution {
// 	int MOD = 20170805;
// 	private static int[] dx;
// 	private static int[] dy;
// 	public int solution(int m, int n, int[][] cityMap) {
//
// 		dx = new int[] {1, 0};
// 		dy = new int[] {0, 1};
// 		int[][][] cost = new int[m][n][4];
// 		int[][][] visitCount = new int[m][n][4];
// 		Queue<Visit> que = new LinkedList<>();
// 		que.add(new Visit(0, 0, -1, 0, 1));
//
// 		for (int i = 0; i < m; i++) {
// 			for (int j = 0; j < n; j++) {
// 				Arrays.fill(cost[i][j], Integer.MAX_VALUE);
// 			}
// 		}
//
// 		Arrays.fill(cost[0][0], 0);
// 		visitCount[0][0][0] = 1;
// 		while (!que.isEmpty()) {
// 			Visit poll = que.poll();
//
// 			if (poll.y == m - 1 && poll.x == n - 1)
// 				continue;
//
// 			// 이 부분이 문제가 되는 부분
// 			// 아래 처럼 수정해야함
// 			// poll.count = (poll.dir == -1) ? 1 : visitCount[poll.y][poll.x][poll.dir];
// 			if (poll.dir != -1 && visitCount[poll.y][poll.x][poll.dir] > poll.count) {
// 				poll.count = visitCount[poll.y][poll.x][poll.dir];
// 			}
//
// 			for (int i = 0; i < 2; i++) {
// 				int nx = poll.x + dx[i];
// 				int ny = poll.y + dy[i];
//
// 				if (isNotSafeIdx(m, n, nx, ny) || cityMap[ny][nx] == 1) continue;
// 				if (cityMap[poll.y][poll.x] == 2 && poll.dir != i && poll.dir != -1) continue;
// 				if (cost[ny][nx][i] < poll.cost + 1) continue;
// 				else if (cost[ny][nx][i] == poll.cost + 1) {
// 					visitCount[ny][nx][i] = (visitCount[ny][nx][i] + poll.count) % MOD;
// 					continue;
// 				}
// 				cost[ny][nx][i] = poll.cost + 1;
// 				visitCount[ny][nx][i] = poll.count;
// 				que.add(new Visit(nx, ny, i, poll.cost + 1, poll.count));
// 			}
// 		}
// 		int answer = 0;
// 		for (int i = 0; i < 4; i++) {
// 			answer = (answer + visitCount[m - 1][n - 1][i]) % MOD;
// 		}
// 		return answer;
// 	}
//
// 	private boolean isNotSafeIdx(int m, int n, int nx, int ny) {
// 		return nx < 0 || nx >= n || ny >= m || ny < 0;
// 	}
//
// 	private static class Visit {
// 		int x;
// 		int y;
// 		int dir;
// 		int cost;
// 		int count;
//
// 		public Visit(int x, int y, int dir, int cost, int count) {
// 			this.x = x;
// 			this.y = y;
// 			this.dir = dir;
// 			this.cost = cost;
// 			this.count = count;
// 		}
// 	}
// }