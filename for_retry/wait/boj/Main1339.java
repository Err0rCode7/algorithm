package boj;

import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Main1339 {
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
			n = parseInt(in.readLine());
			Map<Character, Integer> costMap = new HashMap<>();
			String[] words = new String[n];

			for (int i = 0; i < n; i++) {
				String line = new StringBuilder(in.readLine().strip()).reverse().toString();
				int base = 1;
				for (int j = 0; j < line.length(); j++) {
					char c = line.charAt(j);
					int cost = base;
					if (costMap.containsKey(c)) {
						cost += costMap.get(c);
					}
					costMap.put(c, cost);
					base *= 10;
				}
			}
			List<Integer> values = new ArrayList<>();
			for (Integer value : costMap.values()) {
				values.add(value);
			}
			Collections.sort(values, Comparator.reverseOrder());

			int base = 9;
			int answer = 0;
			for (Integer value : values) {
				answer += base * value;
				base -= 1;
			}
			System.out.println(answer);
		}
	}
}
