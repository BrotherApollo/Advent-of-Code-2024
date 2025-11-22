let rows;
let cols;
let size = 7;
let data;
let step = 0;
let visited = new Map();
let santaTurn = true;
let santa;
let robot;
let bounds;

function preload() {
  data = loadStrings("data.txt");
  // data = [">><<>>>>>>"];
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

function processMovements() {
  santa = new Santa();
  robot = new Santa();
  bounds = {
    minX: 0,
    maxX: 0,
    minY: 0,
    maxY: 0,
  };
  let lastMove = {x: 0, y: 0};
  let santaTurn = true;
  
  for (let i = 0; i < data.length; i++) {
    let dir = data[i];
    
    if (santaTurn) {
      santa.move(dir);
      lastMove.x = santa.x;
      lastMove.y = santa.y;
    } else {
      robot.move(dir);
      lastMove.x = robot.x;
      lastMove.y = robot.y;
    }
    visited.set(lastMove.x + "," + lastMove.y, 1);
    santaTurn = !santaTurn;
    
    if (lastMove.x < bounds.minX) {
      bounds.minX = lastMove.x;
      
    } else if (lastMove.x > bounds.maxX) {
      bounds.maxX = lastMove.x;
    }
    if (lastMove.y < bounds.minY) {
      bounds.minY = lastMove.y;
    } else if (lastMove.y > bounds.maxY) {
      bounds.maxY = lastMove.y;
    }
  }
  
  // Log AFTER loop completes
  console.log(`X: ${bounds.minX} - ${bounds.maxX}; Y: ${bounds.minY} - ${bounds.maxY}`);
  console.log(bounds);
}

function setup() {
  data = data[0];
  let dimentions = processMovements();
  createCanvas(
    (bounds.maxX - bounds.minX)*size,
    (bounds.maxY - bounds.minY)*size
  );
  cols = width/size;
  rows = height/size;
  console.log(data.length);
  drawGrid();
  santa = new Santa();
  robot = new Santa();
  console.log(`Unique Houses visited: ${visited.size}`);
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
    // Restarting the animation
    step = 0;
    visted = new Map();
    santa = new Santa();
    robot = new Santa();
  }
  
  // offset
  let offsetX = Math.abs(bounds.minX);
  let offsetY = Math.abs(bounds.minY);
  //Draw Trail
  fill(200, 200, 255);
  for (let [key, value] of visited.entries()) {
    let [x,y] = key.split(",").map(Number);
    rect((x+offsetX)*size, (y+offsetY)*size, size, size);
  }
  
  // Draw Santa
  fill(255, 0, 0);
  rect((santa.x+offsetX)*size, (santa.y+offsetY)*size, size, size)
  
  // Draw robot
  fill(0, 0, 255);
  rect((robot.x+offsetX)*size, (robot.y+offsetY)*size, size, size);

}