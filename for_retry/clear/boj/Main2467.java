package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main2467 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
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
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			nums = new int[n];
			for (int i = 0; i < n; i++) {
				nums[i] = parseInt(tokenizer.nextToken());
			}

			int answer = 2_000_000_001;
			int answerLeft = -1_000_000_001;
			int answerRight = 1_000_000_001;
			for (int i = 0; i < n; i++) {

				int leftResult = binarySearch(0, i - 1, nums[i]);
				int rightResult = binarySearch(i + 1, n - 1, nums[i]);

				if (leftResult != MAX_VALUE && nums[i] + leftResult == 0) {
					answerLeft = leftResult;
					answerRight = nums[i];
					break;
				}

				if (rightResult != MAX_VALUE && nums[i] + rightResult == 0) {
					answerLeft = nums[i];
					answerRight = rightResult;
					break;
				}

				if (leftResult != MAX_VALUE && answer > Math.abs(nums[i] + leftResult)) {
					answer = Math.abs(nums[i] + leftResult);
					answerLeft = leftResult;
					answerRight = nums[i];
				}

				if (rightResult != MAX_VALUE && answer > Math.abs(nums[i] + rightResult)) {
					answer = Math.abs(nums[i] + rightResult);
					answerLeft = nums[i];
					answerRight = rightResult;
				}
			}

			System.out.print(answerLeft + " " + answerRight);
		}

		public static int binarySearch(int left, int right, int target) {

			int answer = 0;
			int index = -1;
			while (left <= right) {
				int mid = (left + right) / 2;
				if (index == -1 || Math.abs(target + nums[mid]) < answer) {
					answer = Math.abs(target + nums[mid]);
					index = mid;
				}

				if (target + nums[mid] < 0) {
					left = mid + 1;
				} else if (target + nums[mid] == 0) {
					return nums[mid];
				} else {
					right = mid - 1;
				}
			}
			if (index == -1)
				return MAX_VALUE;
			return nums[index];
		}
	}
}