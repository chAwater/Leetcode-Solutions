# https://leetcode.cn/problems/valid-phone-numbers/
# Date: 2023.08.04
# Pass/Error/Bug: 1/3/0
# 执行用时：   8 ms, 击败 19.03% 使用 Bash 的用户
# 内存消耗：3.02 MB, 击败 60.66% 使用 Bash 的用户

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^(\([0-9]{3}\)\ |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
