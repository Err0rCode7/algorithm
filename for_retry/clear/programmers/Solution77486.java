package programmers;

import java.util.HashMap;
import java.util.Map;

public class Solution77486 {
	private Map<String, String> parent;
	private Map<String, Integer> income;
	public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
		parent = new HashMap<>();
		income = new HashMap<>();

		for (int i = 0; i < enroll.length; i++) {
			income.put(enroll[i], 0);
			parent.put(enroll[i], referral[i]);
		}

		for (int i = 0; i < seller.length; i++) {
			String s = seller[i];
			int m = amount[i] * 100;
			doSetIncome(s, m);
		}

		int[] answer = new int[enroll.length];
		for (int i = 0; i < enroll.length; i++) {
			answer[i] = income.get(enroll[i]);
		}
		return answer;
	}

	private void doSetIncome(String seller, int amount) {
		int forParent = amount / 10;
		int mine = amount - forParent;
		this.income.put(seller, this.income.getOrDefault(seller, 0) + mine);

		String parent = this.parent.get(seller);
		if (!parent.equals("-") && forParent != 0) {
			doSetIncome(parent, forParent);
		}
	}
}