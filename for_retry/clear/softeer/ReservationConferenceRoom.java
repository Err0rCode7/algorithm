package softeer;

import java.util.*;
import java.io.*;


public class ReservationConferenceRoom
{
	private static int n, m;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(in.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		String[] room = new String[n];
		Map<String, boolean[]> reservationTableMap = new HashMap<>();
		for (int i = 0; i < n; i++) {
			room[i] = in.readLine();
			reservationTableMap.put(room[i], new boolean[10]); // 09 ~ 18
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(in.readLine());
			String roomName = st.nextToken();
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());

			boolean[] resvationTable = reservationTableMap.get(roomName);
			for (int time = start - 9; time < end - 9; time++) { // end는 비움
				resvationTable[time] = true;
			}
		}

		Arrays.sort(room);
		for (int i = 0; i < room.length; i++) {
			String roomName = room[i];
			out.write("Room ");
			out.write(roomName);
			out.write(":\n");
			boolean[] resvationTable = reservationTableMap.get(roomName);

			int count = 0;
			int start = 0;
			List<int[]> outputList = new ArrayList<>();
			// System.out.println(Arrays.toString(resvationTable));
			for (int time = 0; time < 9; time++) {

				if (!resvationTable[time]) {
					if (count == 0)
						start = time;
					count++;
				} else if (count > 0){
					outputList.add(new int[]{start, count});
					count = 0;
				}
			}
			if (count > 0) {
				outputList.add(new int[]{start, count});
			}

			if (outputList.size() == 0)
				out.write("Not available\n");
			else
				out.write(String.valueOf(outputList.size()) + " available:\n");
			for (int[] outputInfo : outputList) {
				start = outputInfo[0];
				count = outputInfo[1];
				if (start == 0)
					out.write("0");
				out.write(String.valueOf(start + 9) + "-");
				out.write(String.valueOf(start + count + 9) + "\n");
			}


			if (i + 1 != room.length)
				out.write("-----\n");
		}
		out.flush();
	}
}