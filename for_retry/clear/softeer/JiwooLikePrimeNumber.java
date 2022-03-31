package softeer;

import java.util.*;
import java.io.*;


public class JiwooLikePrimeNumber
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		List<int[]>[] graph = new List[n + 1];

		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; ++i) {
			st = new StringTokenizer(in.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());

			graph[a].add(new int[]{b, cost});
			graph[b].add(new int[]{a, cost});
		}

		Queue<int[]> heap = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]); // int[] ==> node, minimumLevel
		heap.add(new int[]{1, 0});

		int[] visited = new int[n + 1];
		Arrays.fill(visited, 1_000_000_001);

		while (!heap.isEmpty()) {
			int[] cur = heap.poll();

			if (visited[cur[0]] < cur[1]) continue;

			if (cur[0] == n) {
				break;
			}
			for(int[] path : graph[cur[0]]) {
				int nextNode = path[0];
				int minimumLevel = Math.max(cur[1], path[1]);
				if (visited[nextNode] <= minimumLevel) continue;

				visited[nextNode] = minimumLevel;
				heap.add(new int[]{nextNode, minimumLevel});
			}
		}

		int minLevel = visited[n] + 1;

		while (true) {

			int sqrt = (int)Math.sqrt(minLevel);
			boolean success = true;
			for (int i = 2; i <= sqrt; ++i) {
				if (minLevel % i == 0){
					success = false;
					break;
				}

			}

			if (success)
				break;
			minLevel++;
		}
		System.out.println(minLevel);
	}
}