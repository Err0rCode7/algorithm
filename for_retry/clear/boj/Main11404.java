package boj;

import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main11404 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static int n, m;
		static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		public static void solution() throws IOException {
			n = parseInt(in.readLine());
			m = parseInt(in.readLine());
			int[][] dist = new int[n + 1][n + 1];
			for (int i = 1; i < n + 1; i++) {
				for (int j = 1; j < n + 1; j++) {
					if (i != j)
						dist[i][j] = MAX_VALUE;
				}
			}
			for (int i = 0; i < m; i++) {
				StringTokenizer tokenizer = new StringTokenizer(in.readLine());
				int a = parseInt(tokenizer.nextToken());
				int b = parseInt(tokenizer.nextToken());
				int c = parseInt(tokenizer.nextToken());
				dist[a][b] = min(dist[a][b], c);
			}

			for (int k = 1; k < n + 1; k++) {
				for (int i = 1; i < n + 1; i++) {
					for (int j = 1; j < n + 1; j++) {
						if ((long) dist[i][j] > ((long) dist[i][k] + (long) dist[k][j]))
							dist[i][j] = dist[i][k] + dist[k][j];
					}
				}
			}
			for (int i = 1; i < n + 1; i++) {
				for (int j = 1; j < n + 1; j++) {
					if (dist[i][j] == MAX_VALUE)
						out.append("0");
					else
						out.append(Integer.toString(dist[i][j]));
					if (j == n)
						out.append("\n");
					else
						out.append(" ");
				}
			}
			out.flush();
			out.close();
			in.close();
		}
	}

}

