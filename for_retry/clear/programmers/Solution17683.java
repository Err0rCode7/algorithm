package programmers;

import java.util.*;

public class Solution17683 {
	public String solution(String m, String[] musicinfos) {
		char[] mArr = m.toCharArray();
		String answer = "(None)";
		int timeSize = 0;
		int startTimeSave = 25 * 36000;
		for (String musicInfo : musicinfos) {
			StringTokenizer st = new StringTokenizer(musicInfo, ",");
			char[] start = st.nextToken().toCharArray();
			char[] end = st.nextToken().toCharArray();
			String name = st.nextToken();
			String info = st.nextToken();

			int startTime = (start[0] - '0') * 600 + (start[1] - '0') * 60 + (start[3] - '0') * 10 + (start[4] - '0');
			int endTime = (end[0] - '0') * 600 + (end[1] - '0') * 60 + (end[3] - '0') * 10 + (end[4] - '0');
			int time = endTime - startTime;
			// System.out.println(time);
			StringBuilder sb = new StringBuilder();

			int length = info.length();
			for (int i = 0; i < info.length(); i++) {
				if (info.charAt(i) == '#')
					length--;
			}
			// System.out.println(length);
			for (int i = 0; i < time / length; i++){
				sb.append(info);
			}

			int idx = 0;
			for (int i = 0; i < time % length; i++) {
				sb.append(info.charAt(idx));
				if (i + 1 < info.length() && info.charAt(idx + 1) == '#')
				{
					sb.append(info.charAt(idx + 1));
					idx++;
				}
				idx++;
			}

			// A#을 하나의 문자로 치환을 하지 않으면 아래 코드 에러
			// String newMelody = sb.toString();
			// if (newMelody.contains(m)) {
			//     if (timeSize < endTime - startTime) {
			//         timeSize = endTime - startTime;
			//         answer = name;
			//     }
			// }

			char[] listenInfo = sb.toString().toCharArray();
			System.out.println(sb.toString());
			for (int i = 0; i < listenInfo.length - mArr.length + 1; i++) {
				boolean equals = true;
				for (int j = 0; j < mArr.length; j++) {
					if ((
						(listenInfo[i + j] != mArr[j])
							|| (((j + 1 < mArr.length && mArr[j + 1] != '#') || j + 1 == mArr.length)
							&& (i + j + 1 < listenInfo.length && (listenInfo[i + j + 1] == '#'))))
					) {
						equals = false;
						break;
					}
				}
				if (equals) {
					if (timeSize < endTime - startTime) {
						timeSize = endTime - startTime;
						answer = name;
					}
					break;
				}
			}
		}

		return answer;
	}
}