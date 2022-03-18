package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main16946_2 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m;
		static int[][] map;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static Map<Integer, Integer> cluster;

		public static void solution() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			n = parseInt(tokenizer.nextToken());
			m = parseInt(tokenizer.nextToken());

			map = new int[n][m];
			que = new LinkedList<>();
			cluster = new HashMap<>();
			for (int i = 0; i < n; i++) {
				String line = in.readLine();
				for (int j = 0; j < m; j++) {
					map[i][j] = Character.getNumericValue(line.charAt(j));
				}
			}
			int clusterCount = 2;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (map[i][j] == 0)
						bfs(j, i, clusterCount++);
				}
			}

			Set<Integer> selectedClusters = new HashSet<>();
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					int sum = 0;
					if (map[i][j] == 1) {
						sum += 1;
						for (int k = 0; k < 4; k++) {
							int nx = j + dx[k];
							int ny = i + dy[k];

							if (nx < 0 || nx >= m || ny < 0 || ny >= n || map[ny][nx] == 1 || selectedClusters.contains(map[ny][nx])) continue;
							selectedClusters.add(map[ny][nx]);
							sum += cluster.get(map[ny][nx]);
						}
					}
					selectedClusters.clear();
					out.append(Integer.toString(sum % 10));
				}
				out.append('\n');
			}
			out.flush();
			out.close();
			in.close();
		}

		private static void bfs(int x, int y, int clusterNumber) {
			Queue<int[]> bfsQ = new LinkedList<>();
			bfsQ.add(new int[] {x, y});
			que.add(bfsQ.peek());
			map[y][x] = clusterNumber;
			int count = 0;
			while (!bfsQ.isEmpty()) {
				int[] pos = bfsQ.poll();
				count += 1;
				for (int i = 0; i < 4; i++) {
					int nx = pos[0] + dx[i];
					int ny = pos[1] + dy[i];

					if (nx < 0 || nx >= m || ny < 0 || ny >= n || map[ny][nx] != 0) continue;

					map[ny][nx] = clusterNumber;
					int[] next = {nx, ny};
					bfsQ.add(next);
					que.add(next);
				}
			}
			cluster.put(clusterNumber, count);
		}
	}
}


