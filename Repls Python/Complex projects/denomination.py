def no_notes (a):
  Q = [1000, 500, 200, 100, 50, 20, 10, 5, 2]
  x = 0
  for i in range(7):
    q = Q[i]
    x = a//q
    print("Notes of {} = {}".format(q, x))
    a = a%q 

amount = int(input("total amount: "))
no_notes(amount)