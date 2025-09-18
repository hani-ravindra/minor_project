document.getElementById('checkBtn').addEventListener('click', () => {
    const url = document.getElementById('urlInput').value;
    if(!url) {
        alert("Enter a URL!");
        return;
    }

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
    })
    .then(res => res.json())
    .then(data => {
        const resultEl = document.getElementById('result');
        resultEl.innerText = data.result;
        resultEl.style.color = data.result.includes("Phishing") ? "red" : "green";
    })
    .catch(err => {
        console.error(err);
        alert("Error connecting to backend!");
    });
});
