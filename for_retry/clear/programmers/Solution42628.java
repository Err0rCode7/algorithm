package programmers;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution42628 {
	public int[] solution(String[] operations) {
		int[] answer = {};

		Queue<Integer> minHeap = new PriorityQueue<>();
		Queue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
		Map<Integer, Integer> counts = new HashMap<>();

		for (String operation : operations) {
			int number = Integer.parseInt(operation.substring(2));
			if (operation.startsWith("I")) {
				if (counts.containsKey(number)) {
					counts.replace(number, counts.get(number) + 1);
				} else {
					counts.put(number, 1);
				}
				minHeap.add(number);
				maxHeap.add(number);
			} else {
				if (number == 1) {
					if (minHeap.isEmpty() || maxHeap.isEmpty()) {
						maxHeap.clear();
						continue;
					}
					Integer maxValue = maxHeap.poll();
					counts.replace(maxValue, counts.get(maxValue) - 1);
				} else if (number == -1) {
					if (maxHeap.isEmpty() || minHeap.isEmpty()) {
						minHeap.clear();
						continue;
					}
					Integer minValue = minHeap.poll();
					counts.replace(minValue, counts.get(minValue) - 1);
				}
			}
		}
		int[] result = new int[2];
		if (!minHeap.isEmpty() && !maxHeap.isEmpty()) {
			boolean hasMax = false;
			boolean hasMin = false;

			while (!maxHeap.isEmpty()) {
				Integer maxValue = maxHeap.poll();
				if (counts.get(maxValue) > 0) {
					result[0] = maxValue;
					counts.replace(maxValue, counts.get(maxValue) - 1);
					hasMax = true;
					break;
				}
			}

			while (!minHeap.isEmpty()) {
				Integer minValue = minHeap.poll();
				if (counts.get(minValue) > 0) {
					result[1] = minValue;
					hasMin = true;
					break;
				}
			}

			if (!hasMax && hasMin)
				result[0] = result[1];
			else if (hasMax && !hasMin)
				result[1] = result[0];
		}
		return result;
	}
}
