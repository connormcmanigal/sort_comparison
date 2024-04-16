from sorting import MergeSort, QuickSort, InsertionSort, ShellSort, BucketSort

merge_sorter = MergeSort()
quick_sorter = QuickSort()
insertion_sort = InsertionSort()
shell_sort = ShellSort([4, 3, 1])
bucket_sort = BucketSort(100)
data = [99,1,4,2,7,71,69,1,9,5,10,4,3,1]

print(data)
#sorted = merge_sorter.sort(data)
#sorted = quick_sorter.sort(data)
#sorted = insertion_sort.sort(data)
#sorted = shell_sort.sort(data)
sorted = bucket_sort.sort(data)
print(sorted)