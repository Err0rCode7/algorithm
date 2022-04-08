package programmers;

public class Solution87391 {
	public long solution(int n, int m, int x, int y, int[][] queries) {

		long sx = y;
		long sy = x;
		long ex = y;
		long ey = x;
		for (int i = queries.length - 1; i >= 0; i--) {
			long dir = (long)queries[i][0];
			long dist = (long)queries[i][1];
			if (dir == 0) {
				// x 감소
				if (sx != 0) {
					sx = sx + dist;
					if (sx > m - 1)
						return (0);
				}
				ex = ex + dist >= m ? m - 1 : ex + dist;
			} else if (dir == 1) {
				// x 증가
				if (ex != m - 1) {
					ex = ex - dist;
					if (ex < 0)
						return (0);
				}
				sx = sx - dist < 0 ? 0 : sx - dist;

			} else if (dir == 2) {
				// y 감소
				if (sy != 0) {
					sy = sy + dist >= n ? n - 1 : sy + dist;
					if (sy > n - 1)
						return (0);
				}
				ey = ey + dist >= n ? n - 1 : ey + dist;
			} else if (dir == 3) {
				// y 증가
				if (ey != n - 1) {
					ey = ey - dist;
					if (ey < 0)
						return(0);
				}
				sy = sy - dist < 0 ? 0 : sy - dist;

			}
		}

		long answer = (ex - sx + 1) * (ey - sy + 1);
		return answer;
	}
}