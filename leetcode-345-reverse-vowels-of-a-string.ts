// https://leetcode.com/problems/reverse-vowels-of-a-string/
// Best solution is a regular two pointrs, but I still did it in O(n) so I kept mine

function reverseVowels(s: string): string {
    const vowels = 'aeiou';
    let reversedVowels = [];
    Array.from(s).forEach((char, index) => {
        if(vowels.indexOf(char.toLowerCase()) > -1)
            reversedVowels.push(char);
    });

    reversedVowels = reversedVowels.reverse();

    let sArray = [...s];

    let j = 0
    for(let i = 0; i < sArray.length; i++){
        if(vowels.indexOf(sArray[i].toLowerCase()) > -1){
            sArray[i] = reversedVowels[j];
            j++;
        }
    }

    s = sArray.join('');

    return s;
};
