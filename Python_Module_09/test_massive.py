#!/usr/bin/env python3
"""
Massive validation test script for Module 09.
This script tests ex0, ex1, and ex2 against the generated datasets.
"""

import json
from pydantic import ValidationError

# Importación de tus modelos desde las carpetas de los ejercicios
from ex0.space_station import SpaceStation
from ex1.alien_contact import AlienContact
from ex2.space_crew import SpaceMission

# Importación de los datasets válidos en formato Python
from generated_data.space_stations import SPACE_STATIONS
from generated_data.alien_contacts import ALIEN_CONTACTS
from generated_data.space_missions import SPACE_MISSIONS


def test_exercise_0() -> None:
    """Tests ex0 (SpaceStation) with massive data."""
    print("\n--- Testing EX0: SpaceStation ---")
    
    # 1. Datos válidos
    valid_count = 0
    for item in SPACE_STATIONS:
        try:
            SpaceStation.model_validate(item)
            valid_count += 1
        except ValidationError as e:
            print(f"❌ Unexpected error in valid station: {e}")
    print(f"✅ VÁLIDOS: {valid_count}/{len(SPACE_STATIONS)} pasados.")

    # 2. Datos inválidos
    try:
        with open("generated_data/invalid_stations.json", "r") as f:
            invalid_data = json.load(f)
        invalid_count = 0
        for item in invalid_data:
            try:
                SpaceStation.model_validate(item)
                print("❌ Error: An invalid station bypassed validation!")
            except ValidationError:
                invalid_count += 1
        print(f"✅ INVÁLIDOS: {invalid_count}/{len(invalid_data)} atrapados.")
    except FileNotFoundError:
        print("⚠ Missing invalid_stations.json")


def test_exercise_1() -> None:
    """Tests ex1 (AlienContact) with massive data."""
    print("\n--- Testing EX1: AlienContact ---")
    
    # 1. Datos válidos
    valid_count = 0
    for item in ALIEN_CONTACTS:
        try:
            AlienContact.model_validate(item)
            valid_count += 1
        except ValidationError as e:
            print(f"❌ Unexpected error in valid contact: {e}")
    print(f"✅ VÁLIDOS: {valid_count}/{len(ALIEN_CONTACTS)} pasados.")

    # 2. Datos inválidos
    try:
        with open("generated_data/invalid_contacts.json", "r") as f:
            invalid_data = json.load(f)
        invalid_count = 0
        for item in invalid_data:
            try:
                AlienContact.model_validate(item)
                print("❌ Error: An invalid contact bypassed validation!")
            except ValidationError:
                invalid_count += 1
        print(f"✅ INVÁLIDOS: {invalid_count}/{len(invalid_data)} atrapados.")
    except FileNotFoundError:
        print("⚠ Missing invalid_contacts.json")


def test_exercise_2() -> None:
    """Tests ex2 (SpaceMission) with massive data."""
    print("\n--- Testing EX2: SpaceMission ---")
    
    # 1. Datos válidos (Misiones con Crews anidados)
    valid_count = 0
    for item in SPACE_MISSIONS:
        try:
            SpaceMission.model_validate(item)
            valid_count += 1
        except ValidationError as e:
            print(f"❌ Unexpected error in valid mission: {e}")
    print(f"✅ VÁLIDOS: {valid_count}/{len(SPACE_MISSIONS)} pasados.")


def main() -> None:
    print("=" * 50)
    print("🚀 RUNNING MASSIVE VALIDATION FOR ALL EXERCISES 🚀")
    print("=" * 50)
    
    test_exercise_0()
    test_exercise_1()
    test_exercise_2()
    
    print("\n" + "=" * 50)
    print("🎯 All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()