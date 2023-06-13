// Iterative factorial
var factorial = function (n) {
  var result = 1;
  for (var i = result; i <= n; i++) {
    result = result * i;
  }
  return result;
};

println("The value of 5! should be " + 5 * 4 * 3 * 2 * 1);
println("The value of 5! is " + factorial(5));
println("The value of 0! should be 1");
println("The value of 0! is " + factorial(0));

// Program.assertEqual(factorial(5), 120);
// Program.assertEqual(factorial(0), 1);

// Program.assertEqual(factorial(3), 6);
// Program.assertEqual(factorial(4), 24);

var factorial = function (n) {
  // base case:
  if (n === 0) {
    return 1;
  }
  // recursive case:
  return n * factorial(n - 1);
};

println("The value of 0! is " + factorial(0) + ".");
println("The value of 5! is " + factorial(5) + ".");

// Program.assertEqual(factorial(0), 1);
// Program.assertEqual(factorial(5), 120);

// Program.assertEqual(factorial(2), 2);
// Program.assertEqual(factorial(3), 6);

// Is a string a palindrome?
// Returns the first character of the string str
var firstCharacter = function (str) {
  return str.slice(0, 1);
};

// Returns the last character of a string str
var lastCharacter = function (str) {
  return str.slice(-1);
};

// Returns the string that results from removing the first
//  and last characters from str
var middleCharacters = function (str) {
  return str.slice(1, -1);
};

var isPalindrome = function (str) {
  // base case #1
  if (str.length <= 1) {
    return true;
  }
  // base case #2
  if (firstCharacter(str) !== lastCharacter(str)) {
    return false;
  }
  // recursive case
  return isPalindrome(middleCharacters(str));
};

var checkPalindrome = function (str) {
  println("Is this word a palindrome? " + str);
  println(isPalindrome(str));
};

checkPalindrome("a");
Program.assertEqual(isPalindrome("a"), true);
checkPalindrome("motor");
Program.assertEqual(isPalindrome("motor"), false);
checkPalindrome("rotor");
Program.assertEqual(isPalindrome("rotor"), true);

Program.assertEqual(isPalindrome("test"), false);
Program.assertEqual(isPalindrome("zaz"), true);
