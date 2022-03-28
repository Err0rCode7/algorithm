package softeer;

// 좌석관리
import java.util.*;
import java.io.*;


public class SeatManage
{
	static Set<Integer> inIds = new HashSet<>();
	static Map<Integer, int[]> userMap = new HashMap<>();
	static int[][] map;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int n, m;
	static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String args[]) throws Exception
	{

		StringTokenizer st = new StringTokenizer(in.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		int q = Integer.parseInt(st.nextToken());

		map = new int[n][m];

		for(int i = 0 ;i < q; ++i) {
			st = new StringTokenizer(in.readLine());
			String cmd = st.nextToken();
			int id = Integer.parseInt(st.nextToken());
			if ("Out".equals(cmd)) {
				out(id);
			} else {
				in(id);
			}
			out.flush();
		}
		out.close();
	}

	private static void out(int id) throws Exception {
		if (inIds.contains(id)) {
			if (userMap.containsKey(id)) {
				int[] pos = userMap.remove(id);
				map[pos[0] - 1][pos[1] - 1] = 0;
				out.write(String.valueOf(id) + " ");
				out.write("leaves from the seat (");
				out.write(String.valueOf(pos[0]) + ", ");
				out.write(String.valueOf(pos[1]) + ").\n");
			} else {
				out.write(String.valueOf(id) + " ");
				out.write("already left seat.\n");
			}
		} else {
			out.write(String.valueOf(id) + " ");
			out.write("didn't eat lunch.\n");
		}
	}

	private static void in(int id) throws Exception{
		if (inIds.contains(id)) {
			if (userMap.containsKey(id)) {
				out.write(String.valueOf(id) + " ");
				out.write("already seated.\n");
			} else {
				out.write(String.valueOf(id) + " ");
				out.write("already ate lunch.\n");
			}
		} else {
			int[] seat = getSeats();
			if (seat[0] == 0 || seat[1] == 0) {
				out.write("There are no more seats.\n");
			} else {
				// System.out.println(seat[0] + " " + seat[1]);
				map[seat[0] - 1][seat[1] - 1] = 1;
				out.write(String.valueOf(id) + " ");
				out.write("gets the seat (");
				out.write(String.valueOf(seat[0]) + ", " + String.valueOf(seat[1]) + ").\n");
				userMap.put(id, seat);
				inIds.add(id);
			}
		}
	}

	private static int[] getSeats() {

		int tx = -1, ty = -1;
		int distMax = 0;
		if (userMap.keySet().size() == 0) {
			return new int[]{1, 1};
		}
		for (int y = 0; y < n; ++y) {
			for (int x = 0; x < m; ++x) {
				if (map[y][x] != 0) continue;
				boolean possible = true;
				for (int k = 0; k < 4; k++) {
					int nx = x + dx[k];
					int ny = y + dy[k];

					if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;

					if (map[ny][nx] != 0) {
						possible = false;
						break;
					}
				}
				if (!possible)
					continue;
				int distMin = Integer.MAX_VALUE;
				int nx = -1, ny = -1;
				for (int[] value : userMap.values()) { // y, x
					int dist = (int)(Math.pow((double)value[1] - x - 1, 2) + Math.pow((double)value[0] - y - 1, 2));
					// System.out.println(x + " " + y + " " + dist);
					// System.out.println(value[] + " " + y + " " + dist);
					if (dist < distMin) {
						nx = x;
						ny = y;
						distMin = dist;
					}
				}
				// System.out.println(nx + " " + ny + " " + distMin);

				if (distMax < distMin) {
					tx = nx;
					ty = ny;
					distMax = distMin;
				}
			}
		}
		return new int[] {ty + 1, tx + 1};
	}
}