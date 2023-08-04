# https://leetcode.cn/problems/word-frequency/
# Date: 2023.08.04
# Pass/Error/Bug: 1/2/0
# 执行用时：   0 ms, 击败 100.00% 使用 Bash 的用户
# 内存消耗：3.54 MB, 击败  69.43% 使用 Bash 的用户

# Read from the file words.txt and output the word frequency list to stdout.
sed 's/ \+/\n/g' words.txt | grep -v '^$' | sort | uniq -c | sort -k1nr | awk '{print $2, $1}'
