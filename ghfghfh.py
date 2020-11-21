class Solution:
	def romanToInt(self, s: str) -> int:
		a=s[::-1]
		sum1=0
		max1=1
		z={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
		for i in a:
			d=z[i]
			if d>max1:
				max1=d
			if d<max1:
				sum1-=d
			if d==max1:
				sum1+=d
		return(sum1)

