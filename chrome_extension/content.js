const url = window.location.href;

fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url })
})
.then(res => res.json())
.then(data => {
    if(data.result.includes("Phishing")) {
        alert("⚠️ Phishing Website Detected!");
    } else {
        console.log("✅ Legitimate site");
    }
})
.catch(err => console.error(err));
