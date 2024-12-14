# Klasy produktów
class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return (f"Car: {self.seats} seats, Engine: {self.engine}, "
                f"Trip Computer: {'Yes' if self.trip_computer else 'No'}, "
                f"GPS: {'Yes' if self.gps else 'No'}")


class Manual:
    def __init__(self):
        self.details = []

    def add_detail(self, detail):
        self.details.append(detail)

    def __str__(self):
        return "Manual: " + ", ".join(self.details)


# Interfejs budowniczego
class Builder:
    def reset(self):
        pass

    def set_seats(self, number):
        pass

    def set_engine(self, engine):
        pass

    def set_trip_computer(self, has_trip_computer):
        pass

    def set_gps(self, has_gps):
        pass


# Konkretne budownicze dla samochodu
class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_seats(self, number):
        self.car.seats = number

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self, has_trip_computer):
        self.car.trip_computer = has_trip_computer

    def set_gps(self, has_gps):
        self.car.gps = has_gps

    def get_product(self):
        product = self.car
        self.reset()
        return product


# Konkretne budownicze dla instrukcji obsługi
class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def set_seats(self, number):
        self.manual.add_detail(f"Seats: {number}")

    def set_engine(self, engine):
        self.manual.add_detail(f"Engine: {engine}")

    def set_trip_computer(self, has_trip_computer):
        if has_trip_computer:
            self.manual.add_detail("Trip Computer: Included")
        else:
            self.manual.add_detail("Trip Computer: Not Included")

    def set_gps(self, has_gps):
        if has_gps:
            self.manual.add_detail("GPS: Included")
        else:
            self.manual.add_detail("GPS: Not Included")

    def get_product(self):
        product = self.manual
        self.reset()
        return product


# Klasa kierownika
class Director:
    def construct_sports_car(self, builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("Sport Engine")
        builder.set_trip_computer(True)
        builder.set_gps(True)

    def construct_suv(self, builder):
        builder.reset()
        builder.set_seats(5)
        builder.set_engine("SUV Engine")
        builder.set_trip_computer(True)
        builder.set_gps(False)


# Kod kliencki
if __name__ == "__main__":
    director = Director()

    # Budowanie samochodu sportowego
    car_builder = CarBuilder()
    director.construct_sports_car(car_builder)
    car = car_builder.get_product()
    print(car)

    # Budowanie instrukcji obsługi do samochodu sportowego
    manual_builder = CarManualBuilder()
    director.construct_sports_car(manual_builder)
    manual = manual_builder.get_product()
    print(manual)
