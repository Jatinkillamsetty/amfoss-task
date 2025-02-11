document.getElementById('weatherForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const location = document.getElementById('locationInput').value;
    const apiKey = 'c1b06b514cf453a07a4f9c755b344c96'; 
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        console.error('Error fetching weather data:', error);
        document.getElementById('weatherData').innerText = 'Failed to fetch weather data. Please try again.';
    }
});

function displayWeather(data) {
    if (data.cod === 200) {
        const weatherDataDiv = document.getElementById('weatherData');
        weatherDataDiv.innerHTML = `
            <p>Location: ${data.name}</p>
            <p>Temperature: ${data.main.temp}°C</p>
            <p>Weather: ${data.weather[0].description}</p>
        `;
        
    } else {
        document.getElementById('weatherData').innerText = 'Location not found. Please try again.';
    }
}
