package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Solution42853 {
	public int solution(int bridge_length, int weight, int[] truck_weights) {
		Queue<int[]> bridgeQue = new LinkedList<>(); // startTime, weight
		Queue<Integer> truckQue = new LinkedList<>();
		for (int truck_weight : truck_weights) {
			truckQue.add(truck_weight);
		}
		int time = 1;
		int totalWeight = truckQue.poll();
		bridgeQue.add(new int[] {time, totalWeight});
		while (true) {

			if (!bridgeQue.isEmpty() && time - bridgeQue.peek()[0] >= bridge_length) {
				int[] truck = bridgeQue.poll();
				totalWeight -= truck[1];
			}

			int truckWeight = 0;
			if (!truckQue.isEmpty())
				truckWeight = truckQue.peek();

			if (truckWeight != 0 && totalWeight + truckWeight <= weight) {
				totalWeight += truckWeight;
				bridgeQue.add(new int[] {time, truckWeight});
				truckQue.poll();
			}
			if (truckQue.isEmpty() && bridgeQue.isEmpty())
				break;
			++time;
		}
		return time;
	}
}