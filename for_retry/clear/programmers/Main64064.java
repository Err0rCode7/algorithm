package programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;


public class Main64064 {

	static class Solution {
		static Set<List<String>> result;
		public int solution(String[] user_id, String[] banned_id) {
			result = new HashSet<>();
			doPermutation(user_id, banned_id);
			return result.size();
		}

		public void doPermutation(String[] users, String[] bans) {
			boolean[] visited = new boolean[users.length];
			LinkedList<String> result = new LinkedList<>();
			permutation(visited, users, bans, 0, result);
		}

		public void permutation(boolean[] visited, String[] users, String[] bans, int recCount, LinkedList<String> result) {
			if (recCount == bans.length) {
				int index = 0;
				List<String> list = new ArrayList<>(bans.length);
				for (String user : result) {
					if (!canBan(user, bans[index++]))
						return;
					list.add(user);
				}

				Collections.sort(list);
				Solution.result.add(list);
				return;
			}

			for (int i = 0; i < users.length; i++) {
				if (visited[i]) continue;
				visited[i] = true;
				result.addLast(users[i]);
				permutation(visited, users, bans,recCount + 1, result);
				result.removeLast();
				visited[i] = false;
			}
		}

		public boolean canBan(String user, String filter) {
			if (user.length() != filter.length())
				return false;
			for (int i = 0; i < user.length(); i++) {
				if (filter.charAt(i) == '*') continue;

				if (user.charAt(i) != filter.charAt(i)) return false;
			}
			return true;
		}

	}
}


