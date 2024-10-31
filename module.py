import time as t
localTime = t.localtime()
print(f"Transaction completed at {localTime.tm_year}:{localTime.tm_mon}:{localTime.tm_mday} {localTime.tm_hour}:{localTime.tm_min}:{localTime.tm_sec}")
print(t.time())

timeNow = t.time()
deliveryTime = timeNow + (86400 * 7)
print(deliveryTime)
estimatedTime = t.localtime(deliveryTime)
print(estimatedTime)
print(f"Your order delivery date is {estimatedTime.tm_year}:{estimatedTime.tm_mon}:{estimatedTime.tm_mday} {estimatedTime.tm_hour}:{estimatedTime.tm_min}:{estimatedTime.tm_sec}")