package programmers;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Solution42579 {
	public int[] solution(String[] genres, int[] plays) {
		Map<String, Integer> genreSumMap = new HashMap<>();
		Map<String, PriorityQueue<Music>> musicMap = new HashMap<>();

		for (int i = 0; i < plays.length; i++) {
			String genre = genres[i];
			int playCount = plays[i];

			if (!genreSumMap.containsKey(genre)) {
				genreSumMap.put(genre, playCount);
			} else {
				genreSumMap.replace(genre, genreSumMap.get(genre) + playCount);
			}

			Music music = new Music(playCount, i);
			if (!musicMap.containsKey(genre))
				musicMap.put(genre, new PriorityQueue<>(
					((o1, o2) -> o1.playCount != o2.playCount ? o2.playCount - o1.playCount : o1.id - o2.id)));
			musicMap.get(genre).add(music);
		}
		PriorityQueue<Genre> heapQue = new PriorityQueue<>((o1, o2) -> o2.playCount - o1.playCount);
		int resultSize = 0;

		for (Map.Entry<String, Integer> entry : genreSumMap.entrySet()) {
			heapQue.add(new Genre(entry.getKey(), entry.getValue()));
			if (musicMap.get(entry.getKey()).size() >= 2)
				resultSize += 2;
			else
				resultSize += 1;
		}

		int[] answer = new int[resultSize];
		int index = 0;
		while (!heapQue.isEmpty()) {
			Genre genre = heapQue.poll();
			PriorityQueue<Music> musicHeap = musicMap.get(genre.id);
			for (int i = 0; i < 2 && !musicHeap.isEmpty(); i++) {
				Music music = musicHeap.poll();
				answer[index++] = music.id;
			}
		}

		return answer;
	}

	private static class Music {
		int playCount;
		int id;

		public Music(int playCount, int id) {
			this.playCount = playCount;
			this.id = id;
		}
	}

	private static class Genre {
		String id;
		int playCount;

		public Genre(String id, int playCount) {
			this.id = id;
			this.playCount = playCount;
		}
	}
}