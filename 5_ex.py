# 演習問題1.
# data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
# 上のリストから、「7」をprint関数で取り出してください。

# 演習問題2.
# 空のリストを定義し、組み込み関数input()を3回呼び出して数値を入力し、空のリストに数値を追加してください。
# そのリストをprint()関数で表示しますが、その際に sortメソッドを使ってソートされて表示するようにしてください。（昇順、小さい数値が先に表示される）

# 演習問題3.
# 空のリストを定義し、組み込み関数input()を3回呼び出して数値を入力し、空のリストに数値を追加してください。その際appendメソっドではなくinsertメソッドを使ってください。
# そのリストをprint()関数で表示しますが、その際に組み込み関数sortedを使ってソートされて表示するようにしてください。（降順、大きい数値が先に表示される）


# 1
data_list = [1,2,[3,4,5],[6,7],8,9,[10,11]]
print(data_list[3][1])

# 2
empty_list = []

first_input = input()
second_input = input()
third_input = input()

empty_list.append(first_input)
empty_list.append(second_input)
empty_list.append(third_input)
sorted_empty_list = sorted(empty_list)
print(sorted_empty_list)

# 3
empty_list2 = []

first_input2 = input()
second_input2 = input()
third_input2 = input()

empty_list2.insert(0,first_input2)
empty_list2.insert(1,second_input2)
empty_list2.insert(2,third_input2)
sorted_empty_list2 = sorted(empty_list2, reverse=True)
print(sorted_empty_list2)

