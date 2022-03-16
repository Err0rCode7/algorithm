package programmers;

import java.util.HashSet;
import java.util.Set;

public class Solution87377 {
	public String[] solution(int[][] line) {
		Set<long[]> set = new HashSet<>();
		long lx = Long.MAX_VALUE;
		long rx = Long.MIN_VALUE;
		long ty = Long.MIN_VALUE;
		long by = Long.MAX_VALUE;

		for (int i = 0; i < line.length; i++) {
			long A = line[i][0];
			long B = line[i][1];
			long E = line[i][2];
			for (int j = i; j < line.length; j++) {
				if (i == j) continue;

				long C = line[j][0];
				long D = line[j][1];
				long F = line[j][2];

				if ((A*D - B*C) != 0) {
					double x = (B * F - E * D) == 0 ? 0 : (double)(B * F - E * D) / (A * D - B * C);
					double y = (E * C - A * F) == 0 ? 0 : (double)(E * C - A * F) / (A * D - B * C);
					if (x - Math.floor(x) > 0 || y - Math.floor(y) > 0)
						continue;
					set.add(new long[] {(long)x, (long)y});
					ty = Math.max(ty, (long)y);
					by = Math.min(by, (long)y);
					rx = Math.max(rx, (long)x);
					lx = Math.min(lx, (long)x);
				}
			}
		}

		int ySize = (int)(ty - by + 1);
		int xSize = (int)(rx - lx + 1);
		char[][] answerChars = new char[ySize][xSize];
		for (int y = 0; y < ySize; y++) {
			for (int x = 0; x < xSize; x++) {
				answerChars[y][x] = '.';
			}
		}
		String[] answer = new String[(int)ySize];

		for (long[] pos : set) {
			int x = (int)(pos[0] - lx);
			int y = (int)(ty - pos[1]);
			answerChars[y][x] = '*';
		}

		for (int i = 0; i < ySize; i++) {
			answer[i] = String.valueOf(answerChars[i]);
		}
		return answer;
	}
}