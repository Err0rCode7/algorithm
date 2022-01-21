import static java.lang.Integer.*;
import java.io.*;
import java.util.*;

public class Main1981 {
	static class Main {
		final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final static BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));
		static int n, min = MAX_VALUE, max = MIN_VALUE;
		static int[][] board;
		static int[] dx = {0, 1, 0, -1};
		static int[] dy = {1, 0, -1, 0};

		public static void main(String[] args) throws IOException {
			n = parseInt(br.readLine());
			board = new int[n][n];
			for (int i = 0; i < n; i++) {
				StringTokenizer tokenizer = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					board[i][j] = parseInt(tokenizer.nextToken());
					min = min(min, board[i][j]);
					max = max(max, board[i][j]);
				}
			}

			int s = min, e = min;
			int result = max - min;
			while (s <= board[0][0] && e <= max) {
				// if (bfs(s, e)) {
				if (dfs(s, e, 0, 0, new boolean[n][n])) {
					result = min(result, e - s);
					s += 1;
				} else {
					e += 1;
				}
			}
			bw.write(Integer.toString(result));
			bw.flush();
			bw.close();
			br.close();
		}
		private static boolean dfs(int s, int e, int x, int y, boolean[][] visited) {
			if (x == n - 1 && y == n - 1) {
				return true;
			}
			visited[y][x] = true;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[ny][nx] && (board[ny][nx] >= s && board[ny][nx] <= e)) {
					if (dfs(s, e, nx, ny, visited)) return true;
				}
			}
			return false;
		}

		private static boolean bfs(int s, int e) {
			if (!(board[0][0] >= s && board[0][0] <= e))
				return false;

			boolean[][] visited = new boolean[n][n];
			Deque<Pair> deque = new LinkedList<>();
			deque.addLast(new Pair(0, 0));
			visited[0][0] = true;

			while (deque.size() > 0) {
				Pair cur = deque.pollFirst();
				for (int i = 0; i < 4; i++) {
					int nx = cur.x + dx[i];
					int ny = cur.y + dy[i];

					if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[ny][nx] && (board[ny][nx] >= s && board[ny][nx] <= e)) {
						visited[ny][nx] = true;
						deque.addLast(new Pair(nx, ny));
					}
				}
			}
			return visited[n - 1][n - 1];
		}

		private static class Pair {
			int x;
			int y;

			public Pair(int x, int y) {
				this.x = x;
				this.y = y;
			}
		}
	}

}
