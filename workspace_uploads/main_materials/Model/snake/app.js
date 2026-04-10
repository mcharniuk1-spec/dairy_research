import {
  DIRECTIONS,
  createInitialState,
  setDirection,
  tick,
  togglePause,
} from "./gameLogic.mjs";

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const scoreEl = document.getElementById("score");
const statusEl = document.getElementById("status");
const restartBtn = document.getElementById("restart");
const pauseBtn = document.getElementById("pause");

const cellSize = 20;
const config = { width: 20, height: 20, tickMs: 120 };
canvas.width = config.width * cellSize;
canvas.height = config.height * cellSize;

let state = createInitialState(config);
let timerId = null;

function drawCell(x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
}

function render() {
  ctx.fillStyle = "#f4f4f4";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = "#d8d8d8";
  for (let x = 0; x <= config.width; x += 1) {
    ctx.beginPath();
    ctx.moveTo(x * cellSize, 0);
    ctx.lineTo(x * cellSize, canvas.height);
    ctx.stroke();
  }
  for (let y = 0; y <= config.height; y += 1) {
    ctx.beginPath();
    ctx.moveTo(0, y * cellSize);
    ctx.lineTo(canvas.width, y * cellSize);
    ctx.stroke();
  }

  if (state.food) {
    drawCell(state.food.x, state.food.y, "#d64545");
  }

  state.snake.forEach((cell, idx) => {
    drawCell(cell.x, cell.y, idx === 0 ? "#1d5f2a" : "#2c8a3d");
  });

  scoreEl.textContent = String(state.score);
  if (state.isGameOver) {
    statusEl.textContent = "Game over";
  } else if (state.isPaused) {
    statusEl.textContent = "Paused";
  } else {
    statusEl.textContent = "Running";
  }
}

function step() {
  state = tick(state);
  render();
}

function restart() {
  state = createInitialState(config);
  render();
}

function mapKeyToDirection(key) {
  const normalized = key.toLowerCase();
  if (normalized === "arrowup" || normalized === "w") return DIRECTIONS.up;
  if (normalized === "arrowdown" || normalized === "s") return DIRECTIONS.down;
  if (normalized === "arrowleft" || normalized === "a") return DIRECTIONS.left;
  if (normalized === "arrowright" || normalized === "d") return DIRECTIONS.right;
  return null;
}

function handleDirectionInput(direction) {
  if (!direction) return;
  state = setDirection(state, direction);
  render();
}

window.addEventListener("keydown", (event) => {
  const direction = mapKeyToDirection(event.key);
  if (direction) {
    event.preventDefault();
    handleDirectionInput(direction);
    return;
  }

  if (event.key === " ") {
    event.preventDefault();
    state = togglePause(state);
    render();
    return;
  }

  if (event.key.toLowerCase() === "r") {
    restart();
  }
});

restartBtn.addEventListener("click", restart);
pauseBtn.addEventListener("click", () => {
  state = togglePause(state);
  render();
});

document.querySelectorAll("[data-dir]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const dir = btn.getAttribute("data-dir");
    handleDirectionInput(DIRECTIONS[dir]);
  });
});

window.render_game_to_text = () =>
  JSON.stringify({
    note: "origin=(0,0) at top-left; +x right, +y down",
    width: state.width,
    height: state.height,
    snake: state.snake,
    direction: state.direction,
    food: state.food,
    score: state.score,
    isPaused: state.isPaused,
    isGameOver: state.isGameOver,
  });

window.advanceTime = (ms) => {
  const steps = Math.max(1, Math.round(ms / state.tickMs));
  for (let i = 0; i < steps; i += 1) {
    state = tick(state);
  }
  render();
};

function startLoop() {
  if (timerId) clearInterval(timerId);
  timerId = setInterval(step, state.tickMs);
}

render();
startLoop();
