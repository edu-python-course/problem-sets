import primes


def test_is_prime():
    assert primes.is_prime(10) is False
    assert primes.is_prime(1) is False
    assert primes.is_prime(2) is True
    assert primes.is_prime(3) is True
    assert primes.is_prime(547) is True


def test_get_primes(limit, first_1000_primes):
    assert primes.get_primes(limit) == first_1000_primes


def test_eratosthenes_sieve(limit, first_1000_primes):
    assert primes.eratosthenes_sieve(limit) == first_1000_primes
