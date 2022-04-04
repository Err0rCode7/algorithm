package softeer;

import java.util.*;
import java.io.*;


public class ObstacleRecognitionProgram
{
	static int n;
	static String[] map;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(in.readLine());
		map = new String[n];

		for (int i = 0; i < n; i++) {
			map[i] = in.readLine();
		}

		boolean[][] visited = new boolean[n][n];
		List<Integer> blockCounts = new ArrayList<>();
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				if (visited[y][x]) continue;
				if (map[y].charAt(x) == '0') continue;

				blockCounts.add(dfs(x, y, visited));
			}
		}

		Collections.sort(blockCounts, (o1, o2) -> o1 - o2);

		out.write(String.valueOf(blockCounts.size()) + "\n");
		for (int count : blockCounts) {
			out.write(String.valueOf(count) + "\n");
		}
		out.flush();
	}

	private static int dfs(int x, int y, boolean[][] visited) {
		visited[y][x] = true;
		int result = 1;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[ny][nx] || map[ny].charAt(nx) == '0') continue;

			result += dfs(nx, ny, visited);
		}
		return result;
	}
}