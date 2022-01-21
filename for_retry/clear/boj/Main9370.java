import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main9370 {
	static class Main {
		final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		public static void main(String[] args) throws IOException {
			int T = parseInt(br.readLine());

			for (int i = 0; i < T; i++) {
				StringTokenizer tokenizer = new StringTokenizer(br.readLine());
				int n = parseInt(tokenizer.nextToken());
				int m = parseInt(tokenizer.nextToken());
				int t = parseInt(tokenizer.nextToken());
				tokenizer = new StringTokenizer(br.readLine());
				int s = parseInt(tokenizer.nextToken());
				int g = parseInt(tokenizer.nextToken());
				int h = parseInt(tokenizer.nextToken());

				int[][] graph = new int[n + 1][n + 1];
				for (int j = 0; j < n + 1; j++) {
					Arrays.fill(graph[j], MAX_VALUE);
				}
				List<List<Integer>> pathList = new ArrayList<>();
				for (int j = 0; j < n + 1; j++) {
					pathList.add(new ArrayList<>());
				}
				for (int j = 1; j < m + 1; j++) {
					tokenizer = new StringTokenizer(br.readLine());
					int a = parseInt(tokenizer.nextToken());
					int b = parseInt(tokenizer.nextToken());
					int d = parseInt(tokenizer.nextToken());
					graph[a][b] = d;
					graph[b][a] = d;
					pathList.get(a).add(b);
					pathList.get(b).add(a);
				}

				int[] target = new int[n];
				for (int j = 0; j < t; j++) {
					int a = parseInt(br.readLine());
					target[j] = a;
				}
				Arrays.sort(target);
				int[] fromStart = dijstra(n, s, graph, pathList);
				int[] fromG = dijstra(n, g, graph, pathList);
				int[] fromH = dijstra(n, h, graph, pathList);
				int minG = MAX_VALUE;
				int minH = MAX_VALUE;
				List<Integer> idxListG = new ArrayList<>();
				List<Integer> idxListH = new ArrayList<>();
				for (int j = 0; j < m; j++) {
					int tempG = minG;
					int tempH = minH;

					minG = min(fromG[target[j]], minG);
					if (tempG == minG) {
						idxListG.add(target[j]);
					} else {
						idxListG.clear();
						idxListG.add(target[j]);
					}
					minH = min(fromH[target[j]], minH);
					if (tempH == minH) {
						idxListH.add(target[j]);
					} else {
						idxListH.clear();
						idxListH.add(target[j]);
					}
				}
				if (minG + fromStart[g] > minH + fromStart[h]) {
					idxListG.stream().forEach(idx -> {
						try {
							bw.write(idx + " ");
						} catch (IOException e) {
							e.printStackTrace();
						}
					});
				} else {
					idxListH.stream().forEach(idx -> {
						try {
							bw.write(idx + " ");
						} catch (IOException e) {
							e.printStackTrace();
						}
					});
				}
				bw.flush();
				bw.close();
				br.close();
			}
		}

		private static int[] dijstra(int n, int s, int[][] graph, List<List<Integer>> pathList) {
			int[] visited = new int[n + 1];
			for (int j = 0; j < n + 1; j++) {
				visited[j] = MAX_VALUE;
			}
			PriorityQueue<Node> heap = new PriorityQueue<>();
			heap.add(new Node(0, s));
			while (heap.size() > 0) {
				Node cur = heap.poll();
				if (cur.dist >= visited[cur.curNumber]) continue;
				for (int next: pathList.get(cur.curNumber)) {
					if (cur.dist + graph[cur.curNumber][next] >= visited[cur.curNumber]) continue;
					heap.add(new Node(cur.dist + graph[cur.curNumber][next], next));
					visited[cur.curNumber] = cur.dist + graph[cur.curNumber][next];
				}
			}
			return visited;
		}

		static class Node implements Comparable<Node>{
			int dist;
			int curNumber;

			public Node(int dist, int cur) {
				this.dist = dist;
				this.curNumber = cur;
			}

			@Override
			public int compareTo(Node o) {
				return this.dist - o.dist;
			}
		}
	}
}
