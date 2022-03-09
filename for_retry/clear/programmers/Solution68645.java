package programmers;

public class Solution68645 {
	public int[] solution(int n) {

		int m = (n * (n + 1)) / 2;
		int[] answer = new int[m];
		answer[0] = 1;
		int answerIndex = 1;
		if (m == 1)
			return answer;

		int[][] map = new int[n][n];

		int count = 1;
		int[] dx = {0, 1, -1};
		int[] dy = {1, 0, -1};
		map[0][0] = 1;
		int x = 0;
		int y = 0;
		int dir = 0;
		while (count < m) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= n || map[ny][nx] != 0) {
				dir = (dir + 1) % 3;
				continue;
			}

			map[ny][nx] = ++count;
			x = nx;
			y = ny;
		}

		for (int i = 1; i < n; i++) {
			for (int j = 0; j < i + 1; j++) {
				answer[answerIndex++] = map[i][j];
			}
		}

		return answer;
	}
}