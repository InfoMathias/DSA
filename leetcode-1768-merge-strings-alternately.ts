// https://leetcode.com/problems/merge-strings-alternately/

function mergeAlternately(word1: string, word2: string): string {
    let mergedWord: string = '';
    const length = Math.max(word1.length,word2.length)

    for(let i=0; i < length; i++){
        mergedWord += (word1?.[i] ?? '') + (word2?.[i] ?? '')
    }

    return mergedWord;
};
