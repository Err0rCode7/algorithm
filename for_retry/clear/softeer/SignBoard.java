package softeer;

import java.util.*;
import java.io.*;


// 전광판
public class SignBoard
{
	private static int[][] segments= new int[][] {
		{0, 1, 2, 3, 4, 5}, //0
		{1, 2}, // 1
		{0, 1, 3, 4, 6},
		{0, 1, 2, 3, 6},
		{1, 2, 5, 6},
		{0, 2, 3, 5, 6},
		{0, 2, 3, 4, 5, 6},
		{0, 1, 2, 5},
		{0, 1, 2, 3, 4, 5, 6},
		{0, 1, 2, 3, 5, 6}
	};
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine());


		for (int i = 0 ; i < n ; ++i) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int answer = 0;
			int digit = 10;
			for (int j = 0; j < 5; j++) {
				int a = from % digit;
				int b = to % digit;

				if (from == 0 && to == 0)
					break;
				else if (from == 0) {
					answer += segments[b].length;
					to /= 10;
					continue;
				} else if (to == 0) {
					answer += segments[a].length;
					from /= 10;
					continue;
				}
				int inter = 0;
				if (a != b) {
					int before = 0;
					for (int k = 0; k < segments[a].length; ++k)
						before += 1 << segments[a][k];
					int after = 0;
					for (int k = 0; k < segments[b].length; ++k)
						after += 1 << segments[b][k];
					int result = before & after;

					inter = Integer.bitCount(result);
					// for (int k = 0; k < segments[a].length; k++) {
					//     for (int g = 0; g < segments[b].length; g++) {
					//         if (segments[a][k] == segments[b][g]) {
					//             inter++;
					//         }
					//     }
					// }
				} else {
					inter = segments[a].length;
				}

				answer += segments[a].length - inter + segments[b].length - inter;
				from /= 10;
				to /= 10;
			}
			System.out.println(answer);
		}
	}
}