def import_modules():
    # Import necessary modules dynamically
    from . import brain_calc
    from . import brain_even
    from . import brain_games
    from . import brain_gcd
    from . import brain_prime
    from . import brain_progression

    # Return imported modules
    return {
        "brain_calc": brain_calc,
        "brain_even": brain_even,
        "brain_games": brain_games,
        "brain_gcd": brain_gcd,
        "brain_prime": brain_prime,
        "brain_progression": brain_progression,
    }
