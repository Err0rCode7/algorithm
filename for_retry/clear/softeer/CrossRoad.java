package softeer;

import java.util.*;
import java.io.*;


public class CrossRoad
{
	static int n;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(in.readLine());
		Queue<Car> carQueue = new LinkedList<>();
		Queue<Car> A = new LinkedList<>();
		Queue<Car> B = new LinkedList<>();
		Queue<Car> C = new LinkedList<>();
		Queue<Car> D = new LinkedList<>();

		Road roadA = new Road(A, D, 1);
		Road roadB = new Road(B, A, 0);
		Road roadC = new Road(C, B, 1);
		Road roadD = new Road(D, C, 0);

		for (int i = 0; i < n; ++i) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			int t = Integer.parseInt(st.nextToken());
			String c = st.nextToken();

			Car car = new Car(t, c.charAt(0), i);
			carQueue.add(car);
		}

		int time = -1;
		int prevTime = -1;
		int lock = -1;
		int[] result = new int[n];
		Arrays.fill(result, -1);
		Road[] roads = new Road[]{roadD, roadC, roadB, roadA};
		while (true) {

			prevTime = time;
			if (!carQueue.isEmpty())
				time = carQueue.peek().time;
			else
				time += 1;

			boolean deadlock = false;
			// System.out.println(prevTime + " " + time);
			for (int t = prevTime; t < time; ++t)
			{
				deadlock = true;
				boolean allEmpty = true;
				lock = -1;
				for (int i = 0; i < 4; ++i) {
					Road road = roads[i];
					if (road.canGo(lock, t)) {
						// System.out.println(i);
						lock = road.getLockNum();
						Car car = road.doGo();
						result[car.idx] = t;
					}

					if (road.rightIsEmpty()) {
						deadlock = false;
					} else {
						allEmpty = false;
					}
				}
				if (deadlock || allEmpty)
					break;
			}

			if (deadlock || (carQueue.isEmpty() && A.isEmpty() && B.isEmpty() && C.isEmpty() && D.isEmpty()))
				break;


			while (!carQueue.isEmpty() && carQueue.peek().time == time) {
				Car car = carQueue.poll();
				if (car.road == 'A') {
					roadA.add(car);
				}
				else if (car.road == 'B') {
					roadB.add(car);
				}
				else if (car.road == 'C') {
					roadC.add(car);
				}
				else if (car.road == 'D') {
					roadD.add(car);
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			out.write(String.valueOf(result[i]));
			out.write('\n');
		}
		out.flush();
		out.close();
		in.close();
	}

	static class Exec {
		Road road;
		int idx;

		public Exec(Road road, int idx) {
			this.road = road;
			this.idx = idx;
		}
	}

	static class Car {
		int time;
		char road;
		int idx;

		public Car(int time, char road, int idx) {
			this.time = time;
			this.road = road;
			this.idx = idx;
		}
	}

	static class Road {
		Queue<Car> que;
		Queue<Car> right;
		int vertical;
		boolean used;

		public Road(Queue<Car> que, Queue<Car> right, int vertical) {
			this.que = que;
			this.right = right;
			this.vertical = vertical;
		}

		public boolean canGo(int lock, int time) {
			if (!(this.vertical == lock || lock == -1))
				return false;
			if (que.isEmpty() || !right.isEmpty())
				return false;
			if (que.peek().time > time)
				return false;
			return true;
		}

		public boolean rightIsEmpty() {
			return right.isEmpty();
		}

		public void add(Car car) {
			que.add(car);
		}

		public int getLockNum() {
			return vertical;
		}

		public Car doGo() {
			this.used = true;
			return que.poll();
		}

		public int size() {
			return que.size();
		}

	}
}