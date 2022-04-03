package softeer;

import java.util.*;
import java.io.*;

public class eightLevelGearbox
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());

		boolean ascending = true;
		boolean descending = true;
		for (int i = 1; i < 9; i++) {

			int cur = Integer.parseInt(st.nextToken());

			if (cur != i)
				ascending = false;
			if (cur != 9 - i)
				descending = false;

			if (!ascending && !descending)
				break;
		}

		if (ascending)
			System.out.print("ascending");
		else if (descending)
			System.out.print("descending");
		else
			System.out.print("mixed");
	}
}