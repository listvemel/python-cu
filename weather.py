

def get_message(temperature: float, humidity: float, wind_speed: float, rain: float) -> str:
    if temperature > 0 and wind_speed < 20 and humidity < 0.5 and rain < 0.5:
        return "Погодка просто топчик, самое время идти на Патрики!"
    if temperature < 20 and wind_speed > 20 and humidity > 0.5 and rain < 0.5:
        return "Треш, сидим дома"
    if temperature < 0 and wind_speed < 20 and humidity < 0.5 and rain < 0.5:
        return "Немного прохладно, можно пойти посидеть в кофейню"
    if temperature > 20 and wind_speed < 20 and humidity < 0.5 and rain < 0.5:
        return "Гулять и кушать мороженку"
    return "Ну что-то серое непонятное"