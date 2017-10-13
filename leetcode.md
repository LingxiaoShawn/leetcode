##167. Two Sum II - Input array is sorted
Given an array of **integers** that is already **sorted** in ascending order, find two numbers such that they add up to a specific target number.

You may assume that each input would have **exactly one solution** and you may not use the same element twice.

```java  
// Solution 1: Java. Use Map. Not efficient. But this solution
// can be extended to find all possible pairs.
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] results = new int[2];
        if (numbers == null || numbers.length < 2) 
        	return results;
        	
        double halfTarget = target/2.0;
        Map<Integer, Integer> components = new HashMap();
        boolean put2search = false;
        
        for (int i = 0; i < numbers.length; ++i){
            int number = numbers[i];
            // First save all components of the numbes 
            // lessing than target/2 into a set
            if (!put2search){
                components.put(target - number, i+1);
                if (number >= halfTarget){
                    put2search = true;
                    if (number != halfTarget){
                        i--;
                    }
                }
            }else{
            // Then look up the set when looking at the 
            // numbers bigger than target/2
                if(components.containsKey(number)){
                    results[0] = components.get(number);
                    results[1] = i+1;
                    return results;
                }
            }
        }
        return results;
    }
}

```

```java
// Solution 2: Java. Without using map. 
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // check existence of solution
        if (numbers == null || numbers.length <= 0) return null;
        double halfTarget = target/2.0;
        if (numbers[0] > halfTarget || numbers[numbers.length - 1] < halfTarget) return null;
        // search solution
        int left = 0, right = numbers.length - 1;
        while (left < right){
            int estimator = target - numbers[left];
            while(numbers[right] > estimator) --right;
            if (numbers[right] == estimator){
                return new int[]{left+1, right+1};
            }
            ++ left;
        }
        return null;
    }
}
```
```python
# Solution 3: python. 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right :
            right_target = target - numbers[left]
            while numbers[right] > right_target:
                right -= 1
            if numbers[right] == right_target:
                return [left+1, right+1]
            left += 1
        return NULL
```