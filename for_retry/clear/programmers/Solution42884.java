package programmers;

import java.util.Arrays;

public class Solution42884 {

	public int solution(int[][] routes) {

		Arrays.sort(routes, (o1, o2) -> o1[1] - o2[1]);

		int prevEnd = routes[0][1];
		int cameraCount = 1;
		for (int i = 1; i < routes.length; i++) {
			if (prevEnd >= routes[i][0]) {
				continue;
			}

			prevEnd = routes[i][1];
			cameraCount += 1;
		}

		return cameraCount;
	}
}
