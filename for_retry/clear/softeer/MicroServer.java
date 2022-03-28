package softeer;

import java.util.*;
import java.io.*;


public class MicroServer
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		int t = Integer.parseInt(in.readLine());
		int[] volumes;
		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(in.readLine());
			StringTokenizer st = new StringTokenizer(in.readLine());

			volumes = new int[n];
			for (int j = 0; j < n ; ++j) {
				volumes[j] = Integer.parseInt(st.nextToken());
			}

			Arrays.sort(volumes);

			int s = 0, e = volumes.length - 1;

			while (s <= e && volumes[s] == 300) {
				s++;
			}
			int size300 = s;
			int count = 0;
			while (s <= e) {
				count++;
				if (volumes[e] > 600) {
					e--;
					continue;
				}
				if (s != e && volumes[e] + volumes[s] <= 900) {
					s++;
				} else if (size300 > 0) {
					size300--;
				}
				e--;

			}
			count += (size300 + 2) / 3;

			out.write(String.valueOf(count));
			out.write("\n");
		}
		out.flush();
	}
}