export const DIRECTIONS = {
  up: { x: 0, y: -1 },
  down: { x: 0, y: 1 },
  left: { x: -1, y: 0 },
  right: { x: 1, y: 0 },
};

export function samePos(a, b) {
  return a.x === b.x && a.y === b.y;
}

function isOpposite(a, b) {
  return a.x + b.x === 0 && a.y + b.y === 0;
}

export function placeFood(snake, width, height, rng = Math.random) {
  const free = [];
  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const occupied = snake.some((cell) => cell.x === x && cell.y === y);
      if (!occupied) free.push({ x, y });
    }
  }
  if (free.length === 0) return null;
  const idx = Math.min(free.length - 1, Math.floor(rng() * free.length));
  return free[idx];
}

export function createInitialState(config = {}, rng = Math.random) {
  const width = config.width ?? 20;
  const height = config.height ?? 20;
  const startX = Math.floor(width / 2);
  const startY = Math.floor(height / 2);
  const snake = [
    { x: startX, y: startY },
    { x: startX - 1, y: startY },
    { x: startX - 2, y: startY },
  ];
  return {
    width,
    height,
    tickMs: config.tickMs ?? 120,
    snake,
    direction: DIRECTIONS.right,
    queuedDirection: DIRECTIONS.right,
    food: placeFood(snake, width, height, rng),
    score: 0,
    isPaused: false,
    isGameOver: false,
  };
}

export function setDirection(state, nextDirection) {
  if (state.isGameOver) return state;
  if (!nextDirection || isOpposite(state.direction, nextDirection)) return state;
  return {
    ...state,
    queuedDirection: nextDirection,
  };
}

export function togglePause(state) {
  if (state.isGameOver) return state;
  return {
    ...state,
    isPaused: !state.isPaused,
  };
}

export function tick(state, rng = Math.random) {
  if (state.isGameOver || state.isPaused) return state;

  const direction = state.queuedDirection;
  const head = state.snake[0];
  const nextHead = {
    x: head.x + direction.x,
    y: head.y + direction.y,
  };

  const hitWall =
    nextHead.x < 0 ||
    nextHead.x >= state.width ||
    nextHead.y < 0 ||
    nextHead.y >= state.height;

  if (hitWall) {
    return {
      ...state,
      direction,
      isGameOver: true,
    };
  }

  const willEat = state.food && samePos(nextHead, state.food);
  const nextSnake = [nextHead, ...state.snake];
  if (!willEat) {
    nextSnake.pop();
  }

  const hitSelf = nextSnake.slice(1).some((cell) => samePos(cell, nextHead));
  if (hitSelf) {
    return {
      ...state,
      direction,
      isGameOver: true,
    };
  }

  const nextFood = willEat
    ? placeFood(nextSnake, state.width, state.height, rng)
    : state.food;

  const gameCompleted = willEat && nextFood === null;

  return {
    ...state,
    direction,
    snake: nextSnake,
    food: nextFood,
    score: willEat ? state.score + 1 : state.score,
    isGameOver: gameCompleted,
  };
}
