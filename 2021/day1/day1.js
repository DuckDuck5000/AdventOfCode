var fs = require('fs');
var array = fs.readFileSync('input.txt').toString().split("\n");

function day1(input){
  let count1 = 0;
  let count2 = 0;
  let input1 = input.map(el => parseInt(el));
  for (let i = 0; i < input1.length; i++){
    if (i >= 1 && input1[i] > input1[i-1]){
      count1 += 1;
    }
    if (i >= 3){
      let firstSum = input1[i-3] + input1[i-2] + input1[i-1];
      let secondSum = input1[i-2] + input1[i-1] + input1[i];
      if (secondSum > firstSum){
        count2 += 1;
      }
    }
  
  }
  console.log("Part 1 " + count1);
  console.log("Part 2 " + count2);
}

day1(array);
