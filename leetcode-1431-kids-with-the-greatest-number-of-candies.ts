// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const mostCandies = Math.max(...candies);
    return candies.map((candyAmount) => candyAmount + extraCandies >= mostCandies)
};
