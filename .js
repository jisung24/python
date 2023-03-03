// 자바스크립트로 문제풀어보기!
// 감 잃지 않기!
let arr = [2, 3, 4, 5, 6, 7, 8];
//
let filtedArr = arr
  .filter((value) => value <= 8)
  .map((value) => value + 1) // 전체적으로 +1
  .reduce((acc, cur) => {
    // 0 index[0]
    // acc의 값이 없다면 index[0]이고,
    return acc + cur;
  });
// acc가
console.log(filtedArr);

let arr2 = [2, 4, 6, 8, 7, 9, 10];
// 짝수와 홀수 개수구하기.

let arr3 = arr2.reduce(
  (acc, cur) => {
    // acc의 값이 배열이 되는거야!
    console.log(acc[0], cur);
  },
  [0, 0]
);
console.log(arr3);
