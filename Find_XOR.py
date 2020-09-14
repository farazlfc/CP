for _ in range(int(input())):
	n = int(input())
	ans1 = 0;
	print("1 1048576")
	sum = int(input())
	sum -= n*1048576;
	ans1 = 0;
	if sum%2: 
      		ans1 = 1;
	for i in range(1,20):
		print("1 " + str((1 << i)))
		sum1 = int(input())
		diff = sum - sum1;
		diff = diff/(1 << i);
		on = (n + diff)/2;
		if on%2 == 1:  #odd number of bits set!
			ans1 |= (1 << i);
	print("2 " + str(ans1))
	_ = int(input());
