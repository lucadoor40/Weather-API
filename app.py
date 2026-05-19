
from flask import Flask

app = Flask(__name__)

class Weather:
    def __init__(self, cities):
        self.cities = cities

@app.route('/city/<name>')
def city(name):
    return f"City: {name}"

class Temperature(Weather):
    def __init__(self, cities, temperature):
        super().__init__(cities)
        self.temperature = temperature

@app.route('/climate/<name>')
def climate(name):
    if name == 'Jakarta':
        return f'{name}'
    elif name == 'Dhaka':
        return f'{name}'
    elif name == 'Tokyo':
        return f'{name}'
    elif name == 'New Delhi':
        return f'{name}'
    elif name == 'Shanghai':
        return f'{name}'
    elif name == 'Guangzhou':
        return f'{name}'
    elif name == 'Cairo':
        return f'{name}'
    elif name == 'Manila':
        return f'{name}'
    elif name == 'Kolkata':
        return f'{name}'
    elif name == 'Seoul':
        return f'{name}'
    else:
        return 'That is not a top 10 cities in the world by population'


@app.route('/conditions/<name>')
def conditions(name):
    if name == 'Jakarta':
        condition = 'Sunny'
    elif name == 'Dhaka':
        condition = 'Rainy'
    elif name == 'Tokyo':
        condition = 'Sunny'
    elif name == 'New Delhi':
        condition = 'Sunny'
    elif name == 'Shanghai':
        condition = 'Cloudy'
    elif name == 'Guangzhou':
        condition = 'Rainy'
    elif name == 'Cairo':
        condition = 'Partly Cloudy'
    elif name == 'Manila':
        condition = 'Sunny'
    elif name == 'Kolkata':
        condition = 'Sunny'
    elif name == 'Seoul':
        condition = 'Cloudy'
    else:
        condition = 'Unknown'
    return f'City: {name} - Condition: {condition}'

if __name__ == '__main__':
    app.run(debug=True)


