package programmers;

import java.util.*;

public class Solution17687 {
	public String solution(int n, int t, int m, String[] timetable) throws Exception{

		PriorityQueue<Integer> crewQueue = new PriorityQueue<>();
		for (int i = 0; i < timetable.length; i++) {
			StringTokenizer st = new StringTokenizer(timetable[i], ":");
			int hour = Integer.parseInt(st.nextToken());
			int minute = Integer.parseInt(st.nextToken());
			crewQueue.add(hour * 60 + minute);
		}

		int count = 0;
		int time = 9 * 60;
		int lastCrewTime = 0;

		while (!crewQueue.isEmpty() && count < n) {
			int crewCount = 0;
			while (!crewQueue.isEmpty() && crewQueue.peek() <= time && crewCount < m) {
				crewCount++;
				lastCrewTime = crewQueue.poll();
			}
			if (crewCount < m)
				lastCrewTime = time;
			else
				lastCrewTime -= 1;

			time += t;
			count++;
		}

		String hour = lastCrewTime / 60 < 10 ? "0" + String.valueOf(lastCrewTime / 60) : String.valueOf(lastCrewTime / 60);
		String minute = lastCrewTime % 60 < 10 ? "0" + String.valueOf(lastCrewTime % 60) : String.valueOf(lastCrewTime % 60);

		return hour + ":" + minute;
	}
}