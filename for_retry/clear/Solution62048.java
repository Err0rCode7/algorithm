package programmers;

public class Solution62048 {
	public long solution(int w, int h) {

		long count = 0;
		long lw = w;
		long lh = h;
		for (double i = 0; i < w; ++i) {
			double top = ((i + 1) * lh) / lw;
			double bottom = (i * lh) / lw;

			count += Math.ceil(top) - Math.floor(bottom);
		}
		return lw * lh - count;
	}

}