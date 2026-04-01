let speechEnabled = false;
let currentSpeech = null;

function toggleSpeech() {
    speechEnabled = !speechEnabled;

    if (!speechEnabled) {
        window.speechSynthesis.cancel();
    } else {
        speakRecommendations(); 
    }

    document.getElementById("voiceBtn").innerText =
        speechEnabled ? "🔊" : "🔇";
}

function speakText(text) {
    if (!speechEnabled) return;

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);
    currentSpeech = speech;

    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}

function speakRecommendations() {
    let movies = document.querySelectorAll(".movie-title");

    if (movies.length === 0) return; 

    let text = "Here are your recommended movies: ";

    movies.forEach(movie => {
        text += movie.innerText + ", ";
    });

    speakText(text);
}

window.onload = function () {
    speakRecommendations();
};

document.addEventListener("keydown", function(event) {
    if (event.code === "Space") {
        window.speechSynthesis.cancel();
    }
});

function toggleReview(id) {
    const box = document.getElementById("review-box-" + id);
    
    box.style.display = (box.style.display === "none") ? "block" : "none";
}