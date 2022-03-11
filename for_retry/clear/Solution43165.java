package programmers;

public class Solution43165 {
	private int answer;
	public int solution(int[] numbers, int target) {
		answer = 0;
		dfs(target, 0, numbers, 0, new int[] {1, -1});
		return answer;
	}

	public void dfs(int target, int result, int[] numbers, int depth, int[] opers) {
		if (depth == numbers.length) {
			if (result == target)
				this.answer++;
			return;
		}
		for (int oper : opers) {
			int cur = numbers[depth] * oper;
			dfs(target, result + cur, numbers, depth + 1, opers);
		}
	}
}
