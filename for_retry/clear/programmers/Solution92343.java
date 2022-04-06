package programmers;

import java.util.ArrayList;
import java.util.List;

public class Solution92343 {
	private List<Integer>[] childListArray;
	private int[] info;
	private int maxSheepCnt;
	public int solution(int[] info, int[][] edges) {
		childListArray = new List[info.length];
		maxSheepCnt = 1;
		this.info = info;


		for (int[] edge : edges) {
			if (childListArray[edge[0]] == null)
				childListArray[edge[0]] = new ArrayList<>();
			childListArray[edge[0]].add(edge[1]);
		}
		List<Integer> list = new ArrayList<>();
		list.add(0);
		dfs(0, 1, 0, list);

		return maxSheepCnt;
	}

	private void dfs(int node, int sheepCnt, int wolfCnt, List<Integer> buffer) {

		if (maxSheepCnt < sheepCnt) {
			maxSheepCnt = sheepCnt;
		}
		// System.out.println(node + " " + buffer + sheepCnt + " " + wolfCnt);
		buffer.remove(Integer.valueOf(node));
		if (childListArray[node] != null)
			buffer.addAll(childListArray[node]);
		for (Integer next : buffer) {
			int nextSheepCnt = sheepCnt + (1 ^ info[next]);
			int nextWolfCnt = wolfCnt + info[next];
			if (nextSheepCnt > nextWolfCnt)
				dfs(next, nextSheepCnt, nextWolfCnt, new ArrayList<>(buffer));
		}
	}
}