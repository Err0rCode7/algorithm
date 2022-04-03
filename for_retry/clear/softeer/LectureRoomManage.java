package softeer;

import java.util.*;
import java.io.*;

// 강의실 배정
public class LectureRoomManage
{
	static int n;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(in.readLine());

		int[][] timeTable = new int[n][2];

		for (int i = 0; i < n; ++i) {
			StringTokenizer st = new StringTokenizer(in.readLine());

			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			timeTable[i][0] = start;
			timeTable[i][1] = end;
		}

		Arrays.sort(timeTable, (o1, o2) -> o1[1] - o2[1]);
		int time = timeTable[0][1];
		int lectureCount = 1;
		for (int i = 1; i < n; i++) {
			if (timeTable[i][0] < time) continue;

			time = timeTable[i][1];
			lectureCount++;
		}
		System.out.println(lectureCount);
	}
}
