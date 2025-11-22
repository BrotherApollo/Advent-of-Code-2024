class Santa {
  constructor() {
    this.x = 0;
    this.y = 0;
  }

  move(dir) {
    const directions = {
      "^": { x: 0, y: -1 },
      "v": { x: 0, y: 1 },
      ">": { x: 1, y: 0 },
      "<": { x: -1, y: 0 },
    };

    if (dir in directions) {
      this.x += directions[dir].x;
      this.y += directions[dir].y;
    } else {
      console.log("INCORRECT MOVEMENT TYPE");
    }
  }
}
