package programmers;

public class Main86053 {
	public static void main(String[] args) {
		long result = new Solution()
			.solution(10, 10, new int[]{100}, new int[]{100}, new int[]{7}, new int[]{10});
		System.out.println(result);
		result = new Solution()
			.solution(90, 500, new int[]{70, 70, 0}, new int[]{0, 0, 500}, new int[]{100, 100, 2}, new int[]{4, 8, 1});
		System.out.println(result);

	}

	static class Solution {
		static long max, min, mid;
		public long solution(int a, int b, int[] g, int[] s, int[] w, int[] t) {

			max =  (long) Math.pow(10, 14) * 4;
			min = 0;
			mid = 0;
			long answer = max;
			int n = g.length;

			while (min <= max) {
				mid = (max + min) / 2;
				long gold = 0;
				long silver = 0;
				long total = 0;

				for (int i = 0; i < n; i++) {
					long count = mid / (t[i] * 2L);
					if (mid % (t[i] * 2L) >= t[i]) {
						count += 1;
					}

					gold += count * w[i] >= g[i] ? g[i] : count * w[i];
					silver += count * w[i] >= s[i] ? s[i] : count * w[i];
					total += count * w[i] >= s[i] + g[i] ? s[i] + g[i] : count * w[i];
				}

				if (gold >= a && silver >= b && total >= a + b) {
					max = mid - 1;
					answer = Long.min(answer, mid);
				} else {
					min = mid + 1;
				}
			}
			return answer;
		}
	}
}
