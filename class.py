#! /usr/bin/python
class afjal:
	number=0
	name="noname"
def main():
	me=afjal()
	me.number=13337
	me.name="shilpi"

	friend=afjal()
	friend.number=3
	friend.name="sexy"
	
	empty=afjal()
	print "name:" + me.name + ", Fav number: " + str(me.number)
	print "name:" + friend.name + ", Fav number: " + str(friend.number)
	print "name:" + empty.name + ", Fav number: " + str(empty.number)

if __name__=='__main__':
	main()
