
    function shareArticle(slug) {
        // Appel AJAX pour incrémenter le nombre de partages côté serveur
        fetch(`/increment_shares/${slug}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',  // Assurez-vous d'inclure le jeton CSRF
            },
        })
        .then(response => response.json())
        .then(data => {
            // Afficher la boîte de dialogue avec les boutons de partage
            const shareDialog = confirm(`Shared ${data.shares} times! Share on social media?`);
            if (shareDialog) {
                // Ajoutez ici la logique pour ouvrir la boîte de dialogue de partage
                // Vous pouvez utiliser des fenêtres modales ou des bibliothèques JS pour cela
            }
        });
    }

