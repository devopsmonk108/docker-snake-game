from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Snake Game</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                font-family: 'Segoe UI', sans-serif;
                color: #fff;
            }
            h1 { margin-bottom: 5px; }
            #score { margin-bottom: 10px; font-size: 1.2rem; color: #00c896; }
            #speedControl { margin-bottom: 15px; display: flex; align-items: center; gap: 10px; }
            #speedControl label { font-size: 0.95rem; color: #cfd8dc; }
            canvas {
                background: #111;
                border: 4px solid #00c896;
                border-radius: 10px;
            }
            #msg { margin-top: 15px; color: #cfd8dc; }
        </style>
    </head>
    <body>
        <h1>🐍 Snake</h1>
        <div id="score">Score: 0</div>

        <div id="speedControl">
            <label for="speed">Speed:</label>
            <input type="range" id="speed" min="40" max="300" value="120" step="10">
            <span id="speedLabel">120 ms</span>
        </div>

        <canvas id="game" width="400" height="400"></canvas>
        <div id="msg">Use arrow keys to move. Press Space to restart.</div>

        <script>
            const canvas = document.getElementById("game");
            const ctx = canvas.getContext("2d");
            const box = 20;
            let snake, direction, food, score, gameOver, loop;
            let speed = 120;

            const speedSlider = document.getElementById("speed");
            const speedLabel = document.getElementById("speedLabel");

            speedSlider.addEventListener("input", () => {
                speed = parseInt(speedSlider.value);
                speedLabel.innerText = speed + " ms";
                restartLoop();
            });

            function restartLoop() {
                if (loop) clearInterval(loop);
                if (!gameOver) loop = setInterval(draw, speed);
            }

            function init() {
                snake = [{ x: 9 * box, y: 9 * box }];
                direction = null;
                score = 0;
                gameOver = false;
                placeFood();
                document.getElementById("score").innerText = "Score: 0";
                restartLoop();
            }

            function placeFood() {
                food = {
                    x: Math.floor(Math.random() * (canvas.width / box)) * box,
                    y: Math.floor(Math.random() * (canvas.height / box)) * box
                };
            }

            document.addEventListener("keydown", (e) => {
                if (e.key === " " && gameOver) { init(); return; }
                if (e.key === "ArrowLeft" && direction !== "RIGHT") direction = "LEFT";
                else if (e.key === "ArrowUp" && direction !== "DOWN") direction = "UP";
                else if (e.key === "ArrowRight" && direction !== "LEFT") direction = "RIGHT";
                else if (e.key === "ArrowDown" && direction !== "UP") direction = "DOWN";
            });

            function draw() {
                if (gameOver) return;

                ctx.fillStyle = "#111";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#ff4d4d";
                ctx.fillRect(food.x, food.y, box, box);

                for (let i = 0; i < snake.length; i++) {
                    ctx.fillStyle = i === 0 ? "#00c896" : "#00966e";
                    ctx.fillRect(snake[i].x, snake[i].y, box - 2, box - 2);
                }

                if (!direction) return;

                let head = { x: snake[0].x, y: snake[0].y };
                if (direction === "LEFT") head.x -= box;
                if (direction === "UP") head.y -= box;
                if (direction === "RIGHT") head.x += box;
                if (direction === "DOWN") head.y += box;

                if (
                    head.x < 0 || head.x >= canvas.width ||
                    head.y < 0 || head.y >= canvas.height ||
                    snake.some(s => s.x === head.x && s.y === head.y)
                ) {
                    endGame();
                    return;
                }

                snake.unshift(head);

                if (head.x === food.x && head.y === food.y) {
                    score++;
                    document.getElementById("score").innerText = "Score: " + score;
                    placeFood();
                } else {
                    snake.pop();
                }
            }

            function endGame() {
                gameOver = true;
                clearInterval(loop);
                ctx.fillStyle = "rgba(0,0,0,0.7)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = "#fff";
                ctx.font = "24px Segoe UI";
                ctx.textAlign = "center";
                ctx.fillText("Game Over", canvas.width / 2, canvas.height / 2 - 10);
                ctx.font = "16px Segoe UI";
                ctx.fillText("Press Space to restart", canvas.width / 2, canvas.height / 2 + 20);
            }

            init();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)