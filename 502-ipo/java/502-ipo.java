import java.util.PriorityQueue;
import java.util.Arrays;

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        // Create an array of projects and sort it based on capital
        int n = profits.length;
        int[][] projects = new int[n][2];
        for (int i = 0; i < n; i++) {
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }
        Arrays.sort(projects, (a, b) -> Integer.compare(a[0], b[0]));

        // Initialize the max-heap for profits
        PriorityQueue<Integer> maxProfitHeap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));

        // Initial capital
        int currentCapital = w;
        int projectIndex = 0;

        for (int i = 0; i < k; i++) {
            // Push all projects that can be started with the current capital to the max profit heap
            while (projectIndex < n && projects[projectIndex][0] <= currentCapital) {
                maxProfitHeap.add(projects[projectIndex][1]);
                projectIndex++;
            }

            // If no project can be done, break the loop
            if (maxProfitHeap.isEmpty()) {
                break;
            }

            // Get the project with the maximum profit
            currentCapital += maxProfitHeap.poll();
        }

        return currentCapital;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int k = 2;
        int w = 0;
        int[] profits = {1, 2, 3};
        int[] capital = {0, 1, 1};
        System.out.println(sol.findMaximizedCapital(k, w, profits, capital)); // Output: 4
    }
}
