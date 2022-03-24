package softeer;

import java.util.*;
import java.io.*;


public class StuffRecognize
{
	private static int answer;
	private static int n, k;
	private static List<int[]>[] positions;
	private static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String args[]) throws Exception
	{
		answer = Integer.MAX_VALUE;
		StringTokenizer st = new StringTokenizer(in.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		positions = new List[k + 1];
		for (int i = 1; i < k + 1; ++i) {
			positions[i] = new ArrayList<>();
		}
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(in.readLine());
			int[] position = new int[2];
			position[0] = Integer.parseInt(st.nextToken());
			position[1] = Integer.parseInt(st.nextToken());
			int color = Integer.parseInt(st.nextToken());
			positions[color].add(position);
		}
		makeComb(1, Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE);

		System.out.println(answer);
	}

	private static void makeComb(int color, int minX, int minY, int maxX, int maxY) {
		if (color == k + 1) {
			answer = Math.min(answer,
				(maxX - minX) * (maxY - minY)
			);
			return;
		}
		for(int[] position: positions[color]) {
			int x = position[0];
			int y = position[1];
			int minXNext = Math.min(minX, x);
			int minYNext = Math.min(minY, y);
			int maxXNext = Math.max(maxX, x);
			int maxYNext = Math.max(maxY, y);
			if (answer <= (maxXNext - minXNext) * (maxYNext - minYNext))
				continue;
			makeComb(color + 1, minXNext, minYNext, maxXNext, maxYNext);
		}
	}
}