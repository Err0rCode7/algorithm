package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main12886 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
		static int[][] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[][] rects;
		public static void solution() throws IOException {

			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			int a = parseInt(tokenizer.nextToken());
			int b = parseInt(tokenizer.nextToken());
			int c = parseInt(tokenizer.nextToken());

			Set<MyKey> visited = new HashSet<>();
			Queue<int[]> que = new LinkedList<>();
			int[] first = {a, b, c};
			que.add(first);
			MyKey myKey = new MyKey(first);
			visited.add(myKey);
			int answer = 0;
			while (que.size() > 0) {
				int[] cur = que.poll();

				if (cur[0] == cur[1] && cur[1] == cur[2]) {
					answer = 1;
					break;
				}

				int min = Math.min(cur[0], cur[1]);
				int max = Math.max(cur[0], cur[1]);
				int left, right;
				if (min == cur[0]) {
					left = min * 2;
					right = max - min;
				} else {
					right = min * 2;
					left = max - min;
				}
				int[] next = new int[]{left, right, cur[2]};
				Arrays.sort(next);
				myKey = new MyKey(next);
				if (!visited.contains(myKey)) {
					que.add(next);
					visited.add(myKey);
				}
				min = Math.min(cur[1], cur[2]);
				max = Math.max(cur[1], cur[2]);

				if (min == cur[1]) {
					left = min * 2;
					right = max - min;
				} else {
					right = min * 2;
					left = max - min;
				}
				next = new int[]{left, right, cur[0]};
				Arrays.sort(next);
				myKey = new MyKey(next);
				if (!visited.contains(myKey)) {
					que.add(next);
					visited.add(myKey);
				}


				min = Math.min(cur[0], cur[2]);
				max = Math.max(cur[0], cur[2]);
				if (min == cur[0]) {
					left = min * 2;
					right = max - min;
				} else {
					right = min * 2;
					left = max - min;
				}
				next = new int[]{left, right, cur[1]};
				Arrays.sort(next);
				myKey = new MyKey(next);
				if (!visited.contains(myKey)) {
					que.add(next);
					visited.add(myKey);
				}
			}
			System.out.println(answer);
		}
		public static class MyKey {
			int[] key;

			public MyKey(int[] key) {
				this.key = key;
			}

			@Override
			public boolean equals(Object o) {
				if (this == o)
					return true;
				if (o == null || getClass() != o.getClass())
					return false;
				Solution.MyKey myKey = (Solution.MyKey)o;
				return Arrays.equals(key, myKey.key);
			}

			@Override
			public int hashCode() {
				return Arrays.hashCode(key);
			}
		}
	}
}