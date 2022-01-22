package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Main43163 {
	public static void main(String[] args) {
		Solution solution = new Solution();
		int result = solution.solution("hit", "cog", new String[] {"hot", "dot", "dog", "lot", "log", "cog"});
		System.out.println(result);
		result = solution.solution("hit", "cog", new String[] {"hot", "dot", "dog", "lot", "log"});
		System.out.println(result);
	}
}

class Solution {
	public int solution(String begin, String target, String[] words) {
		int answer = 0;

		Queue<Node> que = new LinkedList<>();
		que.add(new Node(0, begin));
		boolean[] visited = new boolean[words.length];
		while (que.size() > 0) {
			Node cur = que.poll();
			if (target.equals(cur.status)) {
				answer = cur.count;
				break;
			}
			for (int i = 0; i < words.length; i++) {
				if (visited[i]) continue;
				if (!isDifferentOnlyOne(cur.status, words[i])) continue;

				visited[i] = true;
				que.add(new Node(cur.count + 1, words[i]));
			}
		}
		return answer;
	}

	public boolean isDifferentOnlyOne(String a, String b) {
		//given a.length == b.length

		int count = 0;
		for (int i = 0; i < a.length(); i++) {
			if (a.charAt(i) != b.charAt(i)) {
				count += 1;
			}
			if (count > 1) {
				return false;
			}
		}
		return true;
	}

	class Node {
		int count;
		String status;

		public Node(int count, String status) {
			this.count = count;
			this.status = status;
		}
	}
}