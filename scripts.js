document.getElementById("targetForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let target = document.getElementById("target").value;
    let file = document.getElementById("fileInput").files[0];

    let formData = new FormData();
    formData.append("target", target);
    formData.append("fileInput", file);

    fetch("/run_nuclei_fuzzer", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("output").innerText = data;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
