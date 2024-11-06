// https://leetcode.com/problems/move-zeroes/

/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    let l = 0;
    let r = 0;
    let length = nums.length;


    while (r < length && l < length) {
        if(nums[r] === 0){
            r++;
        }
        else if(nums[l] !== 0 ){
            l++;
        }
        else if(l < r) {
            const temp = nums[l]
            nums[l] = nums[r];
            nums[r] = temp;
        }
        else {
            r++;
        }
    } 
};
