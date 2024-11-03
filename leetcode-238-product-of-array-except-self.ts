// https://leetcode.com/problems/product-of-array-except-self/

function productExceptSelf(nums: number[]): number[] {
    const answer = new Array(nums.length).fill(null)
    let prefixRight = 1
    let prefixLeft = 1

    let left = []
    let right = []

    for (let i = 0; i < nums.length; i++) {
        left[i] = prefixLeft
        prefixLeft = prefixLeft * nums[i]
    }
    for (let i = nums.length - 1; i >= 0; i--) {
        right[i] = prefixRight
        prefixRight = right[i] * nums[i]
    }
    for (let i = 0; i < nums.length; i++) {
        answer[i] = left[i] * right[i]
    }

    return answer
};
