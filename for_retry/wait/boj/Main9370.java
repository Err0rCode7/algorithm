import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main9370 {
	static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer tokenizer;

	public static void main(String[] args) throws IOException {
		tokenizer = new StringTokenizer(br.readLine());
		Integer T = Integer.valueOf(tokenizer.nextToken());
		for (int i=0;i<T;++i) {
			tokenizer = new StringTokenizer(br.readLine());
			Integer n = Integer.valueOf(tokenizer.nextToken());
			Integer m = Integer.valueOf(tokenizer.nextToken());
			Integer t = Integer.valueOf(tokenizer.nextToken());

			tokenizer = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(tokenizer.nextToken());
			int g = Integer.parseInt(tokenizer.nextToken());
			Integer h = Integer.parseInt(tokenizer.nextToken());
			int[][] cost = new int[n + 1][n + 1];
			for (int j=0; j < n + 1; ++j){
				for (int k=0; k < n + 1; ++k) {
					cost[j][k] = Integer.MAX_VALUE;
				}
			}
			List<Integer>[] graph = new List[n + 1];
			for (int j = 0; i <n + 1; ++i) {
				graph[i] = new ArrayList<>();
			}
			for (int j=0; j < m; ++j) {
				tokenizer = new StringTokenizer(br.readLine());
				Integer a = Integer.valueOf(tokenizer.nextToken());
				Integer b = Integer.valueOf(tokenizer.nextToken());
				Integer d = Integer.valueOf(tokenizer.nextToken());
				graph[a].add(b);
				graph[b].add(a);
				cost[a][b]=d;
				cost[b][a]=d;
			}

			int[] target = new int[t];
			for (int j=0; j < t; ++j) {
				int x = Integer.parseInt(br.readLine());
				target[j] = x;
			}

		}

	}

	static class Path implements Comparable<Path>{
		int a;
		int b;
		int d;

		public Path(int a, int b, int d) {
			this.a = a;
			this.b = b;
			this.d = d;
		}

		public int getA() {
			return a;
		}

		public int getB() {
			return b;
		}

		public int getD() {
			return d;
		}

		public void setD(int d) {
			this.d = d;
		}

		@Override
		public int compareTo(Path o) {
			return Integer.compare(this.d, o.getD());
		}
	}

	static void solve(int startNode, List[] graph, int[] target, int[][] dist, int g, int h, int n) {
		// s -> g -> target1, s -> g -> target2
		// s -> h -> target1, s -> h -> target2,
	}

	static int dijkstra(int startNode, List<Integer>[] graph, int target, int[][] dist, int g, int h, int n) {
		// 다익스트라
		Queue<Path> heap = new PriorityQueue<>(((o1, o2) -> Integer.compare(o1.) ));
		Path start = new Path(0, startNode, 0);
		heap.add(start);
		int[] visited = new int[n + 1];
		while (heap.size() > 0) {
			Path path = heap.poll();
			if (visited[path.getB()] <= path.getD()) continue;

			for (int next: graph[path.getB()]) {
				int cost = dist[path.getB()][next] + path.getD();
				if (visited[next] <= cost) continue;

				heap.add(new Path(path.b, next, cost));
			}
		}
		return visited[target];
	}
}
