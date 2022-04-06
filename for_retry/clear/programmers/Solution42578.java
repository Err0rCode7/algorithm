package programmers;

import static java.util.stream.Collectors.*;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution42578 {
	private int answer;
	public int solution(String[][] clothes) {
		Map<String, Integer> map = new HashMap<>();
		for (String[] clothe : clothes) {
			if (map.containsKey(clothe[1]))
				map.replace(clothe[1], map.get(clothe[1]) + 1);
			else
				map.put(clothe[1], 1);
		}

		answer = 0;
		int[] counts = new int[map.size()];
		int index = 0;
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			// answer += entry.getValue();
			counts[index++] = entry.getValue();
		}
		for (int i = 0; i < index; i++) {
			combination(i, index, counts[i], counts);
		}

		return answer;
	}

	public void combination(int start, int limit, int sum, int[] counts) {
		answer += sum;
		for (int i = start + 1; i < limit; i++) {
			combination(i, limit, counts[i] * sum, counts);
		}
	}

	private int solution2(String[][] clothes) {
		return Arrays.stream(clothes)
			.collect(groupingBy(p -> p[1], mapping(p -> p[0], counting())))
			.values()
			.stream()
			.collect(reducing(1L, (x, y) -> x * (y + 1))).intValue() - 1;
	}
}
