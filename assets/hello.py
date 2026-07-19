"""
Project status:
Temporarily paused.

Current exception:
    EnergyError: Not enough coffee and motivation.

The program will automatically resume
when `energy_level >= 100`.
"""

import random
import time


class EnergyError(Exception):
    pass


def check_energy():
    # Aktualny poziom energii programisty 😅
    energy = random.randint(0, 30)

    if energy < 100:
        raise EnergyError(
            f"Energy level: {energy}%\n"
            "I'll come back to this project when future me has more energy."
        )


if __name__ == "__main__":
    print("Starting project...")
    time.sleep(1)

    try:
        check_energy()
        print("Let's code! 🚀")
    except EnergyError as e:
        print(e)
        print("\nEstimated return time: ¯\\_(ツ)_/¯")
        print("See you soon... probably. ☕")