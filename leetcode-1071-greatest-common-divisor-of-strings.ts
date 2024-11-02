// https://leetcode.com/problems/greatest-common-divisor-of-strings/

const gcdOfStrings = function (str1: string, str2: string): string {
    return (str1 + str2 === str2 + str1) ? str1.substring(0, gcd(str1.length, str2.length)) : "";
};

const gcd = function (a: number, b: number): number {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};
