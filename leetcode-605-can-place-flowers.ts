// https://leetcode.com/problems/can-place-flowers/

function canPlaceFlowers(flowerbed: number[], n: number): boolean {

    flowerbed = [0].concat(flowerbed).concat([0]);
    let length = flowerbed.length;

   for(let i = 1; i < length - 1; i++){
        if(flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] === 0){
            flowerbed[i] = 1;
            n--;
        }

        if(n <= 0) return true;
   }

   return false;
};
