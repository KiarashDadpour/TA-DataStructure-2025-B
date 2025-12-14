#  Stacks Assignment

Implement the class **`LinkedListBasedStack`** similar to the **`ArrayBasedStack`** class.

The class must include the following main methods:
- `push`
- `pop`
- `is_empty`
- `get_top`
- `size`

The stack should follow the LIFO principle and handle underflow conditions properly.
Do not use built-in stack libraries.

---
Use your **LinkedListBasedStack** implementation to check whether parentheses in a given string are **balanced**.
Given a string consisting of parentheses, determine whether the parentheses are **balanced**.

The string may contain the following characters:
- `(` and `)`
- `{` and `}`
- `[` and `]`

A string is considered **balanced** if:
1. Every opening bracket has a matching closing bracket.
2. Brackets are closed in the correct order.
3. No closing bracket appears before its corresponding opening bracket.

###  Examples

| Input String | Output | Explanation |
|-------------|--------|-------------|
| `"()"` | `true` | Simple matching parentheses |
| `"([]{})"` | `true` | All types correctly nested |
| `"(]"` | `false` | Mismatched brackets |
| `"((())"` | `false` | Missing closing parenthesis |
| `"())("` | `false` | Incorrect order of brackets |
| `"{[()]}"` | `true` | Proper nesting |
