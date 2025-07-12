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
        const medications = data.medications;
        medications.forEach(medication => {
            const div = document.createElement("div");
            div.className = "card";
            div.innerHTML = `
                <h3>${medication.name}</h3>
                <p>${medication.reason}</p>
                <p>${medication.frequency}</p>
            `;
            document.getElementById("card-list").appendChild(div);
        })
    })
