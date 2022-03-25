package softeer;

import java.util.*;
import java.io.*;


public class PlayFair
{
	static char[][] board = new char[5][5];
	public static void main(String args[]) throws Exception
	{


		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String msg = in.readLine();
		String key = in.readLine();

		// set board
		Set<Character> used = new HashSet<>();
		List<Character> rest = new LinkedList<>();
		for (int i = 'A'; i <= 'Z'; ++i) {
			if (i == 'J') {
				continue;
			}
			rest.add((char)i);
		}
		int count = 0;
		for (int i = 0; i <key.length(); ++i) {
			Character c = key.charAt(i);
			if (c == 'J')
				c = 'I';
			if (used.contains(c)) continue ;

			board[count / 5][count % 5] = c;
			used.add(c);
			rest.remove(c);
			count++;
		}

		for (Character c : rest) {
			board[count / 5][count % 5] = c;
			count++;
		}
		// for (int i = 0; i < 5; ++i)
		//     System.out.println(Arrays.toString(board[i]));

		// split msg
		List<String> msgs = new ArrayList<>();
		StringBuilder sb = new StringBuilder();
		boolean flag = false;
		for (int i = 0; i < msg.length(); ++i) {
			char c = msg.charAt(i);
			if (c == 'J')
				c = 'I';
			if (!flag) {
				sb.append(c);
				flag = true;
				continue;
			}

			if (sb.charAt(sb.length() - 1) == c) {
				if (sb.charAt(sb.length() - 1) == 'X')
					sb.append('Q');
				else
					sb.append('X');
				msgs.add(sb.toString());
				sb.setLength(0);
				sb.append(c);
			} else {
				sb.append(c);
				msgs.add(sb.toString());
				sb.setLength(0);
				flag = false;
			}
		}
		if (sb.length() != 0) {
			if (sb.charAt(sb.length() - 1) == 'X')
				sb.append('Q');
			else
				sb.append('X');
			msgs.add(sb.toString());
		}
		// System.out.println(msgs);

		sb.setLength(0);
		int notFound = -2;
		for (String word : msgs) {
			int fx = notFound;
			int fy = notFound;
			int sx = notFound;
			int sy = notFound;
			for (int y = 0; y < 5; ++y) {
				for (int x = 0; x < 5; ++x) {
					if (board[y][x] == word.charAt(0)) {
						fx = x;
						fy = y;
					}
					if (board[y][x] == word.charAt(1)) {
						sx = x;
						sy = y;
					}
				}
			}


			if (fy == sy) {
				fx = (fx + 1) % 5;
				sx = (sx + 1) % 5;
			} else if (fx == sx) {
				fy = (fy + 1) % 5;
				sy = (sy + 1) % 5;
			} else {
				int tmp = fx;
				fx = sx;
				sx = tmp;
			}
			sb.append(board[fy][fx]);
			sb.append(board[sy][sx]);
		}

		System.out.println(sb.toString());
	}

}