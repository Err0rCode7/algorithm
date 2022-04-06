package programmers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution12936 {
	private static long[] factorial;
	private static Queue<Integer> answer;
	public int[] solution(int n, long k) {
		answer = new LinkedList<>();
		factorial = new long[n];
		List<Integer> numbers = new ArrayList<>();
		for (int i = 1; i < n + 1; i++) {
			numbers.add(i);
		}
		solve(n, k - 1, numbers);
		int[] result = new int[n];
		for (int i = 0; i < n; i++) {
			result[i] = answer.poll();
		}
		return result;
	}

	public long getFactorial(int n) {
		if (n <= 0)
			return 1;
		if (n == 2)
			return 2;
		if (factorial[n] != 0)
			return factorial[n];
		return factorial[n] = n * getFactorial(n - 1);
	}

	public void solve(int n, long k, List<Integer> numbers) {
		if (n <= 0)
			return;

		long permSize = getFactorial(n - 1);
		int q = (int)(k / permSize);
		long r = k % permSize;

		Integer remove = numbers.remove(q);
		answer.add(remove);
		solve(n - 1, r, numbers);
	}
}
