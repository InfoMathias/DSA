// https://leetcode.com/problems/reverse-words-in-a-string/

function reverseWords(s: string): string {
    let answer:string = '';
    let word = '';
    s += ' '
    Array.from(s).forEach((char, index) => {
        if(char === ' ' || index === s.length - 1){
            answer = word !== '' ? ' ' + word + answer : '' + answer;
            word = '';
        } else {
            word += char
        }
    });

    answer = answer.slice(1);

    return answer;
};
