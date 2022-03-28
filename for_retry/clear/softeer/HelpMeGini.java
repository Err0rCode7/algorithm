package softeer;


import java.util.*;
import java.io.*;

public class HelpMeGini
{
	private static int[] dx = {1, 0, -1, 0};
	private static int[] dy = {0, 1, 0, -1};
	private static int r, c;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());

		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());

		List<char[]> map = new ArrayList<>(r);
		int[] start = new int[2];
		int[] end = new int[2];
		Queue<int[]> rainPosQue = new LinkedList<>();
		for (int i = 0; i < r; ++i) {
			char[] line = in.readLine().toCharArray();
			map.add(line);

			for (int j = 0; j < c; ++j) {
				if (line[j] == 'H') {
					end[0] = j;
					end[1] = i;
					line[j] = '.';
				} else if (line[j] == 'W') {
					start[0] = j;
					start[1] = i;
					line[j] = '.';
				} else if (line[j] == '*') {
					rainPosQue.add(new int[] {j, i});
				}
			}
		}


		boolean[][] visited = new boolean[r][c];
		Queue<int[]> carQue = new LinkedList<>();
		carQue.add(new int[]{start[0], start[1]});
		visited[start[1]][start[0]] = true;
		boolean success = false;
		int count = 0;
		while (!carQue.isEmpty()) {
			int size;

			size = rainPosQue.size();
			// System.out.println(rainPosQue);
			for (int a = 0; a < size; a++) {
				int[] rain = rainPosQue.poll();

				for (int i = 0; i < 4; i++) {
					int nx = rain[0] + dx[i];
					int ny = rain[1] + dy[i];

					if (nx < 0 || ny < 0 || nx >= c || ny >= r) continue;
					if (ny == end[1] && nx == end[0]) continue;
					if (map.get(ny)[nx] == '.') {
						map.get(ny)[nx] = '*';
						rainPosQue.add(new int[]{nx, ny});
					}
				}
			}

			size = carQue.size();
			for (int a = 0; a < size; a++) {
				int[] car = carQue.poll();

				if (car[0] == end[0] && car[1] == end[1]) {
					success = true;
					break;
				}

				// if (map.get(car[1])[car[0]] == '*')
				//     continue;

				for (int i = 0; i < 4; i++) {
					int nx = car[0] + dx[i];
					int ny = car[1] + dy[i];

					if (nx < 0 || ny < 0 || nx >= c || ny >= r || visited[ny][nx]) continue;
					if (map.get(ny)[nx] == '.') {
						visited[ny][nx] = true;
						carQue.add(new int[]{nx, ny});
					}
				}
			}

			if (success)
				break;


			count++;
		}

		if (success)
			System.out.println(count);
		else
			System.out.println("FAIL");
	}
}
