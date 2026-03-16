class Distance:

    conversion = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.conversion[self.unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только Distance")

        total_meters = self.to_meters() + other.to_meters()
        new_value = total_meters / self.conversion[self.unit]
        return Distance(new_value, self.unit)


distance_1 = Distance(10, "m")
distance_2 = Distance(2, "km")
distance_3 = Distance(50, "cm")
print(distance_1)
print(distance_2)
result = distance_1 + distance_2
print(result)
result2 = distance_1 + distance_3
print(result2)