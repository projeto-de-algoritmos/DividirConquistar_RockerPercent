document.addEventListener("DOMContentLoaded", function() {
    var sortable = Sortable.create(document.getElementById("sortable"));

  
    document.getElementById("submit-button").addEventListener("click", function() {
      var orderedImages = Array.from(document.querySelectorAll("#sortable li h2")).map(function(item) {
        return item.getAttribute("alt");
      });
  
      // Enviar a lista ordenada de referencia das imagens para o backend
      fetch("/submit", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ orderedImages: orderedImages })
      })
      .then(response => {
        return response.json();
      })
      .then(data => {
        // Atualizar  na página
        var resultDiv = document.getElementById("result");
        resultDiv.textContent = "Você é " + data.result + " % Rockeiro!";
      })
      .catch(error => {
        console.log("Ocorreu um erro: ", error);
      });
    });
  });
  