package programmers;

public class Solution77886 {
	public String[] solution(String[] s) {
		String[] answer = new String[s.length];
		for (int i = 0; i < s.length; i++) {
			answer[i] = solve(s[i]);
		}
		return answer;
	}
	public String solve(String target) {
		char[] stack = new char[target.length()];
		int stackIndex = 0;
		int count = 0;
		for (int i = 0; i < target.length(); i++) {
			char number = target.charAt(i);
			if (stackIndex < 2) {
				stack[stackIndex++] = number;
				continue;
			}

			if (stack[stackIndex - 2] == '1' && stack[stackIndex - 1] == '1' && number == '0') {
				count += 1;
				stackIndex -= 2;
			} else {
				stack[stackIndex++] = number;
			}
		}
		int oneCount = 0;
		while (--stackIndex >= 0 && stack[stackIndex] == '1') {
			oneCount++;
		}
		StringBuilder stringBuilder = new StringBuilder();
		for (int i = 0; i <= stackIndex; i++) {
			stringBuilder.append(stack[i]);
		}
		for (int i = 0; i < count; i++) {
			stringBuilder.append("110");
		}

		for (int i = 0; i < oneCount; i++) {
			stringBuilder.append("1");
		}
		return stringBuilder.toString();
	}
}
