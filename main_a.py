import test_module_a as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

print("메인파일입니다")
print(__name__)
