package programmers;

import java.util.*;

public class Solution84021 {
	private final int[] dx = {1, 0, -1, 0};
	private final int[] dy = {0, 1, 0, -1};
	private int n;

	public int solution(int[][] game_board, int[][] table) {
		n = game_board.length;

		boolean[][] visited = new boolean[n][n];
		List<List<Block>> blocksSet = new ArrayList<>();
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				if (table[y][x] == 1 && !visited[y][x]) {
					List<Block> blocks = new ArrayList<>();
					dfs(x, y, blocks, visited, x, y, table, 1);
					blocks.sort((o1, o2) -> (o1.y - o2.y) == 0 ? o1.x - o2.x : o1.y - o2.y);
					blocksSet.add(blocks);
				}
			}
		}
		int answer = 0;
		for (int i = 0; i < 4; i++) {
			if (i != 0)
				game_board = rotate(game_board);

			visited = new boolean[n][n];
			for (int y = 0; y < n; y++) {
				for (int x = 0; x < n; x++) {
					if (game_board[y][x] == 0 && !visited[y][x]) {
						List<Block> blocks = new ArrayList<>();
						dfs(x, y, blocks, visited, x, y, game_board, 0);
						blocks.sort((o1, o2) -> (o1.y - o2.y) == 0 ? o1.x - o2.x : o1.y - o2.y);
						if (blocksSet.contains(blocks)) {
							answer += blocks.size();
							for (Block block : blocks) {
								game_board[y + block.y][x + block.x] = 1;
							}
							blocksSet.remove(blocks);
						}
					}
				}
			}
		}

		return answer;
	}

	private int[][] rotate(int[][] board) {
		int[][] temp = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				temp[j][n - i - 1] = board[i][j];
			}
		}

		return temp;
	}

	private void dfs(int x, int y, List<Block> result, boolean[][] visited, int sx, int sy, int[][] board, int target) {
		result.add(new Block(x - sx, y - sy));
		visited[y][x] = true;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= n || ny >= n || ny < 0 || board[ny][nx] != target || visited[ny][nx])
				continue;
			dfs(nx, ny, result, visited, sx, sy, board, target);
		}
	}

	private static class Block {
		int x;
		int y;

		public Block(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public boolean equals(Object o) {
			if (this == o)
				return true;
			if (o == null || getClass() != o.getClass())
				return false;
			Block block = (Block)o;
			return x == block.x && y == block.y;
		}

		@Override
		public int hashCode() {
			return Objects.hash(x, y);
		}

		@Override
		public String toString() {
			return "Block{" +
				"x=" + x +
				", y=" + y +
				'}';
		}
	}
}
