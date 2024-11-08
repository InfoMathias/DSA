// https://leetcode.com/problems/container-with-most-water/

function maxArea(height: number[]): number {
    let maxArea = 0;
    let length = height.length;
    let i = 0;
    let j = length - 1;

    while(i < j){
        const area = (j-i)*Math.min(height[i],height[j]);

        if(area > maxArea){
            maxArea = area;
        }

        if(height[i] >= height[j]){
            j--;
        } 
        else{
            i++;
        }
    }

    return maxArea;
};
