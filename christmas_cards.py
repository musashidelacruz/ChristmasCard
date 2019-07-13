def christmas_wrapper(christmas_message):
	print("Jingle Bells, Jingle Bells, \n Jingle All The Way...\n")
	christmas_message()
	print("Ho Ho Ho, Marry Chirstmas \n With Love, \n Musashi")

@christmas_wrapper
def christmas_message():
	#type a personallized message to insert in generic wrapper
	input()
