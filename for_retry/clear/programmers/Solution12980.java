package programmers;

import java.util.*;

public class Solution12980 {
	public int solution(int n) {
		return Integer.bitCount(n);
	}

	private int myBitCount(int n) {
		int ans = 0;

		while (n > 0) {
			if (n % 2 != 0)
				ans++;
			n = n / 2;
		}
		return ans;
	}
}