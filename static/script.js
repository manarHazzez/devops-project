document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const city = document.querySelector('input[name="city"]').value;
    
    const response = await fetch(`/weather?city=${city}`);
    const data = await response.json();
    
    if (data.error) {
        alert(data.error);
    } else {
        document.querySelector('#weather').innerHTML = `
            <h2>Météo pour ${data.city}</h2>
            <p>Température : ${data.temperature}°C</p>
            <p>Description : ${data.description}</p>
            <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png" alt="Weather icon">
        `;
    }
});
