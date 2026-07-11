// =========================
// REGISTER USER
// =========================
async function registerUser() {

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (name === "" || email === "" || password === "") {
        alert("Please fill all fields");
        return;
    }

    try {

        const response = await fetch("http://127.0.0.1:8000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });

        const data = await response.json();

        alert(data.message);

        if (response.ok) {
            window.location.href = "login.html";
        }

    } catch (error) {
        console.error(error);
        alert("Cannot connect to backend.");
    }
}


// =========================
// LOGIN USER
// =========================
async function loginUser() {

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (email === "" || password === "") {
        alert("Please fill all fields");
        return;
    }

    try {

        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (data.message === "Login successful") {

            localStorage.setItem("user_id", data.user_id);
            localStorage.setItem("user_name", data.name);

            window.location.href = "dashboard.html";

        } else {

            alert(data.message);

        }

    } catch (error) {
        console.error(error);
        alert("Cannot connect to backend.");
    }
}

// ADD TASK

async function addTask() {

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const status = document.getElementById("status").value;

    const user_id = localStorage.getItem("user_id");

    const response = await fetch("http://127.0.0.1:8000/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            description: description,
            status: status,
            user_id: Number(user_id)
        })
    });

    const data = await response.json();

    alert(data.message);

    loadTasks();

    document.getElementById("title").value = "";
    document.getElementById("description").value = "";
}

// LOAD TASKS

async function loadTasks() {

    const response = await fetch("http://127.0.0.1:8000/tasks");

    const tasks = await response.json();

    let output = "";

    tasks.forEach(task => {

        output += `
            <div style="border:1px solid black;padding:10px;margin:10px;">
                <h3>${task.title}</h3>
                <p>${task.description}</p>
                <p>Status: ${task.status}</p>

                <button onclick="deleteTask(${task.id})">
                    Delete
                </button>
            </div>
        `;

    });

    document.getElementById("taskList").innerHTML = output;

}

// DELETE TASK

async function deleteTask(id) {

    await fetch(`http://127.0.0.1:8000/tasks/${id}`, {
        method: "DELETE"
    });

    loadTasks();

}