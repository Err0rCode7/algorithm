package softeer;

import java.util.*;
import java.io.*;


// 금고 털이
public class GemSteal
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());

		int weight = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());

		List<int[]> gems = new ArrayList<>();
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(in.readLine());
			int w = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			gems.add(new int[]{w, v});
		}

		Collections.sort(gems, (o1, o2) -> o2[1] - o1[1]);

		int money = 0;
		for (int[] gem : gems){
			int volume = gem[0];
			int value = gem[1];
			// System.out.println(volume + " " + value);
			if (weight > volume) {
				weight -= volume;
				money += value * volume;
			} else {
				money += value * weight;
				break;
			}
		}

		System.out.println(money);
	}
}