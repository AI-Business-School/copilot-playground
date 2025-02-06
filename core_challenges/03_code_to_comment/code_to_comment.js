
function findPrimes(max) {
    const sieve = new Array(max + 1).fill(true);
    sieve[0] = sieve[1] = false;
    
    for (let i = 2; i <= Math.sqrt(max); i++) {
        if (sieve[i]) {
            for (let j = i * i; j <= max; j += i) {
                sieve[j] = false;
            }
        }
    }
    
    return sieve.reduce((primes, isPrime, num) => {
        if (isPrime) primes.push(num);
        return primes;
    }, []);
}

console.log(findPrimes(30));