package programmers;

import java.util.Arrays;

public class Solution42746 {
	public String solution(int[] numbers) {
		return Arrays.stream(numbers)
			.mapToObj(String::valueOf)
			.sorted((o1, o2) -> Integer.parseInt(o2 + o1) - Integer.parseInt(o1 + o2))
			.reduce(((s, s2) -> s + s2))
			.stream()
			.map(s -> s.charAt(0) != '0' ? s : "0")
			.findFirst()
			.orElse("0");
	}
}
