import java.util.*;

public class Solution {
    public String sortVowels(String s) {
        // Define the set of vowels
        Set<Character> vowelSet = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 
                                                               'A', 'E', 'I', 'O', 'U'));

        // List to store the vowels found in the string
        List<Character> vowels = new ArrayList<>();

        // Extract vowels from the string
        for (char c : s.toCharArray()) {
            if (vowelSet.contains(c)) {
                vowels.add(c);
            }
        }

        // Sort the vowels
        Collections.sort(vowels);

        // Iterator for the sorted vowels
        Iterator<Character> vowelIterator = vowels.iterator();

        // StringBuilder to build the result string
        StringBuilder result = new StringBuilder();

        // Reconstruct the string with sorted vowels
        for (char c : s.toCharArray()) {
            if (vowelSet.contains(c)) {
                result.append(vowelIterator.next());
            } else {
                result.append(c);
            }
        }

        return result.toString();
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "lEetcOde";
        System.out.println(sol.sortVowels(s));  // Output: "lEOtcede"
    }
}
