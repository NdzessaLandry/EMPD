document.addEventListener("DOMContentLoaded", function () {
  const choix = document.getElementById("id_type_acces");
  const ligne = document.querySelector(".form-row.field-prix");
  if (!choix || !ligne) return;

  function majAffichage() {
    ligne.style.display = choix.value === "PAYANT" ? "" : "none";
  }

  choix.addEventListener("change", majAffichage);
  majAffichage();
});