Original prompt: Build a classic Snake game in this repo.

- Detected no existing frontend framework/routes in repository; implementing a standalone minimal web page under snake/.
- Constraint: no new dependencies.
- Plan: pure deterministic logic module + minimal UI + lightweight Node tests.

- Implemented standalone Snake web app files:
  - snake/index.html
  - snake/styles.css
  - snake/app.js
  - snake/gameLogic.mjs
- Added Node built-in tests in tests/snake.test.mjs for movement, reverse-input guard, growth, wall/self collision, food placement.

- Ran tests: `node --test tests/snake.test.mjs` (6/6 pass).
- Attempted Playwright skill client run; blocked because `playwright` package is not installed in this repo/environment.
