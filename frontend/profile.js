function openNav() {
  document.getElementById("mySidenav").style.width = "750px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

fetch("http://localhost:8000/summarize", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        "session_id": "11901873742259810244555103576895445913"
    })
})
    .then(response => {
        if (!response.ok) throw new Error("Network error");
        return response.json();
    }).then(data => {
        const todos = data.things_to_do;

        todos.forEach(todo => {
            const div = document.createElement("div");
            div.className = "card";
            div.innerHTML = `
                <h3>${todo.what}</h3>
                <p>${todo.reason}</p>
            `;
            document.getElementById("card-list").appendChild(div);
        });

        const div = document.createElement("div");
        // div.className = "card";
        div.innerHTML = `
            <p>${data.diagnosis}</p>
        `
        document.getElementById("diagnosis").appendChild(div);
    })
