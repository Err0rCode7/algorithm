package programmers;

public class Solution12979 {
	public int solution(int n, int[] stations, int w) {

		int stationIndex = 0;
		int end = 1;
		int addCount = 0;
		while (true){
			if (end > n)
				break;
			if (stations.length > stationIndex &&
				stations[stationIndex] - w <= end && end <= stations[stationIndex] + w) {
				end = stations[stationIndex] + w + 1;
				++stationIndex;
				continue;
			}

			end += 2 * w + 1;
			addCount += 1;
		}

		return addCount;
	}
}
