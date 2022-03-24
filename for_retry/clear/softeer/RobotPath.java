package softeer;

import java.util.*;
import java.io.*;


public class RobotPath
{
	private static List<char[]> map;
	private static int[] dx;
	private static int[] dy;
	private static int h, w;
	private static int count;
	private static String answer;
	public static void main(String args[]) throws Exception
	{
		answer = "";
		dx = new int[]{1, 0, -1, 0};
		dy = new int[]{0, 1, 0, -1};
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		h = Integer.parseInt(st.nextToken());
		w = Integer.parseInt(st.nextToken());
		map = new ArrayList<>();

		count = 0;
		for (int i = 0; i < h; ++i) {
			String s = in.readLine();
			map.add(s.toCharArray());
			for (int j = 0; j < w; ++j) {
				if (s.charAt(j) == '#')
					++count;
			}
		}
		int ax = 0;
		int ay = 0;
		int dir = 0;
		boolean[][][] visited = new boolean[h][w][4];
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				if (map.get(i)[j] != '#') continue;
				for (int k = 0; k < 4; ++k) {
					int size = answer.length();
					visited[i][j][k] = true;
					dfs(j, i, k, 1, "", visited);
					visited[i][j][k] = false;

					if (size != answer.length()) {
						ax = j;
						ay = i;
						dir = k;
					}
				}
			}
		}
		char[] dirs = {'>', 'v', '<', '^'};
		System.out.println((ay + 1) + " " + (ax + 1));
		System.out.println(dirs[dir]);
		System.out.println(answer);

	}

	private static void dfs(int x, int y, int dir, int count, String result, boolean[][][] visited) {
		if (count == RobotPath.count) {
			if (answer.length() == 0 || answer.length() > result.length()) {
				answer = result;
			}
			return;
		}

		if (answer.length() != 0 && result.length() >= answer.length())
			return;
		char pre = map.get(y)[x];
		map.get(y)[x] = '.';
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			int nny = ny + dy[i];
			int nnx = nx + dx[i];
			if (!isSafe(nx, ny) || !isSafe(nnx, nny) || visited[nny][nnx][i]) continue;
			if (map.get(ny)[nx] != '#' || map.get(nny)[nnx] != '#')
				continue;
			visited[nny][nnx][i] = true;
			StringBuilder sb = new StringBuilder();
			if (i == dir) {
				// 직진
				sb.append("A");
			} else if (Math.abs(dir - i) == 2) {
				// 두번 회전
				sb.append("LLA");

			} else if ((dir + 1) % 4 == i) {
				// 오른쪽 한번 회전
				sb.append("RA");
			} else {
				// 왼쪽 한번 회전
				sb.append("LA");
			}

			map.get(ny)[nx] = '.';
			map.get(nny)[nnx] = '.';
			dfs(nnx, nny, i, count + 2, result + sb.toString(), visited);
			map.get(ny)[nx] = '#';
			map.get(nny)[nnx] = '#';
			visited[nny][nnx][i] = false;
		}
		map.get(y)[x] = pre;
	}

	private static boolean isSafe(int x, int y) {
		return (x < w && x >= 0 && y < h && y >= 0);
	}
}