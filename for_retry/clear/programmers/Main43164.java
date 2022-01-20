import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main43164 {
	static class Solution {
		public String[] solution(String[][] tickets) {

			Map<String, Queue<String>> path = new HashMap<>();

			for (String[] ticket : tickets) {
				if (path.containsKey(ticket[0])) {
					path.get(ticket[0]).add(ticket[1]);
				} else {
					PriorityQueue<String> bucket = new PriorityQueue<>();
					bucket.add(ticket[1]);
					path.put(ticket[0], bucket);
				}
			}

			Deque<String> stack = new LinkedList<>();
			List<String> answer = new LinkedList<>();
			stack.add("ICN");
			while (stack.size() > 0) {
				if (path.containsKey(stack.peekLast()) && path.get(stack.peekLast()).size() > 0) {
					stack.add(path.get(stack.peekLast()).poll());
				} else {
					answer.add(stack.pollLast());
				}
			}
			Collections.reverse(answer);
			return answer.toArray(new String[answer.size()]);
		}

		public static void main(String[] args) {
			Solution solution = new Solution();

			String[][] tickets = {
				{"ICN", "JKF"},
				{"HND", "IAD"},
				{"JKF", "HND"}
			};

			String[] result = solution.solution(tickets);
			for (int i = 0; i < result.length; i++) {
				System.out.println(result[i]);
			}
			tickets = new String[][] {
				{"ICN", "SFO"},
				{"ICN", "ATL"},
				{"SFO", "ATL"},
				{"ATL", "ICN"},
				{"ATL", "SFO"}
			};
			System.out.println("test");
			result = solution.solution(tickets);
			for (int i = 0; i < result.length; i++) {
				System.out.println(result[i]);
			}
		}
	}
}