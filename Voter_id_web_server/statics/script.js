const html5QrCode = new Html5Qrcode("reader");
const config = { fps: 10, qrbox: 250 };

function displayResult(data) {
  const resultBox = document.getElementById("result-box");
  resultBox.className = "success";
  resultBox.style.display = "block";
  resultBox.innerHTML = `
    <strong>✅ Voter Details:</strong>
    <pre>${JSON.stringify(data, null, 2)}</pre>
  `;
  document.getElementById("next-btn").style.display = "inline-block";
}

function displayError(message) {
  const resultBox = document.getElementById("result-box");
  resultBox.className = "error";
  resultBox.style.display = "block";
  resultBox.innerHTML = `
    <strong>❌ Error:</strong>
    <pre>${message}</pre>
  `;
  setTimeout(() => {
    restartScanner();
  }, 3000);
}

function sendQRData(qrData) {
  fetch('/qr-data', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ qr: qrData })
  })
  .then(async res => {
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.error || "Unknown error occurred");
    }
    console.log("✅ Server response:", data);
    displayResult(data);
  })
  .catch(err => {
    console.error("❌ Backend error:", err);
    displayError(err.message || "Something went wrong");
  });
}

function startScanner() {
  html5QrCode.start(
    { facingMode: "environment" },
    config,
    qrCodeMessage => {
      console.log("📦 QR Code detected:", qrCodeMessage);
      html5QrCode.stop().then(() => {
        console.log("📷 Camera stopped after scan");
        document.getElementById("reader").style.display = "none";
        sendQRData(qrCodeMessage);
      });
    },
    errorMessage => {
      // Optional scan error logging
    }
  ).catch(err => {
    console.error("❌ Camera start failed:", err);
  });
}

function restartScanner() {
  document.getElementById("reader").style.display = "block";
  document.getElementById("result-box").style.display = "none";
  document.getElementById("next-btn").style.display = "none";
  startScanner();
}

// Init
startScanner();
