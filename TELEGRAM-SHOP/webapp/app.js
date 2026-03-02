let tg = window.Telegram.WebApp;

function buyStars(){
    tg.sendData("stars_250");
}

function buyBoost(){
    tg.sendData("boost_350");
}

function openReviews(){
    alert("Тарифы:\n1 неделя - 150⭐\n1 месяц - 250⭐\nполгода - 500⭐");
}