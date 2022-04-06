package programmers;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution42891 {
	public int solution(int[] food_times, long k) {

		PriorityQueue<Food> heap = new PriorityQueue<>((Comparator.comparingInt(o -> o.time)));
		for (int i = 0; i < food_times.length; i++) {
			heap.add(new Food(food_times[i], i + 1));
		}

		long totalCycle = 0;
		while (!heap.isEmpty()) {

			long cycle = (k / heap.size());
			k = k % heap.size();
			Food minFood = heap.peek();
			long realCycle = cycle;
			if (minFood.time - (totalCycle + cycle) > 0) {
				break;
			} else if (minFood.time - (totalCycle + cycle) < 0) {
				realCycle = minFood.time - totalCycle;
			}

			k += (cycle - realCycle) * heap.size();
			totalCycle += realCycle;
			while (!heap.isEmpty() && minFood.time == heap.peek().time) {
				heap.poll();
			}
		}

		if (heap.size() == 0)
			return -1;

		Food[] leftFoods = heap.toArray(new Food[0]);
		Arrays.sort(leftFoods, Comparator.comparingInt(o -> o.orderNumber));
		return leftFoods[(int)(k % leftFoods.length)].orderNumber;
	}

	private static class Food {
		int time;
		int orderNumber;

		public Food(int time, int orderNumber) {
			this.time = time;
			this.orderNumber = orderNumber;
		}
	}
}

