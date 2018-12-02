const fs = require('fs')

file = fs.readFileSync('input2.txt', {
  encoding: "utf-8"
});
input = file.split('\n')

let doubles = 0
let triples = 0
for (let line of input) {
  let lineMap = new Map()
  for (let char of line) {
    if (lineMap.has(char)) {
      lineMap.set(char, lineMap.get(char) + 1)
    } else {
      lineMap.set(char, 1)
    }
  }

  let hasDouble = false
  let hasTriple = false

  for (let value of lineMap.values()) {
    if (value === 2) {
      hasDouble = true
    } else if (value === 3) {
      hasTriple = true
    }
  }

  if (hasDouble) doubles += 1
  if (hasTriple) triples += 1
}

console.log(doubles, triples)
console.log(doubles * triples)