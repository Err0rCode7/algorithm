package programmers;

public class Solution12938 {
	public int[] solution(int n, int s) {

		int baseSize = s / n;
		int rest = s % n;
		if (s < n)
			return new int[]{-1};
		int[] answer = new int[n];
		for (int i = n - 1; i >= 0; i--) {
			answer[i] = baseSize + (rest > 0 ? 1 : 0);
			rest--;
		}
		return answer;
	}
}