import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main1981 {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		int[][] board = new int[n][n];

		for (int i = 0 ; i < n; ++i){
			StringTokenizer tokenizer = new StringTokenizer(br.readLine());
			for (int j=0; j<n; ++j) {
				board[i][j] = Integer.parseInt(tokenizer.nextToken());
			}
		}
		bw.write(solution(board, n));
		bw.flush();
	}

	static int solution(int[][] board, int n) {
		int min, max;
		if (board[0][0] > board[n - 1][n - 1]) {
			min = board[n - 1][n - 1];
			max = board[0][0];
		} else {
			max = board[n - 1][n - 1];
			min = board[0][0];
		}
		Node[][] visited = new Node[n][n];
		for (int i = 0 ; i < n; ++i){
			for (int j=0; j<n; ++j) {
				visited[i][j] = new Node(-1, -1);
			}
		}
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};

		Deque<Pair> que = new LinkedList<>();
		que.add(new Pair(0, 0));
		visited[0][0].min = min;
		visited[0][0].max = max;
		int result = 200 - 0;
		while (que.size() > 0) {
			Pair pair = que.poll();
			int x = pair.x, y = pair.y;
			System.out.println(x + " " + y + " " + visited[y][x].min + " " + visited[y][x].max);
			for (int i = 0; i < 4; ++i) {
				int nx = pair.x + dx[i];
				int ny = pair.y + dy[i];

				if (!(0 <= nx && nx < n && 0 <= ny && ny < n))
					continue;
				int left, right;
				boolean over = false;
				if (visited[y][x].min < board[ny][nx])
					left = visited[y][x].min;
				else
					left = board[ny][nx];
				if (visited[y][x].max > board[ny][nx])
					right = visited[y][x].max;
				else
					right = board[ny][nx];


				if (visited[ny][nx].min != -1 && visited[ny][nx].max != -1) {
					if (visited[ny][nx].min >= left && visited[ny][nx].max <= right)
						continue;
				}
				visited[ny][nx].min = left;
				visited[ny][nx].max = right;
				if (ny == n - 1 && nx == n - 1) {
					result = Integer.min(result, visited[ny][nx].getSpectrum());
					continue;
				}
				que.add(new Pair(nx, ny));
			}
		}
		System.out.println(visited[n - 1][n - 1].min);
		System.out.println(visited[n - 1][n - 1].max);
		return visited[n - 1][n - 1].getSpectrum();
	}

	static class Pair {
		int x;
		int y;

		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	static class Node {
		int min;
		int max;

		public Node(int min, int max) {
			this.min = min;
			this.max = max;
		}

		public int getSpectrum(){
			return this.max - this.min;
		}
	}
}
