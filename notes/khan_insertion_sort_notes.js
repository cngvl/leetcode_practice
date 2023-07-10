var insert = function (array, rightIndex, value) {
  println("inserting");
  for (var j = rightIndex; j >= 0 && array[j] > value; j--) {
    array[j + 1] = array[j];
  }
  array[j + 1] = value;
};

var insertionSort = function (array) {
  for (var subIndexStart = 1; subIndexStart < array.length; subIndexStart++) {
    insert(array, subIndexStart - 1, array[subIndexStart]);
  }
};

var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

var array2 = [5, 4, 3, 2, 1];
insertionSort(array2);
println("Array after sorting:  " + array2);
Program.assertEqual(array2, [1, 2, 3, 4, 5]);
