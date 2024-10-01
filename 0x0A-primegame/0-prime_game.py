#!/usr/bin/python3
"""
Prime Game
Maria and Ben are playing a game where they choose prime numbers from a set and
remove their multiples. The player who cannot make a move loses.
"""


def sieve_of_eratosthenes(max_n):
    """Generates a list of primes using the Sieve of Eratosthenes."""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(max_n ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_n + 1, start):
                sieve[multiple] = False
    return sieve


def count_primes_up_to(n, prime_flags):
    """Counts how many primes are <= n using the precomputed sieve."""
    return sum(prime_flags[:n + 1])


def isWinner(x, nums):
    """
    Determines the winner of the game.
    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing n for each round.

    Returns:
        str or None: The name of the player that won the most rounds,
                     or None if there's no clear winner.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)
    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = count_primes_up_to(n, prime_flags)
        
        # If the number of primes is odd, Maria wins; if even, Ben wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
