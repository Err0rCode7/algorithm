package softeer;

import java.util.*;
import java.io.*;


public class WinterTestTimePrediction
{
	static char[][] map;
	static int[][] contactCount;
	static int n, m;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		map = new char[n][m];

		Queue<Integer> meltedIce = new LinkedList<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(in.readLine(), " ");

			for (int j = 0; j < m; j++) {
				String test = st.nextToken();
				map[i][j] = test.charAt(0);
			}
		}

		Queue<Integer> removedIce = new LinkedList<>();
		dfs(0, 0, removedIce, new int[n][m]);
		int time = 0;
		while (!removedIce.isEmpty()) {
			time += 1;
			while(!removedIce.isEmpty()) {
				int node = removedIce.poll();
				int x = node % m;
				int y = node / m;
				// System.out.println(x + " " + y);
				map[y][x] = '0';
			}

			dfs(0, 0, removedIce, new int[n][m]);
		}
		System.out.println(time);
	}

	private static void dfs(int x, int y, Queue<Integer> removedIce, int[][] visited) {
		visited[y][x] = 1;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
			if (map[ny][nx] == '1' && visited[ny][nx] < 2) {
				visited[ny][nx] += 1;
				if (visited[ny][nx] > 1) {
					map[ny][nx] = 'C';
					removedIce.add(ny * m + nx);
				}
			} else if (map[ny][nx] == '0' && visited[ny][nx] == 0) {
				dfs(nx, ny, removedIce, visited);
			}
		}
	}
}
