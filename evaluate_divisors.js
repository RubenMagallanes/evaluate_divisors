
/* current implementation passes tests imcluding rangs up to 10 billion in about 2 seconds */
function iSquaredHasKDivisors(i, k) 
{
	var num = i * i; // num is perfect sq, root $i
	var count = 0;
	var step = 1
	
	if (num %2 != 0) // if numbers odd we can skip even factors
	{
		step = 2;
	}
	
	for (var root = 1; root < i; root += step) // loop from 1 to root of num (which is i)
		{
			if (num % root == 0) // check if $root actually is a divisor [probably bad var name]
			{ 
				count += 2; // add 2 because each factor found has another on other side of sqrt(num)
				if (count > k) // instantly break if too many factors
				{
					return false;
				}
			}
		}
	count ++; // plus 1 for the square root

	if (k == count)
	{
		return true;
	}
	else return false;
}

function evaluateDivisors(a, b, k)
{
	var count = 0; // number of ints with k divisors

	var startSq = Math.ceil(Math.sqrt(a));
	var endSq = Math.floor(Math.sqrt(b));
	for (var i = startSq; i<= endSq; i++) // loop through roots of perfect squares from a to b 
	{
			var kDivs = iSquaredHasKDivisors(i, k); // true if (i*i) has k divisors
			if (kDivs) 
			{
				count ++;
			}
	}

	return count;
}
