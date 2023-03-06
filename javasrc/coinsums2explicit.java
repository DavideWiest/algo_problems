package javasrc;
import java.util.ArrayList;
import java.util.Collections;

public class coinsums2explicit {

    public static void main(String[] args) {
        int[] coins = {1,2,5,10,20,50,100,200};
        int target = 200;
        // int[] coins = {5,1};
        // int target = 10;
        ArrayList<ArrayList<Integer>> combsMemoPair = coinsum(coins, target);
        // System.out.println(combsMemoPair);

        System.out.printf("All possible combinations are: %d", combsMemoPair.size());
    }

    public static ArrayList<ArrayList<Integer>> coinsum(int[] coins, int target) {
        ArrayList<ArrayList<Integer>> combinations = new ArrayList<ArrayList<Integer>>();
        if (target <= 0) {
            combinations.add(new ArrayList<Integer>(Collections.nCopies(1, 0)));
        } else {
            for (int coin: coins) {
                if (coin <= target) {
                    for (ArrayList<Integer> subComb: coinsum(coins, target-coin)) {
                        ArrayList<Integer> subComb2 = new ArrayList<Integer>(subComb.size()+1);
                        subComb2.add(coin);
                        for (Integer n: subComb) {
                            subComb2.add(n);
                        }
                        combinations.add(subComb2);
                    }
                }
            }
        }

        return combinations;
    }
}
