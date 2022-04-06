package programmers;

import java.util.Arrays;

public class Solution42577 {
	public boolean solution(String[] phoneBook) {
		Arrays.sort(phoneBook);
		System.out.println(Arrays.toString(phoneBook));
		for (int i = 0; i < phoneBook.length - 1; i++)
			if (phoneBook[i + 1].startsWith(phoneBook[i]))
				return false;
		return true;
	}
}

// class Solution {
// 	public boolean solution(String[] phone_book) {
//
// 		Map<Integer, Set<String>> stringMap = new HashMap<>();
// 		for (int i = 1; i < 21; i++) {
// 			stringMap.put(i, new HashSet<>());
// 		}
// 		Arrays.sort(phone_book);
// 		for (String s : phone_book) {
// 			StringBuilder stringBuilder = new StringBuilder();
// 			for (int i = 0; i < s.length() - 1; i++) {
// 				stringBuilder.append(s.charAt(i));
// 				Set<String> set = stringMap.get(stringBuilder.length());
// 				if (set.contains(stringBuilder.toString()))
// 					return false;
// 			}
// 			stringMap.get(s.length()).add(s);
// 		}
// 		return true;
// 	}
// }