// Sifariş düyməsinə klik zamanı bildiriş
document.querySelectorAll(".product button").forEach(btn => {
  btn.addEventListener("click", () => {
    alert("Sifariş səbətə əlavə olundu ✅");
  });
});

// Əlaqə formu
const form = document.querySelector("form");
form.addEventListener("submit", e => {
  e.preventDefault();
  alert("Mesajınız göndərildi! Təşəkkür edirik 💙");
  form.reset();
});
