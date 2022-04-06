package programmers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution72415 {
	private static List<Card>[] cards;
	private final int[] dx = new int[]{1, 0, -1, 0};
	private final int[] dy = new int[]{0, 1, 0, -1};
	private static int[][] board;
	public int solution(int[][] board, int r, int c) {
		int answer = 0;

		cards = new List[7];
		board = board;
		for (int i = 1; i < 7; i++) {
			cards[i] = new ArrayList<>();
		}

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (board[i][j] != 0) {
					int cardNumber = board[i][j];
					cards[cardNumber].add(new Card(j, i));
				}
			}
		}

		int result = cardPerm(new boolean[7], c, r);

		return result;
	}

	public int cardPerm(boolean[] used, int x, int y) {
		int result = Integer.MAX_VALUE;
		for (int i = 1; i < 7; i++) {
			if (used[i] || cards[i].size() == 0)
				continue;
			used[i] = true;
			Card cardOne = cards[i].get(0);
			Card cardTwo = cards[i].get(1);

			//Order: start -> cardOne -> cardTwo
			int distOneFirst = findDistance(x, y, cardOne) + findDistance(cardOne.x, cardOne.y, cardTwo);
			int distTwoFirst = findDistance(x, y, cardTwo) + findDistance(cardTwo.x, cardTwo.y, cardOne);
			board[cardOne.y][cardOne.x] = 0;
			board[cardTwo.y][cardTwo.x] = 0;
			int ret = Math.min(distTwoFirst + 2 + cardPerm(used, cardOne.x, cardOne.y),
				distOneFirst + 2 + cardPerm(used, cardTwo.x, cardTwo.y));
			board[cardOne.y][cardOne.x] = i;
			board[cardTwo.y][cardTwo.x] = i;
			used[i] = false;

			result = Math.min(result, ret);
		}
		if (result == Integer.MAX_VALUE)
			return 0;
		return result;
	}

	public int findDistance(int x, int y, Card dest) {
		Queue<int[]> que = new LinkedList<>();
		que.add(new int[]{x, y, 0});

		boolean[][] visited = new boolean[5][5];
		visited[y][x] = true;
		while (!que.isEmpty()) {
			int[] poll = que.poll();
			int cost = poll[2];

			if (poll[0] == dest.x && poll[1] == dest.y)
				return cost;
			for (int i = 0; i < 4; i++) {
				int nx = poll[0] + dx[i];
				int ny = poll[1] + dy[i];

				if (!(nx >= 0 && nx < 4 && ny >= 0 && ny < 4)) {
					continue;
				}
				if (!visited[ny][nx]) {
					que.add(new int[] {nx, ny, cost + 1});
					visited[ny][nx] = true;
				}

				if (board[ny][nx] != 0)
					continue;

				int count = 0;
				while (nx + dx[i] >= 0 && nx + dx[i] < 4 && ny + dy[i] >= 0 && ny + dy[i] < 4) {
					nx += dx[i];
					ny += dy[i];
					count += 1;
					if (board[ny][nx] != 0) {
						break;
					}
				}

				if (count > 0 && !visited[ny][nx]) {
					que.add(new int[] {nx, ny, cost + 1});
					visited[ny][nx] = true;
				}

			}

		}
		return 0;
	}

	private static class Card {
		int x;
		int y;

		public Card(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}