package programmers;

public class Solution92342 {
	private int[] answer;
	private int[] info;
	private int n;
	private int maxPoint;
	public int[] solution(int n, int[] info) {
		this.info = info;
		this.n = n;
		this.maxPoint = 0;
		this.answer = new int[info.length];
		dfs(n, 10, new int[info.length]);
		if (maxPoint == 0)
			return new int[]{-1};
		return answer;
	}

	private void dfs(int size, int cur, int[] result) {
		if (cur < 0 || size == 0) {
			result[10] += size;
			int point = getPoint(result);
			// System.out.println(point);
			if (maxPoint < point) {
				maxPoint = point;
				copySrcTo(result, answer);
			} else if (maxPoint == point) {
				for (int i = 10; i >= 0; i--) {
					if (answer[i] != result[i]) {
						if (answer[i] < result[i])
							copySrcTo(result, answer);
						break;
					}
				}
			}
			result[10] -= size;
			return;
		}
		dfs(size, cur - 1, result);
		if (info[cur] < size) {
			result[cur] = info[cur] + 1;
			dfs(size - (info[cur] + 1), cur - 1, result);
			result[cur] = 0;
		}
	}

	private int getPoint(int[] result) {
		int point = 0;
		for (int i = 0; i < info.length - 1; i++) {
			if (result[i] > info[i])
				point += 10 - i;
			else if (!(result[i] == 0 && info[i] == 0))
				point -= 10 - i;
		}
		return point;
	}

	private void copySrcTo(int[] src, int[] answer) {
		for (int i = 0; i < src.length; i++) {
			answer[i] = src[i];
		}
	}
}