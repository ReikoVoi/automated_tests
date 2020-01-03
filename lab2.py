import random
import prettytable
import datetime
import matplotlib.pyplot as plt

def selection_sort(nums):                   #сортировка выбором
    for i in range(len(nums)):
        lowest_value = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value]:
                lowest_value = j
        nums[i], nums[lowest_value] = nums[lowest_value], nums[i]


def sort(nums, low, high):                  #быстрая сортировка
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = sort(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)
list_of_nums = [random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50)]
quick_sort(list_of_nums)
#print(list_of_nums)

table = prettytable.PrettyTable(["Размер списка", "Время сортировки выбором", "Время быстрой сортировки"])
x=[]
y1=[]
y2=[]

for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()

    print("---")

    t1 = datetime.datetime.now()
    selection_sort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Сортировка выбором  " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    quick_sort(list_of_nums)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая сортировка  " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()