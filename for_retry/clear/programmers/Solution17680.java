package programmers;

import java.util.*;

public class Solution17680 {
	public int solution(int cacheSize, String[] cities) {

		List<String> cache = new LinkedList<>();
		int answer = 0;
		for (String city: cities) {
			city = city.toUpperCase();
			if (cache.contains(city)) {
				cache.remove(city);
				cache.add(city);
				answer += 1;
			} else {
				if (cacheSize != 0 && cache.size() == cacheSize) {
					cache.remove(0);
				}
				if (cacheSize != 0)
					cache.add(city);
				answer += 5;
			}
		}
		return answer;
	}
}