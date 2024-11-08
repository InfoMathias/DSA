// https://leetcode.com/problems/string-compression/

function compress(chars: string[]): number {
    chars.push('');
    chars.unshift('');
    let charsCount = 1;
    const length = chars.length

    for(let i = 1; i < length; i++){
        if(chars[i] === chars[i-1]){
            charsCount++;
        }
        
        if (chars[i] !== chars[i-1]){
            if(charsCount > 1){
                chars[0] += charsCount;
                charsCount = 1;
            }
            chars[0] += chars[i];
        }
    }

    chars = chars.splice(0, chars.length, ...chars[0].split(''));
    return chars.length;

};
