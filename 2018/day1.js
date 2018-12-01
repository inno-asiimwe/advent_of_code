const fs = require('fs')

file = fs.readFileSync('input1.txt', {encoding: "utf-8"});
input = file.split('\n')


sum = 0
seen = {}
let hasSeen = false
while (!hasSeen) {
  for (let line of input) {
    sum += Number(line)
    if (!seen[sum]) {
       seen[sum] = true
    } else {
      hasSeen = true;
      break;
    }
  }
}

console.log(sum)