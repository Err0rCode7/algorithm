package programmers;

import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Solution43164 {
	private static Map<String, LinkedList<String>> graph;
	private static int ticketSize;
	public String[] solution(String[][] tickets) {
		ticketSize = tickets.length;
		graph = new HashMap<>();
		for (int i = 0; i < tickets.length; i++) {
			String from = tickets[i][0];
			String to = tickets[i][1];
			if (!graph.containsKey(from))
				graph.put(from, new LinkedList<>());
			graph.get(from).add(to);
		}

		for (List<String> value : graph.values()) {
			Collections.sort(value);
		}

		String start = "ICN";
		LinkedList<String> result = new LinkedList<>();
		dfs(start, result);
		return result.toArray(new String[0]);
	}

	public boolean dfs(String start, Deque<String> deque) {

		deque.addLast(start);
		if (deque.size() == ticketSize + 1)
			return true;

		if (!graph.containsKey(start)) {
			deque.removeLast();
			return false;
		}

		Deque<String> nexts = graph.get(start);
		int size = nexts.size();
		for (int i = 0; i < size; i++) {
			String next = nexts.pollFirst();
			if (dfs(next, deque))
				return true;
			nexts.addLast(next);
		}
		deque.removeLast();
		return false;
	}
}