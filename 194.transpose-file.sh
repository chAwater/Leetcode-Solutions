# https://leetcode.cn/problems/valid-phone-numbers/
# Date: 2023.08.05
# Pass/Error/Bug: 1/1/0
# 执行用时：   0 ms, 击败 100.00% 使用 Bash 的用户
# 内存消耗：3.85 MB, 击败   9.31% 使用 Bash 的用户

# Read from the file file.txt and print its transposed content to stdout.
awk '{for(i=1; i<=NF; i++){a[i]=a[i]" "$i;}}END{for(i=1; i<=NF; i++){print a[i];}}' file.txt | sed 's/^ *//'
