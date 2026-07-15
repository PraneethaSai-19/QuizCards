const loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", login);

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  const response = await fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: formData,
  });
  const data = await response.json();
  localStorage.setItem("token", data.access_token);
  window.location.href = "index.html";
  console.log(data);
}
