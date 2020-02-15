def apartment_filters(query):
	result = {}
	if "property_type" in query:
		result["property_type"] = query["property_type"]
	if "country" in query:
		result["country"] = query["country"]
	if "city" in query:
		result["city"] = query["city"]
	if "minPrice" in query:
		result["price"] = {'$gt': int(query["minPrice"])}
	if "maxPrice" in query:
		result["price"] = {'$lt': int(query["maxPrice"])}
	if "minRooms" in query:
		result["number_of_room"] = {'$gt': int(query["minRooms"])}
	if "maxRooms" in query:
		result["number_of_room"] = {'$lt': int(query["maxRooms"])}
	if "minBath" in query:
		result["number_of_bath"] = {'$gt': int(query["minBath"])}
	if "maxBath" in query:
		result["number_of_bath"] = {'$lt': int(query["maxBath"])}
	if "sale_status" in query:
		result["sale_status"] = query["sale_status"]
	if "availability" in query:
		result["availability"] = query["availability"]
	if "status" in query:
		result["status"] = query["status"]
	return result

