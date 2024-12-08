var fs = require('fs');
var array = fs.readFileSync('input.txt').toString().split("\n");

function part1(array){
  let horz = 0;
  let vert = 0;

  for (let i = 0; i < array.length; i++){
    let temp = array[i].split(' ');
    let dir = temp[0];
    let delta = parseInt(temp[1]);

    if (dir == "forward"){
      horz += delta;
    } else if (dir == "down"){
      vert += delta;
    } else {
      vert -= delta;
    }
    
  }
  return vert*horz
}

function part2(array){
  let horz = 0;
  let vert = 0;
  let aim = 0;

  for (let i = 0; i < array.length; i++){
    let temp = array[i].split(' ');
    let dir = temp[0];
    let delta = parseInt(temp[1]);

    if (dir == "forward"){
      horz += delta;
      vert += (aim*delta)
    } else if (dir == "down"){
      aim += delta;
    } else {
      aim -= delta;
    }
    
  }
  return vert*horz
}


console.log(part1(array));
console.log(part2(array));
