social_studies=int(input("Please tell me your social studies grades:"))
science=int(input("Please tell me your science grade:"))
math=int(input("Please tell me your math grade:"))
reading=int(input("Please tell me your reading grade:"))
PE=int(input("Please tell me your PE grade:"))

add=social_studies + science + math + reading + PE

def average(addition):
    print(addition/5)
average(add)
