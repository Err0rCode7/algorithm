package programmers;

import java.util.ArrayList;
import java.util.List;

public class Solution1835 {
	public List<Condition> conditions;
	private char[] people;
	private List<char[]> stringList;
	public int solution(int n, String[] data) {
		people = new char[]{'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};

		createConditions(data);
		stringList = new ArrayList<>();
		int answer = 0;
		dfs(0, new boolean[people.length], new char[people.length]);
		for (char[] s : stringList) {
			boolean success = true;
			for (Condition condition : conditions) {
				for (int i = 0; i < s.length; i++) {
					if (s[i] == condition.from) {
						if (!checkCondition(condition, s, i, condition.target))
							success = false;
						break;
					}

					if (s[i] == condition.target) {
						if (!checkCondition(condition, s, i, condition.from))
							success = false;
						break;
					}
				}
				if (!success)
					break;
			}
			if (success) {
				answer += 1;
			}
		}
		return answer;
	}

	public void createConditions(String[] data) {

		conditions = new ArrayList<>();
		for (String d : data) {
			char a = d.charAt(0);
			char b = d.charAt(2);
			char type = d.charAt(3);
			int offset = d.charAt(4) - '0';
			conditions.add(new Condition(a, b, type, offset));
		}

	}

	public void dfs(int depth, boolean[] used, char[] result) {
		if (depth == people.length) {
			stringList.add(result.clone());
			return;
		}

		for (int i = 0; i < people.length; i++) {
			if (used[i]) continue;
			used[i] = true;
			result[depth] = people[i];
			dfs(depth + 1, used, result);
			used[i] = false;
		}
	}

	public boolean checkCondition(Condition condition, char[] result, int depth, char target) {
		switch (condition.type) {
			case '>':
				if (!leftIncludeCheck(result, depth - 1, depth - 1 - condition.offset, target)
					&& !rightIncludeCheck(result, depth + 1, depth + condition.offset + 1, target))
					break;
				return false;
			case '<':
				if (leftIncludeCheck(result, depth - 1, depth - condition.offset, target)
					|| rightIncludeCheck(result, depth + 1, depth + condition.offset, target))
					break;
				return false;
			case '=':
				if (depth - condition.offset - 1 >= 0 && result[depth - condition.offset - 1] == target)
					break;
				if (depth + condition.offset + 1 < result.length && result[depth + condition.offset + 1] == target)
					break;

				return false;
		}
		return true;
	}

	private boolean leftIncludeCheck(char[] result, int start, int last, char target) {
		for (int i = start; i >= last && i >= 0; i--) {
			if (result[i] == target)
				return true;
		}
		return false;
	}

	private boolean rightIncludeCheck(char[] result, int start, int last, char target) {
		for (int i = start; i <= last && i < result.length; i++) {
			if (result[i] == target)
				return true;
		}
		return false;
	}

	public static class Condition {
		char from;
		char target;
		char type;
		int offset;

		public Condition(char from, char target, char type, int offset) {
			this.from = from;
			this.target = target;
			this.type = type;
			this.offset = offset;
		}
	}
}
