// https://leetcode.com/problems/increasing-triplet-subsequence/

function increasingTriplet(nums: number[]): boolean {
    if(nums.length < 3) return false;

    let iValueMin = Infinity;
    let jValueMin = Infinity;


    for(let num of nums){
        if(num <= iValueMin){
            iValueMin = num;
        } 
        else if (num <= jValueMin){
            jValueMin = num;
        }
        else{
            return true;
        }
    }
    
    return false;
};
