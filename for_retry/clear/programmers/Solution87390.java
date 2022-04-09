package programmers;

public class Solution87390 {
	private int[] arr;
	public int[] solution(int n, long left, long right) {
		int size = (int)(right - left);
		size++;
		int[] answer = new int[size];
		int idx = 0;
		for (long i = left; i <= right; i++) {
			int x = (int)(i % n);
			int y = (int)(i / n);
			answer[idx] = Math.max(x, y) + 1;

			idx++;
		}
		return answer;
	}
}