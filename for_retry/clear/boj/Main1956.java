package boj;

import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		int solution = Solution.solution();
		System.out.println(solution);
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static int v, e;
		static int[][] graph;

		public static int solution() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			v = parseInt(tokenizer.nextToken());
			e = parseInt(tokenizer.nextToken());

			graph = new int[v + 1][v + 1];
			for (int i = 1; i < v + 1; i++) {
				Arrays.fill(graph[i], MAX_VALUE);
			}

			for (int i = 0; i < e; i++) {
				tokenizer = new StringTokenizer(in.readLine());
				int a = parseInt(tokenizer.nextToken());
				int b = parseInt(tokenizer.nextToken());
				int c = parseInt(tokenizer.nextToken());
				graph[a][b] = c;
			}

			for (int k = 1; k < v + 1; k++) {
				for (int a = 1; a < v + 1; a++) {
					if (graph[a][k] == MAX_VALUE) continue;
					for (int b = 1; b < v + 1; b++) {
						if (graph[k][b] == MAX_VALUE) continue;
						if (graph[a][b] > graph[a][k] + graph[k][b])
							graph[a][b] = graph[a][k] + graph[k][b];

					}
				}
			}
			int answer = MAX_VALUE;
			for (int i = 1; i < v + 1; i++) {
				if (answer > graph[i][i])
					answer = graph[i][i];
			}

			if (answer == MAX_VALUE)
				return -1;
			return answer;
		}
	}
}


