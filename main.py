def main():
    testArray = [1,2,3,4,5,6,7,8,9]
    testSubarray = testArray[:5]
    testOtherSubarray = testArray[5+1:]
    print(testSubarray)
    print(testOtherSubarray)
    testArray.pop(5)
    print(testArray)
    print(testArray.pop(5))
    
main()