# 🧩 Palindrome

## 📝 Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward.

---

## 📌 Examples

Input: x = 121  
Output: true  

Input: x = -121  
Output: false  

Input: x = 10  
Output: false  

---

## 🚀 Approach Reverse the Entire Number

### 🔹 Explanation

- Negative numbers are not palindromes.
- Store the original number.
- Reverse the number using:
  - `% 10` to extract the last digit
  - `/ 10` to remove the last digit
- Compare the reversed number with the original number.
- If both are equal → return `true`, otherwise `false`.

---

## 💻 Java Implementation

```java
class Solution {
    public boolean isPalindrome(int x) {

        // Negative numbers are not palindrome
        if (x < 0) return false;

        int original = x;
        int reversed = 0;

        while (x != 0) {
            int lastDigit = x % 10;
            reversed = reversed * 10 + lastDigit;
            x = x / 10;
        }

        return original == reversed;
    }
}

---

⏱ Time & Space Complexity

Time Complexity: O(log₁₀ n)

Space Complexity: O(1)

---