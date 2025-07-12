    function openNav() {
  document.getElementById("mySidenav").style.width = "750px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

document.getElementById("book-btn").addEventListener("click", () => {
  const promptValue = document.getElementById("prompt").value;
  const responseLink = document.getElementById("response-link");


  fetch("http://localhost:8000/notify", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content: promptValue }),
  })
    .then(res => {
      if (!res.ok) throw new Error("Failed to book");
      return res.json();
    })
    .then(data => {
      if (data.url) {
        responseLink.innerHTML = `<a href="${data.url}" target="_blank">Link here</a>`;
      } else {
        alert("No redirect URL provided.");
      }
    })
    .catch(error => {
      console.error("Error:", error);
      alert("Something went wrong!");
    });
});
