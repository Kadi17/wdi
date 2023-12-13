array = [0, 4, 6, 8, 4, -20, 100, -500]
class SequenceCounter():    

    def count_sequences(self, arr):
        def is_arithmetic(a, b, c):
            return 2 * b == a + c

        def is_geometric(a, b, c):
            return b * b == a * c

        arithmetic_count = 0
        geometric_count = 0

        for i in range(len(arr) - 2):
            if is_arithmetic(arr[i], arr[i + 1], arr[i + 2]):
                arithmetic_count += 1

            if is_geometric(arr[i], arr[i + 1], arr[i + 2]):
                geometric_count += 1

        if arithmetic_count > geometric_count:
            return 1
        elif arithmetic_count < geometric_count:
            return -1
        else:
            return 0


counter = SequenceCounter()
result = counter.count_sequences(array)
print(result)
