package programmers;

import java.util.*;

public class Solution49993 {
	private Map<Character, Integer> idxMap = new HashMap<>();
	public int solution(String skill, String[] skill_trees) {



		for (int i = 0; i < skill.length(); i++) {
			idxMap.put(skill.charAt(i), i);
		}

		int answer = 0;
		for (String skillTree : skill_trees) {
			if (checkSkillTree(skillTree))
				answer++;
		}
		return answer;
	}

	private boolean checkSkillTree(String skillTree) {
		int recent = -1;
		for (int i = 0; i < skillTree.length(); i++) {
			char ch = skillTree.charAt(i);

			if (!idxMap.containsKey(ch)) continue;

			if (!(idxMap.get(ch) - 1 == recent))
				return false;
			recent = idxMap.get(ch);
		}
		return true;
	}
}