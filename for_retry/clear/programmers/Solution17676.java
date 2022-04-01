package programmers;

import java.util.*;

public class Solution17676 {
	public int solution(String[] lines) {
		Queue<Integer> inQueue = new PriorityQueue<>();
		Queue<Integer> outQueue = new PriorityQueue<>();

		for (String line : lines) {
			// System.out.println(line.length());
			int hour = Integer.parseInt(line.substring(11, 13));
			int minute = Integer.parseInt(line.substring(14, 16));
			int second = Integer.parseInt(line.substring(17, 19));
			int mSecond = Integer.parseInt(line.substring(20, 23));
			int processTimeDecimal = Integer.parseInt(line.substring(24, 25));
			int processTimeUnder = 0;
			if (line.length() > 26)
				processTimeUnder = Integer.parseInt(line.substring(26, line.length() - 1));

			int end = hour * 3600;
			end += minute * 60;
			end += second;
			end = end * 1000 + mSecond;
			int start = end - (processTimeDecimal * 1000 + processTimeUnder) + 1;

			inQueue.add(start);
			outQueue.add(end);
		}
		int start = 0;
		int end = 0;
		int count = 0;
		int answer = 0;
		while (!inQueue.isEmpty()) {
			end = inQueue.poll();
			start = end - 999;
			count += 1;
			// System.out.println(start + " " + end + " " + outQueue + " " + count);
			while (!outQueue.isEmpty() && outQueue.peek() < start) {
				count -= 1;
				outQueue.poll();
			}
			// System.out.println(outQueue + " " + count);
			answer = Math.max(answer, count);
		}

		return answer;
	}
}