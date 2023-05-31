var swap = function (array, firstIndex, secondIndex) {
  var temp = array[firstIndex];
  array[firstIndex] = array[secondIndex];
  array[secondIndex] = temp;
};

var indexOfMinimum = function (array, startIndex) {
  var minValue = array[startIndex];
  var minIndex = startIndex;

  for (var i = minIndex + 1; i < array.length; i++) {
    if (array[i] < minValue) {
      minIndex = i;
      minValue = array[i];
    }
  }
  return minIndex;
};

var selectionSort = function (array) {
  var minimum = 0;
  for (var position = 0; position < array.length; position++) {
    minimum = indexOfMinimum(array, position);
    swap(array, minimum, position);
  }
};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
println("Array after sorting:  " + array);

// Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

var testArray = [1, 2, 3, 0];
selectionSort(testArray);
// Program.assertEqual(testArray, [0, 1, 2, 3]);
