fetch("data.json")
  .then(res => res.json())
  .then(avatars => {
    const container = document.getElementById("cards");

    avatars.forEach(avatar => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <div class="name">${avatar.name}</div>
        <img src="${avatar.image}" alt="${avatar.name}">
        <div class="stats">
          <div class="stat">🛡️ ${avatar.stats.defense}</div>
          <div class="stat">⚔️ ${avatar.stats.attack}</div>
          <div class="stat">⭐ ${avatar.stats.luck}</div>
        </div>
        <div class="bottom">
          <div class="cash">${avatar.cash} Cash</div>
          <div class="gold">${avatar.gold.toLocaleString()} Gold</div>
        </div>
      `;
      container.appendChild(card);
    });
  });
