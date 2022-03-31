package softeer;

//징검다리
import java.util.*;
import java.io.*;


public class JumpBridge
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine());
		StringTokenizer st = new StringTokenizer(in.readLine());

		// int[] stones = new int[n];
		int[] count = new int[n];
		List<Integer> searchTable = new ArrayList<>();
		List<Integer> searchTableCount = new ArrayList<>();
		int answer = 0;
		for (int i = 0; i < n; ++i) {
			int stone = Integer.parseInt(st.nextToken());
			// stones[i] = Integer.parseInt(st.nextToken());

			int idx = binarySearch(stone, searchTable);
			// System.out.println(stone + " " + idx);
			if (idx >= searchTable.size()) {
				count[i] = idx > 0 ? searchTableCount.get(idx - 1) + 1: 1;
				searchTable.add(stone);
				searchTableCount.add(count[i]);

				answer = Math.max(answer, count[i]);
			} else {
				searchTable.set(idx, stone);
				count[i] = searchTableCount.get(idx);
			}
		}
		System.out.println(answer);
	}

	private static int binarySearch(int target, List<Integer> list) {
		int s = 0;
		int e = list.size();

		while (s < e) {
			int m = (s + e) / 2;

			if (list.get(m) >= target) {
				e = m;
			} else {
				s = m + 1;
			}
		}
		return e;
	}
}