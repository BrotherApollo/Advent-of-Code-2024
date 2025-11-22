let rows;
let cols;
let size = 7;
let data;
let step = 0;
let visited = new Map();
let santaTurn = true;
let santa;
let robot;

function preload() {
  data = loadStrings("data.txt");
}

function drawGrid() {
  background(50,50,50);
  fill(50,50,50);
  for (let i=0; i<cols; i++) {
    for (let j=0; j<rows; j++) {
      rect(i*size, j*size, size, size);
    }
  }
}

function setup() {
  createCanvas(1000, 1000);
  cols = width/size;
  rows = height/size;
  santa = new Santa(cols, rows);
  robot = new Santa(cols, rows);
  data = data[0];
  drawGrid();
  
  // Process all movements at once
  let santaTurn = true;
  for (let i = 0; i < data.length; i++) {
    let dir = data[i];
    if (santaTurn) {
      santa.move(dir);
      visited.set(santa.x + "," + santa.y, 1);
    } else {
      robot.move(dir);
      visited.set(robot.x + "," + robot.y, 1);
    }
    santaTurn = !santaTurn;
  }
  
  santa = new Santa(cols, rows);
  robot = new Santa(cols, rows);
  
  console.log(visited.size);
}

function draw() {
  
  // step logic
  let dir = data[step];
  // console.log(dir);
  if (santaTurn){
    santa.move(dir);
  } else {
    robot.move(dir);
  }
  santaTurn = !santaTurn
  
  step++;
  if (step+1 > data.length) {
    console.log("we did it");
    console.log(visited.size);
    step = 0;
    
    visted = new Map();
    santa = new Santa(cols, rows);
    robot = new Santa(cols, rows);
  }  
  //Draw Trail
  fill(200, 200, 255);
  for (let [key, value] of visited.entries()) {
    let [x,y] = key.split(",").map(Number);
    rect(x*size, y*size, size, size);
  }
  
  // Draw Santa
  fill(255, 0, 0);
  rect(santa.x*size, santa.y*size, size, size)
  
  // Draw robot
  fill(0, 0, 255);
  rect(robot.x*size, robot.y*size, size, size);

}