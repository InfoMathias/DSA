// https://leetcode.com/problems/max-number-of-k-sum-pairs/

function maxOperations(nums: number[], k: number): number {
    let left = 0;
    let right = nums.length - 1;
    let count = 0;
    nums.sort((a,b) => a-b)

    while(left < right){
        const sum = nums[left] + nums[right];

        if(sum < k){
            left++;
        }
        else if(sum > k){
            right--;
        }
        else {
            left++;
            right--;
            count++;
        }
    }

    return count;
};
