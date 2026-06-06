const form = document.getElementById("flashcardForm");
const flashcardsContainer = document.getElementById("flashcardsContainer");

const quizContainer = document.getElementById("quizContainer");
const startQuizBtn = document.getElementById("startQuizBtn");
let currentQuestionIndex = 0;
let score = 0;
let flashcards = [];
async function getFlashcards() {
  const response = await fetch("http://127.0.0.1:8000/flashcards");
  //await= wait until API response comes back
  // browser sends GET req to backend = GET /flashcards
  const data = await response.json();
  flashcards = data;
  flashcardsContainer.innerHTML = "";
  data.forEach((card) => {
    flashcardsContainer.innerHTML += `
        <div class="flashcard">
        <h3>${card.question}</h3>
        <p>${card.answer}</p>
        <small>${card.category}</small>
        <div class = "card-buttons">
        <button class = "edit-btn">
        Edit </button>
        <button class="delete-btn" onclick = "deleteFlashcard(${card.id})"> Delete </button>
        </div>
        </div>`;
  });
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const question = document.getElementById("question").value;
  const answer = document.getElementById("answer").value;
  const category = document.getElementById("category").value;
  await fetch(
    "http://127.0.0.1:8000/flashcards",

    {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        question,
        answer,
        category,
      }),
    },
  );
  form.reset();
  getFlashcards();
});
getFlashcards();
console.log(startQuizBtn);
startQuizBtn.addEventListener("click", startQuiz);

function startQuiz() {
  currentQuestionIndex = 0;
  score = 0;
  showQuestion();
}
function showQuestion() {
  if (currentQuestionIndex >= flashcards.length) {
    quizContainer.innerHTML = `
        <h2> Quiz finished!!!!</h2>
        <p>Your Score: ${score}/${flashcards.length}</p>
        <button onclick="startQuiz()">
        Restart Quiz
        </button>
        `;
    return;
  }
  const currentCard = flashcards[currentQuestionIndex];
  const progress = (currentQuestionIndex / flashcards.length) * 100;
  quizContainer.innerHTML = `
    <h3>
    Question
    ${currentQuestionIndex + 1}
    of
    ${flashcards.length}
    </h3>
    <div class = "progress-bar">
    <div class = "progress-fill" style="width:${progress}%"></div>
    </div>
    <h2>
    ${currentCard.question}</h2>

    <input
    type = "text"
    id="userAnswer"
    placeholder = "Enter Answer"
    >
    <button class="quiz-btn"
    onclick="checkAnswer()"
    >
    Submit Answer
    </button>
    <p class="score-text">
    Score: ${score}</p>
    `;
}
function checkAnswer() {
  const userAnswer = document.getElementById("userAnswer").value;

  const correctAnswer = flashcards[currentQuestionIndex].answer;

  if (userAnswer.toLowerCase().trim() === correctAnswer.toLowerCase().trim()) {
    score++;
  }
  currentQuestionIndex++;
  showQuestion();
}
async function deleteFlashcard(id) {
  await fetch(`http://127.0.0.1:8000/flashcards/${id}`, {
    method: "DELETE",
  });
  getFlashcards();
}
