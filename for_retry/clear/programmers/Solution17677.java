package programmers;

import java.util.HashMap;
import java.util.Map;

public class Solution17677 {
	public int solution(String str1, String str2) {

		Map<String, Integer> map1 = new HashMap<>();
		Map<String, Integer> map2 = new HashMap<>();
		int idx1 = 0;
		int idx2 = 0;
		StringBuilder result = new StringBuilder();

		while (idx1 < str1.length() - 1 || idx2 < str2.length() - 1) {
			int count = 0;
			int cursor = idx1;
			int idx1Forloop = idx1;
			int idx2Forloop = idx2;
			result.setLength(0);
			while (cursor < str1.length()) {
				char c = str1.charAt(cursor);
				if ('a' <= c && c <= 'z') {
					result.append((char)(c - 32));
					count++;
				} else if ('A' <= c && c <= 'Z') {
					result.append(c);
					count++;
				} else {
					idx1 = cursor + 1;
					break;
				}
				cursor++;
				if (count == 2) {
					String s = result.toString();
					map1.put(s, map1.getOrDefault(s, 0) + 1);
					idx1 = cursor - 1;
					break;
				}
			}

			result.setLength(0);
			cursor = idx2;
			count = 0;
			while (cursor < str2.length()) {
				char c = str2.charAt(cursor);
				if ('a' <= c && c <= 'z') {
					result.append((char)(c - 32));
					count++;
				} else if ('A' <= c && c <= 'Z') {
					result.append(c);
					count++;
				} else {
					idx2 = cursor + 1;
					break;
				}
				cursor++;
				if (count == 2) {
					String s = result.toString();
					map2.put(s, map2.getOrDefault(s, 0) + 1);
					idx2 = cursor - 1;
					break;
				}
			}
			if (idx1Forloop == idx1 && idx2Forloop == idx2)
				break;
		}

		int cross = 0;
		int union = 0;
		for (Map.Entry<String, Integer> entry : map1.entrySet()) {
			if (map2.containsKey(entry.getKey())) {
				cross += Math.min(entry.getValue(), map2.get(entry.getKey()));
				union += Math.max(entry.getValue(), map2.get(entry.getKey()));
			} else {
				union += entry.getValue();
			}
		}

		for (Map.Entry<String, Integer> entry : map2.entrySet()) {
			if (map1.containsKey(entry.getKey()))
				continue;
			union += entry.getValue();
		}
		if (cross == 0 && union == 0)
			return 65536;

		return (int)(((double)cross / union) * 65536);
	}
}
