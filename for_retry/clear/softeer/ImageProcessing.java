package softeer;

import java.util.*;
import java.io.*;


public class ImageProcessing
{

	private static int[] dx = {1, 0, -1, 0};
	private static int[] dy = {0, 1, 0, -1};
	private static int h, w;
	private static int[][] img;
	private static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	private static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String args[]) throws Exception
	{


		StringTokenizer st = new StringTokenizer(in.readLine());
		h = Integer.parseInt(st.nextToken());
		w = Integer.parseInt(st.nextToken());

		img = new int[h][w];
		for (int i = 0; i < h; ++i) {
			st = new StringTokenizer(in.readLine());

			for (int j = 0; j < w; j++) {
				img[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int q = Integer.parseInt(in.readLine());

		for (int i = 0; i < q; ++i) {
			st = new StringTokenizer(in.readLine());
			int y = Integer.parseInt(st.nextToken()) - 1;
			int x = Integer.parseInt(st.nextToken()) - 1;
			int changedImg = Integer.parseInt(st.nextToken());


			dfs(x, y, new boolean[h][w], img[y][x], changedImg);

		}
		print();
		out.flush();

	}

	private static void print() throws Exception {
		for (int y = 0; y < h; ++y){
			for (int x = 0; x < w; ++x) {
				out.write(String.valueOf(img[y][x]));
				if (x + 1 != w)
					out.write(" ");
			}
			out.write("\n");
		}
	}

	private static void dfs(int x, int y, boolean[][] visited, int cur, int target) {
		visited[y][x] = true;
		img[y][x] = target;
		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || ny < 0 || nx >= w || ny >= h || visited[ny][nx]) continue;
			if (img[ny][nx] != cur) continue;

			dfs(nx, ny, visited, cur, target);
		}
	}
}