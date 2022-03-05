package programmers;

public class Solution64062 {
	public int solution(int[] stones, int k) {
		int s = 0;
		int e = 200_000_000;
		while (s < e) {
			int mid = (s + e) / 2;
			int count = 0;
			boolean valid = true;
			for (int i = 0; i < stones.length; i++) {
				if (stones[i] < mid) {
					count++;
					if (count == k){
						valid = false;
						break;
					}
					continue;
				}
				count = 0;
			}

			if (valid) {
				s = mid;
			} else {
				e = mid;
			}
			if (mid == (s + e) / 2)
				break;
		}
		return s;
	}
}