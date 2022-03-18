package programmers;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class Solution72411 {
	private Map<Integer, Map<String, Integer>> courseCountMap;
	public String[] solution(String[] orders, int[] course) {
		courseCountMap = new HashMap<>();
		for (int count : course) {
			courseCountMap.put(count, new HashMap<>());
		}

		for (int i = 0; i < orders.length; i++) {
			char[] order = orders[i].toCharArray();
			Arrays.sort(order);
			makeCombination(order, 0, "");
		}

		Set<String> result = new HashSet<>();
		for (int count : course) {
			Map<String, Integer> courseMap = courseCountMap.get(count);
			List<Map.Entry<String, Integer>> sortedEntryList = courseMap.entrySet()
				.stream()
				.filter((o -> o.getValue() > 1))
				.sorted(((o1, o2) -> o2.getValue() - o1.getValue()))
				.collect(Collectors.toList());

			if (sortedEntryList.isEmpty())
				continue;

			Map.Entry<String, Integer> first = sortedEntryList.get(0);
			result.add(first.getKey());
			for (Map.Entry<String, Integer> entry : sortedEntryList) {
				if (entry.getValue() < first.getValue())
					break;
				result.add(entry.getKey());
			}
		}

		return result.stream().sorted().toArray(String[]::new);
	}

	public void makeCombination(char[] order, int start, String result) {
		if (courseCountMap.containsKey(result.length())) {
			Map<String, Integer> courseMap = courseCountMap.get(result.length());
			courseMap.put(result, courseMap.getOrDefault(result, 0) + 1);
		}
		if (result.length() == order.length)
			return;

		for (int i = start; i < order.length; i++) {
			makeCombination(order, i + 1, result + order[i]);
		}
	}
}
