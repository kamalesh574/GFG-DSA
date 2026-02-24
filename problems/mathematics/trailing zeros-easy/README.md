# 🔢 Factorial Trailing Zeroes

## 📝 Problem Statement

Given an integer `n`, return the number of trailing zeroes in `n!`.

Trailing zeroes are the zero digits that appear at the end of a number.

---

## 📌 Examples

Input: n = 3  
Output: 0  
Explanation: 3! = 6 → No trailing zero  

Input: n = 5  
Output: 1  
Explanation: 5! = 120 → One trailing zero  

Input: n = 10  
Output: 2  
Explanation: 10! = 3628800 → Two trailing zeroes  

---

## 🚀 Approach (Efficient Mathematical Method)

### 🔹 Key Idea

A trailing zero is produced by a factor of **10**.  

Since:

10 = 2 × 5  

In factorials, there are always more factors of **2** than **5**.  
So, the number of trailing zeroes depends on the number of **5s** in the prime factorization.

### 🔹 Steps

1. Count how many multiples of 5 are present.
2. Add how many multiples of 25 (extra 5).
3. Add how many multiples of 125, and so on.
4. Continue while `n > 0`.

---

## 💻 Java Implementation

```java
class Solution {
    public int trailingZeroes(int n) {

        int count = 0;

        for (int i = 5; i <= n; i *= 5) {
            n = n / 5;
            count += n;
        }

        return count;
    }
}

```

---



⏱ Time & Space Complexity

Time Complexity: O(log₅ n)

Space Complexity: O(1)

---