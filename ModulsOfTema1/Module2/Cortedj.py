tuple_1 = 1, 2, 3, 4, True, "Setting";
tuple_2 = (1, 2, 3);
tuple_3 = tuple([1, 2, 3,4]);
print(tuple_1);
print(tuple_2);
print(tuple_3);
print(tuple_1[0]);
list1 = [1, 2, 3, 4, True, "Setting"];
print(list1.__sizeof__());
print(tuple_1.__sizeof__());
tup = ([1, 2], 0);
print(tup);
tup[0][0] = 2;
print(tup);
print(tup + tuple_3);
print(tup * 3);

