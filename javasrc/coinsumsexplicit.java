package javasrc;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class coinsumsexplicit {

    public static void main(String[] args) {
        int[] coins = {1,2,5,10,20,50,100,200};
        int target = 200;
        // int[] coins = {5,1};
        // int target = 10;
        HashMap<Integer, ArrayList<ArrayList<Integer>>> startingMemo = new HashMap<Integer, ArrayList<ArrayList<Integer>>>();
         Pair<ArrayList<ArrayList<Integer>>, HashMap<Integer, ArrayList<ArrayList<Integer>>>> combsMemoPair = coinsum(coins, target, startingMemo);
        System.out.println(combsMemoPair.second);

        System.out.printf("All possible combinations are: %d", combsMemoPair.first.size());
    }

    public static Pair<ArrayList<ArrayList<Integer>>, HashMap<Integer, ArrayList<ArrayList<Integer>>>> coinsum(int[] coins, int target, HashMap<Integer, ArrayList<ArrayList<Integer>>> memo) {
        ArrayList<ArrayList<Integer>> combinations = new ArrayList<ArrayList<Integer>>();
        if (target <= 0) {
            combinations.add(new ArrayList<Integer>(Collections.nCopies(1, 0)));
        } else {
            for (int coin: coins) {
                if (coin <= target) {
                    if (!memo.containsKey(target-coin)) {
                        memo = coinsum(coins, target-coin, memo).second;
                    }
                    for (ArrayList<Integer> subComb: memo.get(target-coin)) {
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

        memo.put(target, combinations);

        return new Pair(combinations, memo);
    }
}
