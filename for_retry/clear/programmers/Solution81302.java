package programmers;

public class Solution81302 {
	private final int[] dx = {1, 0, -1, 0};
	private final int[] dy = {0, 1, 0, -1};

	public int[] solution(String[][] places) {
		int n = places.length;

		int[] answer = new int[n];
		for (int i = 0; i < n; i++) { // 대기실 번호
			if (checkWaitingRoom(places[i], n))
				answer[i] = 1;
		}
		return answer;
	}

	private boolean checkWaitingRoom(String[] place, int n) {
		for (int y = 0; y < n; y++) { // 대기실 y
			for (int x = 0; x < n; x++) { // 대기실 x
				char c = place[y].charAt(x);

				if (c == 'P' || c == 'O') {
					int pCount = 0;
					for (int i = 0; i < 4; i++) {
						int nx = x + dx[i];
						int ny = y + dy[i];

						if (nx < 0 || nx >= n || ny >= n || ny < 0) continue;
						char target = place[ny].charAt(nx);
						if (target != 'P')
							continue;
						if (c == 'P')
							return false;
						else
							pCount += 1;
					}

					if (pCount > 1)
						return false;
				}
			}
		}

		return true;
	}
}
