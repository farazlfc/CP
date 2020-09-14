for _ in range(int(input())):
		n = int(input())
		ans1 = 0;
		print("1 1048576")
		sum = int(input())
		sum -= n*1048576;
		if sum%2: 
      ans1 = 1;
		for(int i = 1; i <= 19; i++){
			cout << 1 << " " << (1 << i) << endl;
			ll sum1;
			cin >> sum1;
			ll diff = sum - sum1;
			diff = diff/(1LL << i);
			ll on = (n + diff)/2;
			if(on%2 == 1) ans1 |= (1 << i);
		}
		cout << 2 << " " << ans1 << endl;
		int j;
		cin >> j;
		assert(j == 1);
	}
