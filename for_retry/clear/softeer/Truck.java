package softeer;

import java.util.*;
import java.io.*;

public class Truck {
	private static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	private static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String args[]) throws Exception {

		int n = Integer.parseInt(in.readLine());

		List<int[]> buyerProposals = new ArrayList<>();

		for (int i = 0; i < n ; i++) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			int size = Integer.parseInt(st.nextToken());
			for (int j = 0; j < size; j++) {
				int[] proposal = new int[3];
				proposal[0] = Integer.parseInt(st.nextToken());
				proposal[1] = Integer.parseInt(st.nextToken());
				proposal[2] = i;
				buyerProposals.add(proposal);
			}
		}

		buyerProposals.sort((o1, o2) -> o1[0] - o2[0]);

		int m = Integer.parseInt(in.readLine());
		StringTokenizer st = new StringTokenizer(in.readLine());
		List<int[]> sinarios = new ArrayList<>();
		for (int i = 0; i < m; i++) {
			int size = Integer.parseInt(st.nextToken());
			sinarios.add(new int[]{size, i, -1});
		}

		sinarios.sort((o1, o2) -> o1[0] - o2[0]);

		int sum = 0;
		int[] buyerPayment = new int[n];
		int sinarioIdx = 0;
		for (int i = 0; i < buyerProposals.size(); i++) {
			int[] proposal = buyerProposals.get(i);
			if (buyerPayment[proposal[2]] < proposal[1]) {
				sum += - buyerPayment[proposal[2]] + proposal[1];
				buyerPayment[proposal[2]] = proposal[1];
			}
			while (sinarioIdx < sinarios.size() && sinarios.get(sinarioIdx)[0] <= sum) {

				sinarios.get(sinarioIdx)[2] = proposal[0];
				++sinarioIdx;
			}
		}

		sinarios.sort((o1, o2) -> o1[1] - o2[1]);

		for (int[] sinario: sinarios) {
			System.out.print(sinario[2] + " ");
		}
	}
}