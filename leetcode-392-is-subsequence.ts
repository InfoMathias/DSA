// https://leetcode.com/problems/is-subsequence/

function isSubsequence(s: string, t: string): boolean {
    let reader = 0;
    let i = 0;

    while (reader < s.length && i < t.length) {
        if (s[reader] === t[i]) {
            reader++;
        }
        i++;
    }

    return reader === s.length;
}
