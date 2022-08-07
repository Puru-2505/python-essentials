n = int(input("Enter the value: "))
if n > 60:
  print("Value must be less than or equal to 60")
  exit(1)
a = (n < 20)*n+(n >=20)*20
b = (n-a < 10)*(n-a)+(n-a >=10)*10
c = (n-a-b < 30)*(n-a-b)+(n-a-b >=30)*30
print(f"a={a} b={b} c={c}")
