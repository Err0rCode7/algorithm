package softeer;
import java.io.*;
import java.util.*;

public class NewGenerationCarSystem {
	static int[][] d = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
	static int[][] signDir = new int[][] {
		{},
		{1, 0, 3},
		{2, 1, 0},
		{3, 2, 1},
		{0, 3, 2},

		{1, 0},
		{2, 1},
		{3, 2},
		{0, 3},

		{0, 3},
		{1, 0},
		{2, 1},
		{3, 2}
	};
	static int n, t;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		n = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());

		int[][][] sign = new int[n][n][4];
		for (int i = 0; i < n * n; ++i) {
			st = new StringTokenizer(in.readLine());

			for (int j = 0; j < 4; ++j) {
				sign[i / n][i % n][j] = Integer.parseInt(st.nextToken());
			}
		}

		boolean[][][][] visited = new boolean[n][n][4][4]; // y, x, dir, time
		Queue<int[]> que = new LinkedList<>();
		que.add(new int[]{0, 0, 1});
		visited[0][0][1][0] = true;
		int time = 0;
		Set<Integer> resultSet = new HashSet<>();
		resultSet.add(0);
		while (time < t && !que.isEmpty()) {
			int size = que.size();
			// System.out.println(time);
			for (int i = 0; i < size; ++i) {
				int[] poll = que.poll();
				int x = poll[0];
				int y = poll[1];
				int inDir = poll[2];
				// answer = Math.max(answer, cost);
				int signValue = sign[y][x][time % 4];
				// System.out.println(x +" " + y + " " + signValue + " " + inDir);
				if (signValue % 4 != (inDir + 1) % 4)
					continue;
				// System.out.println(x +" " + y + " " + signValue);
				for (int j = 0; j < signDir[signValue].length; ++j) {
					int dir = signDir[signValue][j];

					int nx = x + d[dir][0];
					int ny = y + d[dir][1];

					if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[ny][nx][dir][time % 4])
						continue;

					visited[ny][nx][dir][time % 4] = true;
					que.add(new int[]{nx, ny, dir});
					resultSet.add(ny * n + nx);
				}
			}
			++time;
		}
		System.out.println(resultSet.size());
	}
}