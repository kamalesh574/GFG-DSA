# 🧮 Factorial

## 📝 Problem Statement

Given a non-negative integer `n`, return its factorial.

The factorial of a number is the product of all positive integers less than or equal to `n`.

Factorial is denoted as `n!`.

---

## 📌 Examples

Input: n = 5  
Output: 120  
Explanation: 5! = 5 × 4 × 3 × 2 × 1 = 120  

Input: n = 0  
Output: 1  
Explanation: 0! = 1  

Input: n = 3  
Output: 6  

---

## 🚀 Approach (Iterative Method)

### 🔹 Explanation

- Factorial of 0 is 1.
- Initialize a variable `result = 1`.
- Multiply numbers from `1` to `n`.
- Return the final result.

---

## 💻 Java Implementation (Iterative)

```java
class Solution {
    public long factorial(int n) {

        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }

        long result = 1;

        for (int i = 1; i <= n; i++) {
            result *= i;
        }

        return result;
    }
}

---
🔁 Recursive Approach (Optional)
🔹 Idea

Factorial can also be defined as:

n! = n × (n - 1)!
Base Case: 0! = 1

---

```

class Solution {
    public long factorial(int n) {

        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }

        if (n == 0 || n == 1) {
            return 1;
        }

        return n * factorial(n - 1);
    }
}

```

---
---

⏱ Time & Space Complexity

Iterative:

Time Complexity: O(n)

Space Complexity: O(1)

Recursive:

Time Complexity: O(n)

Space Complexity: O(n) (due to recursion stack)

---