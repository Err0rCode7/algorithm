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
	static class Solution {
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

		static class Node {
			int count;
			String status;

			public Node(int count, String status) {
				this.count = count;
				this.status = status;
			}
		}
	}
	static class Solution2 {
		public int solution(String begin, String target, String[] words) {
			boolean[] visited = new boolean[words.length];
			Queue<Node2> que = new LinkedList<>();
			que.add(new Node2(begin, 0));
			while (!que.isEmpty()) {
				Node2 cur = que.poll();

				if (cur.status.equals(target))
					return cur.count;

				for (int i = 0; i < words.length; i++) {
					if (visited[i] || ! differOnlyOneChar(cur.status, words[i]))
						continue;
					visited[i] = true;
					que.add(new Node2(words[i], cur.count + 1));
				}
			}
			return 0;
		}

		private boolean differOnlyOneChar(String src, String dest) {
			int count = 0;
			for (int i = 0; i < src.length(); i++) {
				if (src.charAt(i) == dest.charAt(i))
					continue;
				count += 1;
				if (count > 1)
					break;
			}
			return count == 1;
		}

		static class Node2 {
			String status;
			int count;

			public Node2(String curStatus, int count) {
				this.status = curStatus;
				this.count = count;
			}
		}
	}
}

