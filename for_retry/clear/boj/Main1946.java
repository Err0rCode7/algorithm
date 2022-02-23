package boj;

import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main1946 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k, t;
		static int[] nums;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[] dp;
		static int answer;
		static Map<Integer, Map<Integer, Integer>> graph;

		public static void solution() throws IOException {
			t = parseInt(in.readLine());
			for (int i = 0; i < t; i++) {

				n = parseInt(in.readLine());
				List<int[]> applicants = new ArrayList<>(n);
				for (int j = 0; j < n; j++) {
					StringTokenizer tokenizer = new StringTokenizer(in.readLine());
					int docScore = parseInt(tokenizer.nextToken());
					int interviewScore = parseInt(tokenizer.nextToken());
					int[] applicant = {docScore, interviewScore};
					applicants.add(applicant);
				}

				Collections.sort(applicants, ((o1, o2) -> {
					if (o1[0] == o2[0])
						return o1[1] - o2[1];
					return o1[0] - o2[0];
				}));

				int count = 0;
				int prevInterviewScore = 0;
				for (int[] applicant : applicants) {
					if (count == 0) {
						prevInterviewScore = applicant[1];
						count += 1;
						continue;
					}

					if (prevInterviewScore >= applicant[1]) {
						count += 1;
						prevInterviewScore = applicant[1];
					}
				}

				System.out.println(count);
			}
		}
	}
}