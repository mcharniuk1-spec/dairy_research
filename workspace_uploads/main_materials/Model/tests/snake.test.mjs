import test from "node:test";
import assert from "node:assert/strict";

import {
  DIRECTIONS,
  createInitialState,
  placeFood,
  setDirection,
  tick,
} from "../snake/gameLogic.mjs";

test("snake moves one cell per tick", () => {
  let state = createInitialState({ width: 10, height: 10, tickMs: 100 }, () => 0);
  const headBefore = state.snake[0];
  state = tick(state, () => 0);
  assert.equal(state.snake[0].x, headBefore.x + 1);
  assert.equal(state.snake[0].y, headBefore.y);
});

test("reverse direction input is ignored", () => {
  const state = createInitialState({ width: 10, height: 10 }, () => 0);
  const next = setDirection(state, DIRECTIONS.left);
  assert.deepEqual(next.queuedDirection, DIRECTIONS.right);
});

test("eating food grows snake and increases score", () => {
  let state = createInitialState({ width: 10, height: 10 }, () => 0);
  const head = state.snake[0];
  state = {
    ...state,
    food: { x: head.x + 1, y: head.y },
  };

  const next = tick(state, () => 0);
  assert.equal(next.score, state.score + 1);
  assert.equal(next.snake.length, state.snake.length + 1);
});

test("wall collision ends game", () => {
  let state = createInitialState({ width: 4, height: 4 }, () => 0);
  state = {
    ...state,
    snake: [{ x: 3, y: 2 }, { x: 2, y: 2 }, { x: 1, y: 2 }],
    direction: DIRECTIONS.right,
    queuedDirection: DIRECTIONS.right,
  };

  const next = tick(state, () => 0);
  assert.equal(next.isGameOver, true);
});

test("self collision ends game", () => {
  const state = {
    width: 8,
    height: 8,
    tickMs: 120,
    snake: [
      { x: 3, y: 3 },
      { x: 3, y: 4 },
      { x: 2, y: 4 },
      { x: 2, y: 3 },
    ],
    direction: DIRECTIONS.up,
    queuedDirection: DIRECTIONS.down,
    food: { x: 7, y: 7 },
    score: 0,
    isPaused: false,
    isGameOver: false,
  };

  const next = tick(state, () => 0);
  assert.equal(next.isGameOver, true);
});

test("food placement picks only empty cells", () => {
  const snake = [
    { x: 0, y: 0 },
    { x: 1, y: 0 },
    { x: 0, y: 1 },
  ];
  const food = placeFood(snake, 2, 2, () => 0.99);
  assert.deepEqual(food, { x: 1, y: 1 });
});
