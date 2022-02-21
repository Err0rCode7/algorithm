package programmers;

import java.util.*;

public class Solution70130 {
	public void main(String[] args) {
		Solution solution = new Solution();
		int solution1 = solution.solution(new int[] {0});
		int solution2 = solution.solution(new int[] {5, 2, 3, 3, 5, 3});
		int solution3 = solution.solution(new int[] {0, 3, 3, 0, 7, 2, 0, 2, 2, 0});
		System.out.println(solution1);
		System.out.println(solution2);
		System.out.println(solution3);

		int solution4 = solution.solution(new int[] {2, 3, 4, 1, 1, 1, 1, 5, 6, 7});
		System.out.println((solution4 == 4) + " " + solution4);
		int solution5 = solution.solution(new int[] {1, 2, 1, 3, 1, 1, 4, 1, 5, 1});
		System.out.println((solution5 == 8) + " " + solution5);
		int solution6 = solution.solution(new int[] {1, 2, 1, 3, 1, 4, 1, 5, 1});
		System.out.println((solution6 == 8) + " " + solution6);
		int solution7 = solution.solution(new int[] {1, 1, 1, 3, 3, 3, 5, 5, 5});
		System.out.println((solution7 == 4) + " " + solution7);
		int solution8 = solution.solution(new int[] {0, 0, 0, 2, 3, 4, 3, 5, 3, 1});
		System.out.println((solution8 == 6) + " " + solution8);

	}
	class Solution {
		public int solution(int[] a) {
			int[] counts = new int[a.length];
			int max = 0;
			Queue<Solution.Node> maxHeap = new PriorityQueue<>(((o1, o2) -> o2.count - o1.count));
			for (int i = 0; i < a.length; i++) {
				counts[a[i]] += 1;
			}

			for (int i = 0; i < a.length; i++) {
				if (counts[i] != 0)
					maxHeap.add(new Solution.Node(counts[i], i));
			}
			int answer = 0;
			while (!maxHeap.isEmpty()){
				Solution.Node poll = maxHeap.poll();
				int inter = poll.value;
				if (answer >= poll.count * 2)
					break;
				int size = 1;
				boolean hasInter = a[0] == inter;
				for (int i = 1; i < a.length; i++) {
					if (hasInter) {
						if (a[i] != inter) {
							size += 1;
							hasInter = !hasInter;
						}
					} else {
						if (a[i] == inter) {
							size += 1;
							hasInter = !hasInter && size % 2 != 0;
						} else if (a[i] != inter && size % 2 == 0){
							size += 1;
						}
					}
				}
				if (size % 2 != 0)
					size -= 1;
				answer = Math.max(answer, size);
			}
			return answer;
		}
		static class Node {
			int count;
			int value;

			public Node(int count, int value) {
				this.count = count;
				this.value = value;
			}
		}
	}

}
