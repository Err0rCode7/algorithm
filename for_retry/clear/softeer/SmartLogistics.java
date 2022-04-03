package softeer;

import java.util.*;
import java.io.*;

public class SmartLogistics
{
	static int n, k;
	static String stuff;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String[] line = in.readLine().split(" ");
		n = Integer.parseInt(line[0]);
		k = Integer.parseInt(line[1]);
		stuff = in.readLine();

		Queue<Integer> robotQ = new LinkedList<>();
		Queue<Integer> stuffQ = new LinkedList<>();

		for (int i = 0; i < n; i++) {
			if (stuff.charAt(i) == 'H') {
				stuffQ.add(i);
			} else {
				robotQ.add(i);
			}
		}

		// int stuffCount = stuffQ.size();
		int stuffCount = 0;
		while (!robotQ.isEmpty() && !stuffQ.isEmpty()) {
			int robot = robotQ.poll();
			// System.out.println("robot: " + robot);
			while (!stuffQ.isEmpty() && robot - stuffQ.peek() > k) {
				stuffQ.poll();
			}
			if (stuffQ.isEmpty())
				break;
			if (stuffQ.peek() - robot > k)
				continue;
			stuffQ.poll();
			// System.out.println("stuff: " + stuffQ.poll());
			stuffCount++;
		}
		System.out.println(stuffCount);
	}
}