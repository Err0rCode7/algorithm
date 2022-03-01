package programmers;

public class Solution42883 {
	public String solution(String number, int k) {
		// Deque<Character> stack = new LinkedList<>();

		StringBuilder stack = new StringBuilder();
		char prev = number.charAt(0);
		stack.append(prev);
		for (int i = 1; i < number.length(); i++) {
			char next = number.charAt(i);

			if (k == 0) {
				for (int j = i; j < number.length(); j++) {
					next = number.charAt(j);
					stack.append(next);
				}
				break;
			}

			if (prev < next) {
				while (k != 0 && prev < next && stack.length() > 0) {
					stack.setLength(stack.length() - 1);
					if (stack.length() > 0)
						prev = stack.charAt(stack.length() - 1);
					else
						prev = '0';
					k -= 1;
				}
			}
			stack.append(next);
			prev = next;
		}

		if (k != 0) {
			stack.setLength(stack.length() - k);
		}
		return stack.toString();
	}
	private static class Solution2 {
		public String solution(String number, int k) {
			if (number.length() == k)
				return "";

			Node head = null;
			Node cur = null;
			for (int i = 0; i < number.length(); i++) {
				char value = number.charAt(i);
				if (head == null) {
					head = new Node(value);
					cur = head;
					continue;
				}

				cur.add(new Node(value));
				cur = cur.next;
			}
			Node prev = head;
			cur = head.next;
			int count = 0;
			while (cur != null && count != k) {
				if (prev != null && cur.value > prev.value) {
					cur.removePrev();
					prev = cur.prev;
					count += 1;
				} else {
					if (cur.next != null) {
						cur = cur.next;
						prev = cur.prev;
					} else {
						break;
					}
				}
				if (prev == null)
					head = cur;
			}

			StringBuilder stringBuilder = new StringBuilder();
			int nodeCount = 0;
			// k -= count;
			while (head != null) {
				if (nodeCount + k >= number.length() + count)
					break;
				stringBuilder.append(head.value);
				head = head.next;
				nodeCount += 1;
			}

			return stringBuilder.toString();
		}

		public static class Node {
			Node prev;
			Node next;
			char value;

			public Node(char value) {
				this.value = value;
			}

			public void add(Node next) {
				this.next = next;
				next.prev = this;
			}

			public Node removeNext() {
				if (this.next == null)
					return null;
				Node removed = this.next;
				this.next = removed.next;
				this.next.prev = this;
				return removed;
			}

			public Node removePrev() {
				if (this.prev == null) {
					return null;
				}
				Node removed = this.prev;
				this.prev = removed.prev;
				if (this.prev != null)
					this.prev.next = this;
				return removed;
			}
		}
	}
}