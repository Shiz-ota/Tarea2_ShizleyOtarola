
import math

class Explosive:
    """
    Represents an explosive with its physical properties.

    Attributes:
        name (str): Commercial name of the explosive.
        density (float): Density of the explosive (kg/m³).
        vod (float): Velocity of detonation (m/s).
        rws (float): Relative strength compared to ANFO (%).
        water_resistant (bool): Indicates if the explosive is water resistant.
    """

    def __init__(self, name, density, vod, rws, water_resistant):
        self.name = name
        self.density = density
        self.vod = vod
        self.rws = rws
        self.water_resistant = water_resistant

    def detonation_pressure(self):
        return 0.25 * self.density * (self.vod ** 2)

    def linear_charge(self, diameter):
        return (math.pi / 4) * (diameter ** 2) * self.density

    def anfo_equivalent(self, mass):
        return (mass * self.rws) / 100

    def print_water_resistance(self):
        if self.water_resistant:
            print(f"{self.name} is water resistant.")
        else:
            print(f"{self.name} is NOT water resistant.")

    def __str__(self):
        return (
            f"Explosive: {self.name}\n"
            f"Density: {self.density} kg/m³\n"
            f"VOD: {self.vod} m/s\n"
            f"RWS: {self.rws}%\n"
            f"Water Resistant: {self.water_resistant}"
        )


class BenchBlasting(Explosive):
    """
    Represents a bench blasting operation using a specific explosive.
    """

    def __init__(self, name, density, vod, rws, water_resistant,
                 spacing, burden, bench_height, stemming, subdrilling,
                 rock_density, powder_factor, cost_per_kg):
        super().__init__(name, density, vod, rws, water_resistant)
        self.spacing = spacing
        self.burden = burden
        self.bench_height = bench_height
        self.stemming = stemming
        self.subdrilling = subdrilling
        self.rock_density = rock_density
        self.powder_factor = powder_factor
        self.cost_per_kg = cost_per_kg

    def bench_volume(self):
        return self.spacing * self.burden * self.bench_height

    def total_explosive_mass(self):
        return self.bench_volume() * self.powder_factor

    def total_anfo_equivalent(self):
        return self.anfo_equivalent(self.total_explosive_mass())

    def total_explosive_cost(self):
        return self.total_explosive_mass() * self.cost_per_kg

    def __str__(self):
        base = super().__str__()
        return (
            base +
            f"\n\n--- Bench Blasting Data ---\n"
            f"Volume: {self.bench_volume():.2f} m³\n"
            f"Explosive Mass: {self.total_explosive_mass():.2f} kg\n"
            f"ANFO Equivalent: {self.total_anfo_equivalent():.2f} kg\n"
            f"Total Cost: ${self.total_explosive_cost():.2f}"
        )


if __name__ == "__main__":
    expl1 = Explosive("Emulnor 3000", 1150, 4500, 80, True)
    expl2 = Explosive("Anfo", 800, 3200, 100, False)
    expl3 = Explosive("Emulind", 1250, 5000, 90, True)

    explosives = [expl1, expl2, expl3]

    for e in explosives:
        print("\n==============================")
        print(e)
        print(f"Detonation Pressure: {e.detonation_pressure():.2f} kPa")
        print(f"Linear Charge (D = 0.14 m): {e.linear_charge(0.14):.2f} kg/m")
        print(f"ANFO Equivalent (500 kg): {e.anfo_equivalent(500):.2f} kg")
        e.print_water_resistance()

    blasting = BenchBlasting(
        name="Emulnor 3000",
        density=1150,
        vod=4500,
        rws=80,
        water_resistant=True,
        spacing=3,
        burden=3,
        bench_height=10,
        stemming=1,
        subdrilling=0.5,
        rock_density=2600,
        powder_factor=0.6,
        cost_per_kg=4.5
    )

    print("\n==============================")
    print(blasting)
    print(f"\nDetonation Pressure: {blasting.detonation_pressure():.2f} kPa")
    print(f"Linear Charge (D = 0.14 m): {blasting.linear_charge(0.14):.2f} kg/m")
    blasting.print_water_resistance()
