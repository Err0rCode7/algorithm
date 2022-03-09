package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Solution77485 {
	public int[] solution(int rows, int columns, int[][] queries) {
		int[][] map = new int[rows][columns];
		for (int i = 0; i < rows * columns; i++) {
			map[i / columns][i % columns] = i + 1;
		}
		int[] answer = new int[queries.length];

		for (int queryIdx = 0; queryIdx < queries.length; queryIdx++) {
			int[] query = queries[queryIdx];
			int y = query[0] - 1;
			int x = query[1] - 1;

			int ty = query[2] - 1;
			int tx = query[3] - 1;

			// top
			int min = Integer.MAX_VALUE;
			min = Math.min(min, map[y][tx]);
			Queue<Integer> prev = new LinkedList<>();
			prev.add(map[y][tx]);
			for (int i = tx; i >= x + 1; i--) {
				min = Math.min(min, map[y][i - 1]);
				map[y][i] = map[y][i - 1];
			}

			// right
			min = Math.min(min, map[ty][tx]);
			prev.add(map[ty][tx]);
			for (int i = ty; i >= y + 2; i--) {
				min = Math.min(min, map[i - 1][tx]);
				map[i][tx] = map[i - 1][tx];
			}
			map[y + 1][tx] = prev.poll();

			// bottom
			min = Math.min(min, map[ty][x]);
			prev.add(map[ty][x]);
			for (int i = x; i <= tx - 2; i++) {
				min = Math.min(min, map[ty][i + 1]);
				map[ty][i] = map[ty][i + 1];
			}
			map[ty][tx - 1] = prev.poll();

			// left
			min = Math.min(min, map[y][x]);
			for (int i = y; i <= ty - 2; i++) {
				min = Math.min(min, map[i + 1][x]);
				map[i][x] = map[i + 1][x];
			}
			map[ty - 1][x] = prev.poll();

			answer[queryIdx] = min;
		}
		return answer;
	}
}
