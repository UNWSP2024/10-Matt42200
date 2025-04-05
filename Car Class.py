class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Initial speed is 0


    def accelerate(self):
        """Increases the car's speed by 5."""
        self.__speed += 5


    def brake(self):
        """Decreases the car's speed by 5."""
        self.__speed -= 5


    def get_speed(self):
        """Returns the current speed of the car."""
        return self.__speed




my_car = Car(2021, "Toyota")


for _ in range(5):
    my_car.accelerate()
    print(f"Current speed after accelerating: {my_car.get_speed()} mph")


for _ in range(5):
    my_car.brake()
    print(f"Current speed after braking: {my_car.get_speed()} mph")