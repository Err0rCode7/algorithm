package boj;

import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main2186 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
		static String[] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static List<List<Integer>> dp;
		public static void solution() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			n = parseInt(tokenizer.nextToken());
			m = parseInt(tokenizer.nextToken());
			k = parseInt(tokenizer.nextToken());
			map = new String[n];
			for (int i = 0; i < n; i++) {
				String line = in.readLine();
				map[i] = line;
			}
			target = in.readLine();

			dp = new ArrayList<>();
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (map[i].charAt(j) == target.charAt(0))
						dfs(0, j, i, new ArrayList<>());
				}
			}
			System.out.println(dp.size());
		}

		public static void dfs(int size, int x, int y, List<Integer> curPath) {
			curPath.add(y * m + x);
			for (List<Integer> cache : dp) {
				if (cache.size() < curPath.size())
					continue;
				boolean hit = true;
				for (int i = 0; i < curPath.size(); i++) {
					if (cache.get(i) != curPath.get(i)) {
						hit = false;
						continue;
					}
				}
				if (hit) return;
			}

			if (size == target.length() - 1) {
				if (target.charAt(size) == map[y].charAt(x))
					dp.add(List.copyOf(curPath));
				return;
			}

			for (int i = 0; i < 4; i++) {
				int nx = x;
				int ny = y;
				for (int j = 0; j < k; j++) {
					nx = nx + dx[i];
					ny = ny + dy[i];
					if (nx < 0 || nx >= m || ny < 0 || ny >= n) break;

					if (map[ny].charAt(nx) == target.charAt(size + 1)) {
						dfs(size + 1, nx, ny, curPath);
					}
				}
			}
		}
	}
}
