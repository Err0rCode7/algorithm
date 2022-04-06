package programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution72412 {
	public int[] solution(String[] info, String[] query) {

		Map<String, List<Integer>> scoreMap = new HashMap<>();
		Queue<String> que = new LinkedList<>();
		for (String s : info) {
			StringTokenizer tokenizer = new StringTokenizer(s, " ");
			que.add("");
			for (int i = 0; i < 4; i++) {
				String token = tokenizer.nextToken();
				int size = que.size();
				for (int j = 0; j < size; ++j) {
					String poll = que.poll();
					que.add(poll + "-");
					que.add(poll + token);
				}
			}

			int score = Integer.parseInt(tokenizer.nextToken());
			while (!que.isEmpty()) {
				String key = que.poll();
				if (!scoreMap.containsKey(key)) {
					scoreMap.put(key, new ArrayList<>());
				}
				scoreMap.get(key).add(score);
			}
		}

		for (List<Integer> value : scoreMap.values()) {
			Collections.sort(value);
		}

		int[] answer = new int[query.length];
		int idx = 0;
		for (String s : query) {
			String[] s1 = s.replaceAll(" and ", "").split(" ");

			if (!scoreMap.containsKey(s1[0])) {
				answer[idx++] = 0;
				continue;
			}

			answer[idx++] = scoreMap.get(s1[0]).size() - findLowerBound(Integer.parseInt(s1[1]), scoreMap.get(s1[0]));
		}

		return answer;
	}

	private int findLowerBound(int targetScore, List<Integer> scores) {
		int s = 0;
		int e = scores.size();

		while (s < e) {
			int mid = (s + e) / 2;

			if (scores.get(mid) >= targetScore) {
				e = mid;
			} else {
				s = mid + 1;
			}
		}
		return s;
	}
}
