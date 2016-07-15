#! /usr/bin/python


def diff(a):

        n = len(a)
        max = a[1] - a[0]
        for i in range(n-1):
                for j in range(i+1, n):
                        if a[j]-a[i] > max:
                                max = a[j] - a[i]

        return max

a = [7,9,5,6,3,2]

print diff(a)

