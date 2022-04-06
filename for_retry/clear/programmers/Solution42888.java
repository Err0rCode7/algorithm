package programmers;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Solution42888 {
	public String[] solution(String[] record) {

		Map<String, String> idMap = new HashMap<>();
		String in = "님이 들어왔습니다.";
		String out = "님이 나갔습니다.";

		List<Messege> messegeList = new ArrayList<>();
		for (String line : record) {
			StringTokenizer tokenizer = new StringTokenizer(line, " ");
			String cmd = tokenizer.nextToken();
			String id = tokenizer.nextToken();
			String name;
			switch (cmd){
				case "Enter":
					name = tokenizer.nextToken();
					if (idMap.containsKey(id))
						idMap.replace(id, name);
					idMap.put(id, name);
					messegeList.add(new Messege(id, in));
					break;
				case "Leave":
					messegeList.add(new Messege(id, out));
					break;
				case "Change":
					name = tokenizer.nextToken();
					idMap.put(id, name);
					break;
			}
		}

		String[] answer = new String[messegeList.size()];
		int index = 0;
		StringBuilder stringBuilder = new StringBuilder();
		for (Messege messege : messegeList) {
			answer[index++] = stringBuilder
				.append(idMap.get(messege.id))
				.append(messege.cmd)
				.toString();

			stringBuilder.setLength(0);
		}
		return answer;
	}

	private static class Messege {
		String id;
		String cmd;

		public Messege(String id, String cmd) {
			this.id = id;
			this.cmd = cmd;
		}
	}
}
