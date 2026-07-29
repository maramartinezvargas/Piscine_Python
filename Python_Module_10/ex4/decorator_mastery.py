import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints execution time of a spell."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """Decorator factory that validates whether spell power is sufficient."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None:
                # Search positional args for the power parameter (int)
                for arg in args:
                    if isinstance(arg, int) and not isinstance(arg, bool):
                        power = arg
                        break

            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """Decorator that retries a spell upon failure up to max_attempts."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... (attempt "
                              f"{attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if mage name is valid (>= 3 chars, letters/spaces only)."""
        if not isinstance(name, str) or len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power level meets requirement."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    res = fireball()
    print(f"Result: {res}\n")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def failing_spell() -> str:
        raise ValueError("Magic power corrupted!")

    res_retry = failing_spell()
    print(res_retry)
    print("Waaaaaaagh spelled !\n")

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf The Grey"))  # True
    print(MageGuild.validate_mage_name("A1"))                # False

    guild = MageGuild()
    # Sufficient power for this spell
    print(guild.cast_spell("Lightning", 15))
    # Insufficient power for this spell
    print(guild.cast_spell("Lightning", 5))
