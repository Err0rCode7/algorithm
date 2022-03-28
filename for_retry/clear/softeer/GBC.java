package softeer;

import java.util.*;
import java.io.*;


public class GBC
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		Queue<int[]> rule = new LinkedList<>();
		int start = 0;
		for (int i = 0; i < n ; ++i) {
			st = new StringTokenizer(in.readLine());
			int time = Integer.parseInt(st.nextToken());
			int speed = Integer.parseInt(st.nextToken());
			rule.offer(new int[]{start, time, speed});
			start += time;
		}

		Queue<int[]> real = new LinkedList<>();
		start = 0;
		for (int i = 0; i < m; ++i) {
			st = new StringTokenizer(in.readLine());
			int time = Integer.parseInt(st.nextToken());
			int speed = Integer.parseInt(st.nextToken());
			real.offer(new int[]{start, time, speed});
			start += time;
		}
		int answer = 0;
		int[] curRule = rule.poll();
		int[] curReal = real.poll();
		for (int curTime = 0; curTime <= 100; ++curTime) {

			answer = Math.max(answer, curReal[2] - curRule[2]);

			if (curRule[0] + curRule[1] == curTime && !rule.isEmpty()) {
				curRule = rule.poll();
			}
			if (curReal[0] + curReal[1] == curTime && !real.isEmpty()) {
				curReal = real.poll();
			}
		}

		System.out.println(answer);
	}
}