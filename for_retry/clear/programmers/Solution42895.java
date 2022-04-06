package programmers;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution42895 {
	public int solution(int N, int number) {
		Map<Integer, Set<Integer>> map = new HashMap<>();

		int addValue = 0;

		for (int i = 1; i < 9; i++) {
			Set<Integer> set = new HashSet<>();
			map.put(i, set);

			// ex. 5 , 55, 555, 5555
			addValue = addValue * 10 + N;
			set.add(addValue);

			if (i > 1) {
				for (int j = 1; j < i; j++) {
					for (Integer op1 : map.get(j)) {
						for (Integer op2 : map.get(i - j)) {
							set.add(op1 + op2);
							set.add(op1 * op2);
							if (op1 - op2 > 0)
								set.add(op1 - op2);
							if (op1 != 0 && op2 != 0)
								set.add(op1 / op2);
						}
					}
				}
			}
			if (set.contains(number))
				return i;
		}
		return -1;
	}
}
