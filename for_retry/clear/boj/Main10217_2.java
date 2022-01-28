package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

class Main10217_2 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static int r, c;
		static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		// static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static List<List<Solution.Ticket>> tickets;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		public static void solution() throws IOException {

			int t = parseInt(in.readLine());
			for (int i = 0; i < t; i++) {
				solve();
			}

			// solve();
			// out.flush();
			// out.close();
			in.close();
		}

		private static void solve() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			int n = parseInt(tokenizer.nextToken());
			int m = parseInt(tokenizer.nextToken());
			int k = parseInt(tokenizer.nextToken());
			tickets = new ArrayList<>(n + 1);
			for (int i = 0; i < n + 1; i++) {
				tickets.add(new ArrayList<>());
			}

			for (int i = 0; i < k; i++) {
				tokenizer = new StringTokenizer(in.readLine());
				int u = parseInt(tokenizer.nextToken());
				int v = parseInt(tokenizer.nextToken());
				int c = parseInt(tokenizer.nextToken());
				int d = parseInt(tokenizer.nextToken());
				tickets.get(u).add(new Solution.Ticket(v, c, d));
			}
			int[][] times = new int[n + 1][m + 1];
			for (int i = 0; i < n + 1; i++) {
				if (i == 1) continue;
				Arrays.fill(times[i], MAX_VALUE);
			}
			Queue<int[]> heap = new PriorityQueue<>((Comparator.comparingInt(o -> o[0])));
			heap.add(new int[] {0, 0, 1});
			int answer = MAX_VALUE;

			while (heap.size() > 0) {
				int[] poll = heap.poll();
				int time = poll[0];
				int cost = poll[1];
				int cur = poll[2];

				if (times[cur][cost] < time)
					continue;

				if (cur == n) {
					System.out.println(time);
					answer = time;
					break;
				}

				for (Solution.Ticket ticket : tickets.get(cur)) {
					int nextTime = time + ticket.time;
					int nextCost = cost + ticket.cost;

					if (nextCost > m) continue;

					if (times[ticket.to][nextCost] <= nextTime) continue;

					times[ticket.to][nextCost] = nextTime;
					heap.add(new int[] {nextTime, nextCost, ticket.to});
				}
			}
			if (answer == MAX_VALUE)
				System.out.println("Poor KCM");
		}

		private static class Ticket {
			int to;
			int cost;
			int time;

			public Ticket(int to, int cost, int time) {
				this.to = to;
				this.cost = cost;
				this.time = time;
			}
		}
	}
}

/**
 * dp 예외 tc
 *
 * 1
 * 5 1200 5
 * 1 2 800 1
 * 1 3 100 2
 * 3 2 200 2
 * 2 4 200 2
 * 4 5 300 2
 */