class Santa {
  constructor(cols, rows) {
    let startingX = Math.floor(cols/2);
    let startingY = Math.floor(rows/2);
    this.x = startingX;
    this.y = startingY;
  }
  
  move(dir) {
    const directions = {
      "^": { x: 0, y: -1 },
      "v": { x: 0, y: 1 },
      ">": { x: 1, y: 0 },
      "<": { x: -1, y: 0 }
    };

    if (dir in directions) {
      this.x += directions[dir]["x"];
      this.y += directions[dir]["y"];
    } else {
      console.log("INCORRECT MOVEMENT TYPE");
    }
  }
}