package programmers;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution64065 {
	public int[] solution(String s) {

		String s1 = s.substring(1, s.length() - 1);

		List<List<String>> combs = new ArrayList<>();

		int i = 0;
		StringBuilder stringBuilder = new StringBuilder();
		while (i < s1.length()) {

			if (s1.charAt(i) == '{') {
				List<String> list = new ArrayList<>();
				while (s1.charAt(i) != '}') {
					if (s1.charAt(i) == '{' || s1.charAt(i) == ',') {
						i++;
						continue;
					}

					while(s1.charAt(i) >= '0' && s1.charAt(i) <= '9'){
						stringBuilder.append(s1.charAt(i));
						i++;
					}

					list.add(stringBuilder.toString());
					stringBuilder.setLength(0);
				}
				combs.add(list);
			}

			i++;
		}

		combs.sort(Comparator.comparingInt(List::size));

		List<Integer> result = new ArrayList<>();
		Set<String> set = new HashSet<>();
		for (List<String> comb : combs) {
			for (String combStringOne : comb) {
				if (set.contains(combStringOne)) continue;

				set.add(combStringOne);
				result.add(Integer.parseInt(combStringOne));
			}
		}
		return result.stream().mapToInt(Integer::intValue).toArray();
	}
}
